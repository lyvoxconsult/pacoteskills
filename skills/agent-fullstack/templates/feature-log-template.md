# Feature Log Template - Acompanhamento de Features

```markdown
---
title: [Nome da Feature]
status: planning | in_progress | review | completed | blocked
priority: P0 | P1 | P2 | P3
started: {{date:YYYY-MM-DD}}
target_release: [versão]
tags: [feature, [módulo]]
---

# Feature: [Nome]

## Status
{{status}}

## Priority
{{priority}}

## Overview
[Descrição breve da feature]

## Escopo

### In Scope
- [ ] Item 1
- [ ] Item 2

### Out of Scope
- Item 1 (razão)

## Dependências
- [ ] Dependência 1
- [ ] Dependência 2

## Technical Notes

### Arquitetura
[Notas sobre implementação]

### API Changes
```
[schema de mudanças]
```

### Database Changes
```sql
[migration se aplicável]
```

## Progress

- [ ] planning - [data]
- [ ] in_progress - [data]
- [ ] review - [data]
- [ ] completed - [data]

## PR Links
- [PR #1](link)
- [PR #2](link)

## Blocker
[Se aplicável]

## Lessons Learned
[Notas após completar]

## Related
- [Notas relacionadas]
- [Tickets]
```

## Exemplo

```markdown
---
title: Login OAuth com Google
status: completed
priority: P0
started: 2026-04-15
target_release: v1.1.0
tags: [feature, auth, oauth]
---

# Feature: Login OAuth com Google

## Status
completed

## Priority
P0

## Overview
Adicionar login social via Google OAuth usando Supabase Auth.

## Escopo

### In Scope
- [ ] Login com Google
- [ ] Logout
- [ ] Session persistence

### Out of Scope
- GitHub OAuth (v1.2)

## Dependências
- [x] Supabase Auth configurado
- [x] Credenciais Google Cloud

## Technical Notes

### Arquitetura
Usar @supabase/ssr para gerenciar sessão.

### API Changes
- Novo hook: `useGoogleLogin()`
- Componente: `<OAuthButtons />`

## Progress

- [x] planning - 2026-04-15
- [x] in_progress - 2026-04-16
- [x] review - 2026-04-17
- [x] completed - 2026-04-17

## PR Links
- [PR #45](https://github.com/user/repo/pull/45)

## Lessons Learned
- Configurar redirect URLs no Google Console antes
- Testar em staging primeiro

## Related
- [[ADR:Authentication-Decision]]
- [[Auth Integration]]
```