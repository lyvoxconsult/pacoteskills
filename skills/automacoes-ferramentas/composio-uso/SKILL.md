---
name: composio-uso
description: "Operate connected Composio toolkits via the Composio CLI (search, execute, link, proxy, run) with --account selection. Use when the user wants to act on GitHub, Gmail, Vercel, Figma, Jira, Confluence, Supabase, Firecrawl, Google Calendar, Google Tasks, Google Analytics, or Microsoft Teams through an existing Composio connection."
risk: critical
source: local
date_added: "2026-10-13"
---

# Composio Uso (CLI)

Guia operacional para usar toolkits já conectados via Composio CLI. Não contém credenciais. Seleção de conta sempre por `--account <alias|word_id|id>`.

## Pré-requisitos

```bash
composio whoami
composio connections list
```

Se `whoami` falhar: `composio login`. Se um `execute` disser que o toolkit não está conectado: `composio link <toolkit>` e repita.

## Fluxo padrão

1. Slug conhecido → `composio execute <SLUG> -d '{...}' [--account <alias>]`.
2. Dúvida nos argumentos → `composio execute <SLUG> --get-schema` ou `--dry-run` antes de executar.
3. Slug desconhecido → `composio search "<tarefa>" --toolkits <toolkit>` (agrupar buscas relacionadas num único comando).
4. Chamadas independentes → `composio execute --parallel <SLUG> -d '{...}' <SLUG2> -d '{...}'`.
5. Lógica multi-etapas (loops, agregação) → `composio run '<js/ts com execute()>'`.

## Descoberta e inspeção

```bash
composio search "list github repositories" --toolkits github
composio execute GITHUB_LIST_REPOSITORIES_FOR_THE_AUTHENTICATED_USER --get-schema
composio execute GITHUB_CREATE_AN_ISSUE --dry-run -d '{ "owner": "<owner>", "repo": "<repo>", "title": "<titulo>" }'
```

## Contas (sem segredos)

```bash
composio connections list --toolkit github
composio link github --list
composio link gmail --alias <alias>   # só para conta adicional do mesmo toolkit
composio execute GMAIL_GET_PROFILE -d '{}' --account <alias>
```

Nunca gravar `connected_account_id`, `word_id` alheio, e-mails ou tokens em arquivos versionados. Resolver o seletor em tempo de execução e passar via `--account`.

## Toolkits verificados (slugs primários)

| Toolkit | Slug de leitura verificado | Exemplo seguro |
|---|---|---|
| github | `GITHUB_GET_THE_AUTHENTICATED_USER` | `composio execute GITHUB_GET_THE_AUTHENTICATED_USER -d '{}'` |
| vercel | `VERCEL_LIST_PROJECTS` | `composio execute VERCEL_LIST_PROJECTS -d '{"limit": 5}'` |
| gmail | `GMAIL_GET_PROFILE` | `composio execute GMAIL_GET_PROFILE -d '{}' --account <alias>` |
| figma | `FIGMA_GET_PROJECTS_IN_A_TEAM` | `composio execute FIGMA_GET_PROJECTS_IN_A_TEAM --get-schema` |
| jira | `JIRA_SEARCH_ISSUES` | `composio execute JIRA_SEARCH_ISSUES --get-schema` |
| confluence | `CONFLUENCE_GET_SPACES` | `composio execute CONFLUENCE_GET_SPACES -d '{}'` |
| supabase | `SUPABASE_LIST_ALL_PROJECTS` | `composio execute SUPABASE_LIST_ALL_PROJECTS -d '{}'` |
| firecrawl | `FIRECRAWL_SCRAPE` | `composio execute FIRECRAWL_SCRAPE --get-schema` |
| googlecalendar | `GOOGLECALENDAR_EVENTS_LIST` | `composio execute GOOGLECALENDAR_EVENTS_LIST --get-schema` |
| googletasks | `GOOGLETASKS_LIST_ALL_TASKS` | `composio execute GOOGLETASKS_LIST_ALL_TASKS --get-schema` |
| google_analytics | `GOOGLE_ANALYTICS_LIST_ACCOUNT_SUMMARIES` | `composio execute GOOGLE_ANALYTICS_LIST_ACCOUNT_SUMMARIES --get-schema` |
| microsoft_teams | `MICROSOFT_TEAMS_LIST_USER_JOINED_TEAMS` | `composio execute MICROSOFT_TEAMS_LIST_USER_JOINED_TEAMS --get-schema` |

Gmail com várias contas: sempre `--account <alias>` (ex.: uma conta pessoal e outra operacional). Confirmar o perfil com `GMAIL_GET_PROFILE` antes de enviar em nome de alguém.

## Segurança

- Leitura primeiro (`GET`/`LIST`/`--dry-run`) antes de qualquer escrita.
- Escrita/destrutivo (enviar e-mail, merge, delete, update de proteção de branch) só com confirmação explícita do usuário.
- `type: sensitive/secret` (ex.: env vars da Vercel) não pode ser lido de volta após criação.
- `proxy` só quando não houver slug dedicado e for mais simples que descobrir um.

```bash
composio proxy https://api.github.com/user --toolkit github --method GET
```
