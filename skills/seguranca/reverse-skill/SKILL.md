---
name: reverse-skill
description: "Route authorized reverse-engineering and security-research tasks to the correct safe workflow and tooling"
category: security
risk: medium
source: curated-community
tags: "[reverse-engineering, security-research, authorized-testing, routing, tooling]"
date_added: "2026-08-28"
---

## Purpose

This skill helps route authorized reverse-engineering and security-research work without mixing it with unrelated product tasks.
It is limited to lawful, authorized analysis and defensive research.

## When to Use

Use this skill when the user explicitly requests:

- Authorized reverse engineering
- Security research on owned or permitted targets
- Binary, protocol, or obfuscation analysis
- Toolchain selection for a sanctioned lab or assessment

## Workflow

1. Confirm authorization and the exact target scope.
2. Separate defensive research from exploit construction.
3. Select only the minimum toolchain needed for the authorized task.
4. Record assumptions, inputs, and observed behavior.
5. Prefer reproducible, inspectable steps over opaque automation.

## Safety Boundaries

- Do not assist with unauthorized access or exploitation.
- Do not invent permission or scope.
- Do not treat a public repository as permission to attack real targets.
- When a request is ambiguous, stop and ask for scope clarification.

