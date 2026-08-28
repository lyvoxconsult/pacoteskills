# MCP Servers

Captura saneada do ambiente local em `2026-08-28`.

## Ativos

| Nome | Tipo | Inicializacao | Observacoes |
|---|---|---|---|
| `openaiDeveloperDocs` | remoto | `url` | documentacao OpenAI |
| `composio` | remoto | `url` | requer chave via header |
| `context7` | remoto | `url` | requer chave via header |
| `gsap` | local | `node <mcp-root>/gsap/start-gsap-mcp.mjs` | path local deve ser adaptado |
| `chrome-devtools` | local | `npx chrome-devtools-mcp@latest` | integra Chrome DevTools |
| `playwright` | local | `npx @playwright/mcp@latest` | varias tools em modo approve |
| `shadcn` | local | `npx shadcn@latest mcp` | UI/shadcn |
| `chakra-ui` | local | `npx @chakra-ui/react-mcp` | UI/Chakra |
| `filesystem` | local | `npx @modelcontextprotocol/server-filesystem` | requer roots explicitados |
| `supabase` | remoto | `url` | projeto em read-only |
| `vercel` | remoto | `url` | deploy/docs Vercel |
| `figma` | remoto | `url` | design/Figma |
| `stitch` | remoto | `url` | requer chave via header |
| `node_repl` | local runtime | binario local | acoplado ao runtime local do Codex |

## Desabilitados

| Nome | Tipo | Observacoes |
|---|---|---|
| `github` | remoto | configurado como disabled no ambiente atual |
| `penpot` | remoto/local | apontado para `localhost`, desabilitado |
| `21st-magic` | local via `npx` | desabilitado; depende de `API_KEY` |

## Regras de portabilidade

- substituir paths locais por equivalentes da maquina destino
- nao copiar binarios efemeros do runtime local
- para macOS, preferir comandos POSIX e paths sob `$HOME`
