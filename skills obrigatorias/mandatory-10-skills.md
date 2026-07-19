---
id: VCC-MANDATORY-001
title: "Pack Obrigatório de 10 Skills"
aliases:
  - "10 Skills Obrigatórias"
  - "Mandatory Skill Pack"
type: process
domain: ia
lifecycle: permanent
status: active
authority: canonical
owner: "vibecoderconfigall"
sensitivity: internal
confidence: high
effective_at: 2026-07-06
review_at: 2026-08-06
created_at: 2026-07-06
updated_at: 2026-07-06
tags:
  - mandatory
  - skills
  - baseline
---

# Pack Obrigatório de 10 Skills

> **Regra:** Todo agente ou IDE DEVE carregar este pack antes de qualquer trabalho. As 10 skills são o baseline universal.

> Estado observado em 2026-07-12: `lyvox-core-reader` está ausente e não deve ser simulada. `devpromptarchitect` é uma skill obrigatória adicional quando acionada pelas regras globais.

---

## As 10 Skills

| # | Skill | Propósito | Quando Usar |
|---|-------|-----------|-------------|
| 1 | **caveman** | Clareza, objetividade, economia de tokens | Sempre — baseline de comunicação |
| 2 | **lyvox-core-reader** | Leitura do knowledge base, MOCs, registries | Antes de consultar ou modificar o knowledge |
| 3 | **audit-context-building** | Entender contexto real antes de agir | Antes de tarefas significativas |
| 4 | **deep-research** | Pesquisa profunda externa | Quando conhecimento interno é insuficiente |
| 5 | **concise-planning** | Planejar antes de executar | Antes de tarefas com múltiplos passos |
| 6 | **subagent-driven-development** | Ativar subagentes especializados | Para tarefas complexas multi-domínio |
| 7 | **architecture-skill** | Decisões técnicas e estrutura | Quando afetar estrutura do sistema |
| 8 | **security-skill** | Segredos, dados sensíveis, permissões | Sempre que envolver dados ou auth |
| 9 | **multiagent-qa-orchestration** | QA final e cross-validation | Antes de finalizar entregas significativas |
| 10 | **documentation** | Changelog, docs, atualizações | Ao finalizar qualquer tarefa |

### Skill adicional por gatilho

| Skill | Propósito | Quando usar |
|---|---|---|
| **devpromptarchitect** | Transformar requisitos em prompt técnico executável | Quando mencionada, em arquitetura de prompt ou preparação de tarefa para agente |

---

## Regra de Uso

```
1º → Carregar Pack Obrigatório (este documento)
2º → Ativar skills contextuais conforme o tipo de tarefa
3º → Documentar skills utilizadas no resultado
```

### Skills Contextuais

Adicionar conforme o domínio:
- **Frontend:** frontend-skills, design-skills
- **Backend:** backend-skills, database-skills
- **DevOps:** devops-skills
- **QA:** qa-skills
- **Segurança:** security-skills (adicional ao pack)
- **Documentação:** documentation-skills

---

## Referências

- Lyvox Core: [[Pack Obrigatório de 10 Skills]]
- Mapeamento: [[Skills Obrigatórias por Tipo de Tarefa]]
- Regras: [[Regra Global de Uso de Skills]]
