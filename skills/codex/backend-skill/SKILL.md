---
name: backend-skill
description: Use for backend API design and implementation with FastAPI, NestJS, REST, service layers, controllers, DTOs, validation, persistence, authentication, authorization, migrations, background jobs, and API performance. Trigger for server routes, database access, backend contracts, or integration changes.
---

# Backend Skill

Use this skill when backend behavior, API contracts, or persistence paths are involved.

Reference repositories:
- https://github.com/fastapi/fastapi
- https://github.com/nestjs/nest

## Workflow

1. Read route, service, persistence, and auth flow before editing.
2. Keep controllers thin: validate input, call application/service logic, return typed responses.
3. Put business rules in services or domain modules that can be tested without HTTP.
4. Enforce authorization at the backend and database boundary.
5. Treat migrations and API response shapes as contracts; preserve compatibility unless explicitly changing them.
6. Add logging and errors that help operators without leaking sensitive details.
7. Verify with unit, integration, and API-level tests appropriate to the change.

## Framework Guidance

- FastAPI: prefer Pydantic models, dependency injection for auth/session concerns, explicit response models, and async only when the stack supports it end-to-end.
- NestJS: prefer modules with clear providers, DTO validation pipes, guards for authorization, and injectable services for testable logic.

## Review Checklist

- Input validation is explicit.
- Data access is scoped and authorized.
- Transactions or consistency controls exist where partial writes are possible.
- API errors are stable and do not expose internals.
- Performance-sensitive paths avoid avoidable N+1 calls.
