---
name: testing-skill
description: Use for automated testing strategy and implementation with Jest, Playwright, pytest, unit tests, integration tests, end-to-end tests, regression tests, fixtures, mocks, coverage, and verification plans. Trigger whenever behavior changes, bugs are fixed, persistence is touched, or UI flows need validation.
---

# Testing Skill

Use this skill to prove the behavior that matters, not to chase coverage mechanically.

Reference repositories:
- https://github.com/jestjs/jest
- https://github.com/microsoft/playwright
- https://github.com/pytest-dev/pytest

## Workflow

1. Identify the risk introduced by the change.
2. Choose the lowest reliable test level: unit for pure logic, integration for boundaries, browser tests for user flows, manual checks only when automation is impractical.
3. Reuse existing test utilities, fixtures, factories, and scripts.
4. Add regression tests for fixed bugs when the failure can be reproduced deterministically.
5. Keep tests independent, deterministic, and clear about the expected behavior.
6. Run the narrowest useful test first, then the broader suite when the blast radius justifies it.

## Commands To Prefer When Available

- `npm test`
- `npm run test`
- `npx jest <pattern>`
- `npx playwright test`
- `pytest`
- `pytest <path>`

## Review Checklist

- The changed behavior has direct verification.
- Edge cases cover empty, invalid, unauthorized, stale, and persistence states when relevant.
- Browser tests assert visible outcomes and important network/data effects.
- Mocks do not hide the integration being validated.
- Failing tests produce actionable output.
