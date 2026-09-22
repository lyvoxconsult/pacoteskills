---
name: frontend-skill
description: Use for frontend implementation and review with Next.js, React, Tailwind CSS, shadcn/ui, accessibility, responsive layout, client/server rendering, forms, state management, UX flows, browser verification, and production UI quality. Trigger for UI, routing, styling, component, or frontend data-flow changes.
---

# Frontend Skill

Use this skill to build usable product screens that fit the existing application.

Reference repositories:
- https://github.com/vercel/next.js
- https://github.com/tailwindlabs/tailwindcss
- https://github.com/shadcn-ui/ui

## Workflow

1. Inspect the current component structure, design system, route model, and styling conventions.
2. Build the actual workflow first; avoid marketing screens unless requested.
3. Keep state ownership clear: server data, URL state, local UI state, and persisted state should not be mixed casually.
4. Use existing UI primitives before introducing new component patterns.
5. Design responsive layouts with stable dimensions so controls do not shift or overlap.
6. Verify with browser checks for desktop and mobile when the change is visual or interactive.
7. Preserve accessibility: labels, focus states, keyboard paths, semantic elements, and contrast.

## Framework Guidance

- Next.js: respect App Router boundaries, avoid unnecessary client components, and keep data fetching close to the route or server component when possible.
- Tailwind CSS: use existing tokens and utility patterns; avoid one-off palettes that fight the product.
- shadcn/ui: compose primitives directly and keep variants consistent with the local design system.

## Review Checklist

- The first screen is usable for the target workflow.
- Text does not overflow or overlap at common viewport sizes.
- Loading, empty, error, and unauthorized states are handled.
- Forms validate input and preserve user work where appropriate.
- Visual changes are verified in a browser when feasible.
