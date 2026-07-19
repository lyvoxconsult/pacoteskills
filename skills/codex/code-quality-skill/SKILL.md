---
name: code-quality-skill
description: Use for linting, formatting, maintainability review, static analysis, ESLint, Prettier, SonarQube, TypeScript strictness, code smells, complexity reduction, and repository quality gates. Trigger before finalizing code changes or when the user asks for cleanup, review, standards, or refactoring.
---

# Code Quality Skill

Use this skill to keep changes consistent with the repository instead of imposing a new style.

Reference repositories:
- https://github.com/eslint/eslint
- https://github.com/prettier/prettier
- https://github.com/SonarSource/sonarqube

## Workflow

1. Inspect package scripts and config files before choosing commands.
2. Preserve existing formatting rules and lint conventions.
3. Prefer targeted fixes for touched files unless the user asked for broad cleanup.
4. Treat lint, type, and static-analysis failures as behavior risks when they affect runtime paths.
5. Avoid churn: do not reformat unrelated files or rename symbols without a concrete reason.
6. Verify with the repo's own quality gate: lint, typecheck, tests, or Sonar scanner when configured.

## Commands To Prefer When Available

- `npm run lint`
- `npm run typecheck`
- `npm run format:check`
- `npx eslint <files>`
- `npx prettier --check <files>`
- `sonar-scanner`

## Review Checklist

- Code follows local patterns and naming.
- Error handling is explicit where failure is expected.
- Shared helpers are introduced only when duplication is meaningful.
- Public contracts and types remain stable.
- No unrelated formatting or metadata churn.
