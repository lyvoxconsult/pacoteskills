---
name: architecture-skill
description: Use for software architecture, system design, Clean Architecture boundaries, modularization, scalability analysis, technical tradeoffs, ADRs, refactors, and senior design reviews. Trigger when work may affect module boundaries, data flow, persistence, integrations, maintainability, or cross-service behavior.
---

# Architecture Skill

Use this skill before changing architectural boundaries or designing new modules.

Reference repositories:
- https://github.com/gsd-build/get-shit-done
- https://github.com/ardalis/CleanArchitecture
- https://github.com/donnemartin/system-design-primer

## Workflow

1. Read the existing code and runtime flow before proposing structure.
2. Identify the current boundaries: UI, application services, domain logic, persistence, external integrations, background jobs, and configuration.
3. Diagnose the real constraint: coupling, ownership, scalability, latency, security, operational risk, or maintainability.
4. Prefer the smallest structural change that preserves current behavior and improves the weak boundary.
5. Separate business rules from framework glue when the codebase already supports that direction.
6. For new modules, define data ownership, access paths, failure modes, and migration strategy before implementation.
7. Record important tradeoffs in concise comments, docs, or an ADR only when the repo already uses that pattern or the decision is likely to be revisited.

## Review Checklist

- Clear dependency direction and no accidental circular ownership.
- Domain or business logic is not trapped in presentation components or controllers.
- Persistence contracts are explicit and tested at the boundary.
- New abstractions remove real complexity; they are not decorative.
- Failure, retry, and partial-state behavior are understood.
- Changes can be verified with focused tests or runtime checks.
