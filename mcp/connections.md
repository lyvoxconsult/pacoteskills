# Conexoes e autenticacao

Inventario saneado em `2026-08-28`.

## Remotos com autenticacao/configuracao

| Nome | Modo | Segredo requerido | Observacoes |
|---|---|---|---|
| `composio` | `http_headers` | API key | nao versionar header real |
| `context7` | `http_headers` | API key | nao versionar chave real |
| `supabase` | `url` parametrizada | project ref | manter read-only quando possivel |
| `vercel` | remoto | sessao/login do Codex | sem segredo no repo |
| `figma` | remoto | sessao/login do Codex | sem segredo no repo |
| `stitch` | `http_headers` | API key | nao versionar chave real |
| `openaiDeveloperDocs` | remoto | nenhuma chave local explicita nesta captura | oficial |

## Locais com configuracao relevante

| Nome | Detalhe | Portabilidade |
|---|---|---|
| `filesystem` | roots locais configurados | adaptar roots por maquina |
| `gsap` | script local em `.codex/mcp/gsap` | replicar script ou reinstalar |
| `chrome-devtools` | depende de `npx` | requer Node.js |
| `playwright` | depende de `npx` | requer Node.js e browsers |
| `shadcn` | depende de `npx` | requer Node.js |
| `chakra-ui` | depende de `npx` | requer Node.js |
| `node_repl` | aponta para runtime local do Codex | nao reutilizar path bruto entre maquinas |

## Approvals observados

- `playwright.browser_fill_form` -> `approve`
- `playwright.browser_click` -> `approve`
- `playwright.browser_resize` -> `approve`
- `playwright.browser_evaluate` -> `approve`
- `playwright.browser_navigate` -> `approve`
- `playwright.browser_run_code_unsafe` -> `approve`
- `supabase.execute_sql` -> `approve`
- `apps.asdk_app_69d3e5ee6a708191baa733f7b8931995.tools.supabase_apply_migration` -> `approve`

## Filesystem roots da captura Windows

Referencia apenas. Nao copiar literalmente para outras maquinas.

- `<workspace-root>`
- `<references-root>/claude-cookbooks-main/claude-cookbooks-main`
- `<lyvox-core-root>`
