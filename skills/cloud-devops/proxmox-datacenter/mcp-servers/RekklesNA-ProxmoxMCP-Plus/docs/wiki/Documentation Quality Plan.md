# Documentation Quality Plan

This plan keeps the README, wiki, media, and release documentation useful as the MCP ecosystem changes.

## Documentation Goals

The docs should let a new operator:

1. Understand the project value in the first README screen.
2. Choose stdio, Streamable HTTP, or OpenAPI without guessing.
3. Install in a common MCP client in a few minutes.
4. Verify success with read-only tools before mutating Proxmox.
5. Understand the security model before exposing the server.
6. Find the right tool for a VM, LXC, snapshot, backup, ISO, command, or job workflow.
7. Debug common startup, auth, TLS, SSH, and health-check problems.

## README Standard

The README should stay optimized for GitHub scanning:

- one-sentence positioning statement
- badges for package, release, CI, container, and license
- architecture image near the top
- three quick-start paths: MCP stdio, MCP Streamable HTTP, OpenAPI
- one-click install buttons where supported
- short demo section with GIF and MP4 link
- tool-selection table for common workflows
- compact safety model
- clear links into the wiki for long-form details

Avoid moving full reference material into the README. Keep reference detail in wiki pages or generated docs.

## Wiki Standard

The wiki should be task-oriented:

| Page | Purpose |
| --- | --- |
| `Home` | routing page and five-minute path |
| `Client Setup` | client-specific install and verification |
| `Operator Guide` | runtime modes, config, deployment, health, logs |
| `Tool Selection Guide` | goal-to-tool workflow guidance |
| `Security Guide` | auth, TLS, command policy, approval, exposure controls |
| `Container Command Execution` | SSH-backed LXC command setup |
| `API & Tool Reference` | exact tools, inputs, prerequisites, failures |
| `Troubleshooting` | symptom-driven fixes |
| `Developer Guide` | local dev, tests, release workflow |
| `Release & Upgrade Notes` | compatibility and upgrade impact |

## Media Plan

Keep existing assets:

- `docs/assets/logo-proxmoxmcp-plus.png`
- `docs/assets/logo-proxmoxmcp-plus-400.png`
- `docs/assets/proxmoxmcp-drawio-hero-main-refresh.svg`
- `docs/assets/proxmoxmcp-demo.gif`
- `docs/assets/proxmoxmcp-demo.mp4`

Recommended new assets when real screenshots or recordings are available:

| Asset | Purpose |
| --- | --- |
| `docs/assets/client-connected-vscode.png` | prove the MCP server is visible in a mainstream IDE |
| `docs/assets/client-connected-cursor.png` | show client install success for Cursor users |
| `docs/assets/job-lifecycle.png` | explain natural language request -> MCP tool -> Proxmox `UPID` -> `job_id` |
| `docs/assets/security-flow.png` | show Proxmox token, OpenAPI bearer auth, TLS, command policy, and Host/Origin checks |
| YouTube or release-asset demo video | 60-90 second live workflow from install to read-only verification to one controlled mutation |

Do not add placeholder screenshots. Only publish assets captured from a working client or lab.

## Docs Site Plan

The repository can continue publishing `docs/wiki/` to GitHub Wiki. A future docs site should use the repository as the source of truth and publish to GitHub Pages.

Recommended path:

1. Add a lightweight static docs generator such as MkDocs Material.
2. Treat `docs/wiki/` as the initial content source.
3. Publish on tags and on `main`.
4. Generate `llms.txt` and `llms-full.txt` during the docs build.
5. Keep GitHub Wiki pages as a mirror for users who prefer the GitHub UI.

## LLM Documentation Entry Points

Maintain a small `docs/llms.txt` index for AI clients. It should link to:

- README
- Client Setup
- Operator Guide
- Tool Selection Guide
- Security Guide
- API & Tool Reference
- Troubleshooting
- Release & Upgrade Notes

If a full docs export is added later, keep it generated rather than hand-maintained.

## Automation Checklist

Add or keep checks that prevent documentation drift:

- markdown formatting check for README and docs
- link check for relative links
- JSON validation for config examples and MCP client snippets where possible
- manifest/runtime parity test for tool registration
- generated API/tool reference from runtime tool metadata or `manifest.json`
- asset existence check for README images and video links
- release checklist entry requiring README/wiki updates for user-facing changes

## Release Documentation Checklist

For each release that changes behavior:

1. Update `README.md` only if the first-run path, capability list, safety model, or install path changed.
2. Update `docs/wiki/API & Tool Reference.md` for tool names, inputs, prerequisites, and failure modes.
3. Update `docs/wiki/Operator Guide.md` for config, runtime, Docker, health, or logging changes.
4. Update `docs/wiki/Security Guide.md` for auth, TLS, command policy, or exposure changes.
5. Update `docs/wiki/Release & Upgrade Notes.md` with upgrade and rollback guidance.
6. Update `server.json` and `manifest.json` if package metadata or environment variables changed.
7. Run the docs validation checklist before publishing.

## Related Pages

- [Home](Home)
- [Client Setup](Client-Setup)
- [Tool Selection Guide](Tool-Selection-Guide)
- [Developer Guide](Developer-Guide)
