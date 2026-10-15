"""Synthetic local tests; no files, subprocesses or infrastructure mutations."""

import contextlib
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from review_terraform_plan import MAX_BYTES, PlanError, main, review_plan


def plan(actions=None):
    changes = [] if actions is None else [{
        "address": "example_vm.app",
        "change": {"actions": actions, "before": {"secret": "synthetic-marker"}},
    }]
    return {"format_version": "1.2", "resource_changes": changes, "complete": True}


class ReviewTests(unittest.TestCase):
    def test_non_destructive_actions(self):
        for actions in (None, ["create"], ["read"], ["update"], ["no-op"]):
            with self.subTest(actions=actions):
                result = review_plan(plan(actions))
                self.assertEqual(result["status"], "NO_EXPLICIT_DELETION_DETECTED")
                self.assertFalse(result["authorization_granted"])

    def test_destructive_actions(self):
        for actions in (["delete"], ["delete", "create"], ["create", "delete"], ["forget"]):
            with self.subTest(actions=actions):
                result = review_plan(plan(actions))
                self.assertEqual(result["status"], "HUMAN_REVIEW_REQUIRED")
                self.assertEqual(result["review_items"][0]["actions"], actions)

    def test_sensitive_values_not_returned(self):
        self.assertNotIn("synthetic-marker", json.dumps(review_plan(plan(["delete"]))))

    def test_missing_changes_with_planned_values(self):
        self.assertEqual(review_plan({"format_version": "1.0", "planned_values": {}})["review_items"], [])

    def test_missing_change_information(self):
        with self.assertRaises(PlanError):
            review_plan({"format_version": "1.0"})

    def test_unknown_action(self):
        with self.assertRaises(PlanError):
            review_plan(plan(["future-delete"]))

    def test_invalid_action_combination(self):
        with self.assertRaises(PlanError):
            review_plan(plan(["read", "delete"]))

    def test_duplicate_actions(self):
        with self.assertRaises(PlanError):
            review_plan(plan(["delete", "delete"]))

    def test_unknown_format(self):
        data = plan()
        data["format_version"] = "2.0"
        with self.assertRaises(PlanError):
            review_plan(data)

    def test_incomplete_or_errored(self):
        for field, value in (("complete", False), ("errored", True), ("deferred_changes", [{}])):
            with self.subTest(field=field):
                data = plan()
                data[field] = value
                with self.assertRaises(PlanError):
                    review_plan(data)

    def test_invalid_flag(self):
        data = plan()
        data["complete"] = "true"
        with self.assertRaises(PlanError):
            review_plan(data)

    def test_missing_address(self):
        data = plan(["delete"])
        del data["resource_changes"][0]["address"]
        with self.assertRaises(PlanError):
            review_plan(data)

    def test_duplicate_address(self):
        data = plan(["delete"])
        data["resource_changes"].append(data["resource_changes"][0])
        with self.assertRaises(PlanError):
            review_plan(data)

    def test_output_deletion(self):
        data = plan()
        data["output_changes"] = {"old_endpoint": {"actions": ["delete"], "before": "synthetic-marker"}}
        result = review_plan(data)
        self.assertEqual(result["review_items"][0]["address"], "output.old_endpoint")
        self.assertNotIn("synthetic-marker", json.dumps(result))

    def test_current_and_deposed_objects(self):
        data = plan(["update"])
        data["resource_changes"].append({
            "address": "example_vm.app", "deposed": "deadbeef",
            "change": {"actions": ["delete"]},
        })
        result = review_plan(data)
        self.assertEqual(result["status"], "HUMAN_REVIEW_REQUIRED")
        self.assertEqual(result["review_items"][0]["deposed"], "deadbeef")

    def test_duplicate_deposed_object(self):
        data = plan(["delete"])
        data["resource_changes"][0]["deposed"] = "deadbeef"
        data["resource_changes"].append(data["resource_changes"][0])
        with self.assertRaises(PlanError):
            review_plan(data)

    def test_invalid_deposed_keys(self):
        for key in (None, "", [], 1):
            with self.subTest(key=key):
                data = plan(["delete"])
                data["resource_changes"][0]["deposed"] = key
                with self.assertRaises(PlanError):
                    review_plan(data)

    def test_invalid_input_shapes(self):
        for data in ([], None, {"format_version": "1.0", "resource_changes": {}}, plan([None]), plan([])):
            with self.subTest(data=data):
                with self.assertRaises(PlanError):
                    review_plan(data)

    def test_cli_exit_codes_and_no_writes(self):
        for actions, expected in ((["create"], 0), (["delete"], 3)):
            with self.subTest(actions=actions):
                with patch.object(Path, "stat") as stat, patch.object(Path, "read_bytes") as read:
                    stat.return_value.st_size = 100
                    read.return_value = json.dumps(plan(actions)).encode()
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        self.assertEqual(main(["synthetic-plan.json"]), expected)
                    result = json.loads(output.getvalue())
                    self.assertFalse(result["authorization_granted"])
                    self.assertEqual(len(result["artifact_sha256"]), 64)

    def test_cli_invalid_json_does_not_echo(self):
        with patch.object(Path, "stat") as stat, patch.object(Path, "read_bytes") as read:
            stat.return_value.st_size = 10
            read.return_value = b"synthetic-sensitive-invalid-json"
            output = io.StringIO()
            with contextlib.redirect_stderr(output):
                self.assertEqual(main(["synthetic-plan.json"]), 2)
            self.assertNotIn("synthetic-sensitive", output.getvalue())

    def test_cli_size_limit(self):
        with patch.object(Path, "stat") as stat, patch.object(Path, "read_bytes") as read:
            stat.return_value.st_size = MAX_BYTES + 1
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(["synthetic-plan.json"]), 2)
            read.assert_not_called()

    def test_null_resource_changes(self):
        with self.assertRaises(PlanError):
            review_plan({"format_version": "1.0", "resource_changes": None, "planned_values": {}})

    def test_invalid_deferred_shape(self):
        data = plan()
        data["deferred_changes"] = {}
        with self.assertRaises(PlanError):
            review_plan(data)

    def test_cli_duplicate_json_keys(self):
        with patch.object(Path, "stat") as stat, patch.object(Path, "read_bytes") as read:
            stat.return_value.st_size = 100
            read.return_value = b'{"format_version":"1.0","resource_changes":[],"resource_changes":[]}'
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(["synthetic-plan.json"]), 2)


if __name__ == "__main__":
    unittest.main()
