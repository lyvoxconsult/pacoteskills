# MCP Servers

Captura saneada do ambiente local em `2026-08-28`.

## Conferencia local em 2026-10-15

Nomes observados na configuracao desta maquina, sem copiar URL, comando, header, token ou caminho local. A presenca na configuracao nao comprova conexao funcional:

| Nome | Estado configurado | Nota de catalogo |
|---|---|---|
| `node_repl` | configurado | runtime local; ja constava da captura anterior |
| `playwright` | configurado | automacao de navegador; ja constava |
| `sequential-thinking` | configurado | **novo no inventario**; conferir pacote e comandos na maquina de destino |
| `computer-use` | desabilitado | **novo no inventario**; nao presumir uso ativo |
| `stitch` | configurado | ja constava |
| `21st` | configurado | **novo no inventario**; nome de configuracao local, sem template de segredo |

Os demais nomes da captura de agosto abaixo nao foram confirmados na configuracao atual. Podem estar expostos por plugins ou conectores fora de `config.toml`; valide no host de destino antes de reproduzir. Nao replique entradas de autenticacao diretamente.

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
