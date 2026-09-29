# Wiki Seed Pages

This directory contains the markdown files intended for the GitHub Wiki and the in-repo documentation hub.

## Documentation Strategy

- `README.md` in the repository root is the conversion-focused homepage
- `docs/wiki/` holds the longer client setup, operator, integration, security, workflow, and reference material
- page names should stay stable so README links and published wiki URLs do not break

## Included Pages

- `Home.md`
- `Client Setup.md`
- `Operator Guide.md`
- `Tool Selection Guide.md`
- `Developer Guide.md`
- `Security Guide.md`
- `Container Command Execution.md`
- `Integrations Guide.md`
- `API & Tool Reference.md`
- `Troubleshooting.md`
- `Release & Upgrade Notes.md`
- `Documentation Quality Plan.md`
- `_Sidebar.md`

## Publishing To GitHub Wiki

1. Enable the repository Wiki in GitHub settings.
2. Clone the wiki repository:

```bash
git clone https://github.com/RekklesNA/ProxmoxMCP-Plus.wiki.git
```

3. Copy the files from `docs/wiki/` into the root of the cloned wiki repository.
4. Commit and push:

```bash
git add .
git commit -m "Update wiki content"
git push
```

## Maintenance Notes

- Keep titles stable so wiki URLs remain stable
- Update the root README when adding, removing, or renaming wiki pages
- Keep the homepage short and move operational detail into wiki pages
- Keep client install examples in `Client Setup.md`
- Keep goal-to-tool workflow guidance in `Tool Selection Guide.md`
- Keep documentation improvement work in `Documentation Quality Plan.md`
- Do not add placeholders for features that do not exist in the codebase
