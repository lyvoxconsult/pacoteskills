# ADR Template - Architectural Decision Record

```markdown
---
title: [Título da Decisão]
status: proposed | accepted | deprecated | superseded
date: {{date:YYYY-MM-DD}}
author: [Nome]
pr: [Link PR se aplicável]
tags: [architecture, backend, frontend, etc]
---

# ADR: {{title}}

## Status
{{status}} - {{date}}

## Contexto
[Descreva o problema ou contexto que motivou esta decisão]

## Decisão
[Descreva a decisão tomada]

## Alternativas Consideredas

### Opção 1: [Nome]
- Prós: [lista]
- Contras: [lista]

### Opção 2: [Nome]
- Prós: [lista]
- Contras: [lista]

## Impacto
- Positivo: [o que melhora]
- Negativo: [o que pode impactar]

## Backward Compatibility
[ ] Breaking change - Requer migração
[ ] Backward compatible

## Implementação
[Notas sobre como implementar]

## Related
- [Links para notas relacionadas]
- [Links para issues/PRs]
```

## Exemplo Preenchido

```markdown
---
title: Usar Zustand para Estado Global
status: accepted
date: 2026-04-17
author: Pedro
pr: https://github.com/user/repo/pull/45
tags: [architecture, frontend, state]
---

# ADR: Usar Zustand para Estado Global

## Status
accepted - 2026-04-17

## Contexto
Precisamos de gerenciamento de estado global para:
- Dados do Supabase espelhados localmente
- Estado de UI (sidebar, modals)
- Filtros e ordenação

## Decisão
Usar **Zustand 5** com slices organizados por feature.

## Alternativas Consideredas

### Zustand (escolhido)
- Prós: Simples, TypeScript, middleware
- Contras: Learning curve pequena

### Redux Toolkit
- Prós: Mature, DevTools
- Contras: Verbose

### Context API
- Prós: built-in
- Contras: Não recomendado para estado muito mutável

## Impacto
- Positivo: Estado centralizado, acesso simples
- Negativo: Nenhum significativo

## Backward Compatibility
[ x ] Backward compatible

## Implementação
1. Criar store/useAppStore.ts
2. Criar slices por feature
3. Migrar estado gradualmente

## Related
- PROJECT_MAP.md
- Feature: Auth Integration
```

## Metadata (Dataview)

```yaml
tags: [adr]
adr:: this.status
```