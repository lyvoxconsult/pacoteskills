---
name: security-skill
description: Use for application security, OWASP Top 10 review, DevSecOps, dependency/container scanning, authentication, authorization, secret handling, input validation, RLS, API hardening, threat modeling, and vulnerability remediation. Trigger before shipping user-facing, admin, auth, payment, file, database, or infrastructure changes.
---

# Security Skill

Use this skill to make security part of the implementation, not a final cosmetic scan.

Reference repositories:
- https://github.com/OWASP/Top10
- https://github.com/TaptuIT/awesome-devsecops
- https://github.com/aquasecurity/trivy

Note: `https://github.com/TaptuIT/DevSecOps-Guide` was requested, but it is not accessible as a public Git repository. `TaptuIT/awesome-devsecops` is the validated public TaptuIT DevSecOps reference.

## Workflow

1. Identify assets, actors, trust boundaries, and exposed inputs.
2. Check authorization at the backend or data layer; do not rely only on hidden UI.
3. Validate input, output encoding, rate limits, and error disclosure for exposed routes.
4. Review secrets, tokens, environment variables, logs, and client bundles.
5. Use the repo's existing scanners first. If Trivy is available, prefer it for filesystem, dependency, image, and IaC scanning.
6. Prioritize findings by exploitability and blast radius. Fix high-risk issues before broad cleanup.
7. Verify with tests, scanner output, or a concrete manual exploit check.

## Commands To Prefer When Available

- `trivy fs .`
- `trivy config .`
- `trivy image <image>`
- `npm audit --audit-level=high`
- `pnpm audit --audit-level high`
- `pip-audit`

## Review Checklist

- Authentication and authorization are enforced server-side.
- Sensitive data is not included in public payloads, logs, localStorage, or client-only state.
- Database access policies match business ownership.
- Dependencies and containers have no untriaged critical or high findings.
- Error responses do not expose internals.
