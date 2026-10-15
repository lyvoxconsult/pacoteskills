"""Read-only plan review; never executes Terraform or grants authorization."""

import argparse
import hashlib
import json
import sys
from pathlib import Path


class PlanError(ValueError):
    """Input cannot safely support a plan review."""


KNOWN_ACTIONS = {"no-op", "read", "create", "update", "delete", "forget"}
MAX_BYTES = 32 * 1024 * 1024


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PlanError("Duplicate JSON object key")
        result[key] = value
    return result


def _actions(change):
    if not isinstance(change, dict):
        raise PlanError("Invalid change object")
    actions = change.get("actions")
    if not isinstance(actions, list) or not actions:
        raise PlanError("Missing change actions")
    if any(not isinstance(action, str) or action not in KNOWN_ACTIONS for action in actions):
        raise PlanError("Unsupported change action")
    if len(set(actions)) != len(actions):
        raise PlanError("Duplicate change actions")
    if len(actions) > 1 and set(actions) != {"create", "delete"}:
        raise PlanError("Unsupported action combination")
    return actions


def review_plan(plan):
    if not isinstance(plan, dict):
        raise PlanError("Plan must be an object")
    version = plan.get("format_version")
    if not isinstance(version, str) or not version.startswith("1.") or not version[2:].isdigit():
        raise PlanError("Unsupported plan JSON format")
    for flag in ("complete", "errored", "applyable"):
        if flag in plan and not isinstance(plan[flag], bool):
            raise PlanError("Invalid plan status flag")
    deferred = plan.get("deferred_changes", [])
    if not isinstance(deferred, list):
        raise PlanError("Invalid deferred change list")
    if plan.get("complete") is False or plan.get("errored") is True or deferred:
        raise PlanError("Incomplete or errored plan requires manual investigation")
    changes = plan.get("resource_changes")
    if "resource_changes" not in plan:
        if not isinstance(plan.get("planned_values"), dict):
            raise PlanError("Missing plan change information")
        changes = []
    if not isinstance(changes, list):
        raise PlanError("Invalid resource change list")
    review_items = []
    object_keys = set()
    for resource in changes:
        if not isinstance(resource, dict):
            raise PlanError("Invalid resource object")
        address = resource.get("address")
        if not isinstance(address, str) or not address.strip():
            raise PlanError("Missing resource address")
        deposed = resource.get("deposed")
        if "deposed" in resource and (not isinstance(deposed, str) or not deposed.strip()):
            raise PlanError("Invalid deposed object key")
        object_key = (address, deposed)
        if object_key in object_keys:
            raise PlanError("Duplicate resource object")
        object_keys.add(object_key)
        actions = _actions(resource.get("change"))
        if "delete" in actions or "forget" in actions:
            item = {"address": address, "actions": actions}
            if deposed is not None:
                item["deposed"] = deposed
            review_items.append(item)
    outputs = plan.get("output_changes", {})
    if not isinstance(outputs, dict):
        raise PlanError("Invalid output change map")
    for name, change in outputs.items():
        if not isinstance(name, str) or not name.strip():
            raise PlanError("Invalid output name")
        actions = _actions(change)
        if "delete" in actions or "forget" in actions:
            review_items.append({"address": "output." + name, "actions": actions})
    return {
        "status": "HUMAN_REVIEW_REQUIRED" if review_items else "NO_EXPLICIT_DELETION_DETECTED",
        "review_items": review_items,
        "authorization_granted": False,
        "limitations": [
            "No provider calls or approval authentication performed",
            "Updates, provisioners and remote lifecycle policies may delete data indirectly",
            "Addresses can contain private metadata; protect this output",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan_json", help="Protected JSON from terraform/tofu show -json")
    args = parser.parse_args(argv)
    try:
        path = Path(args.plan_json)
        if path.stat().st_size > MAX_BYTES:
            raise PlanError("Plan exceeds local review size limit")
        raw = path.read_bytes()
        if len(raw) > MAX_BYTES:
            raise PlanError("Plan exceeds local review size limit")
        result = review_plan(json.loads(raw, object_pairs_hook=_unique_object))
        result["artifact_sha256"] = hashlib.sha256(raw).hexdigest()
    except (OSError, ValueError, RecursionError):
        # Do not echo raw JSON, paths or decoder fragments from sensitive input.
        print(json.dumps({"status": "UNREVIEWABLE", "authorization_granted": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 3 if result["review_items"] else 0


if __name__ == "__main__":
    sys.exit(main())
