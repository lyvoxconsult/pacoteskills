# Runbook Template - Procedimentos Operacionais

```markdown
---
title: [Nome do Runbook]
type: troubleshooting | procedure | runbook
severity: P1 | P2 | P3 | P4
last_updated: {{date:YYYY-MM-DD}}
tags: [ops, runbook, [serviço]]
---

# Runbook: [Nome do Serviço/Procedimento]

## Tipo
{{type}}

## Severity Target
{{severity}}

## Overview
[Breve descrição do que este runbook cobre]

---

## Troubleshooting

### Sintoma 1: [Descrição]
**Severity**: [P1-P4]

**Passos de Diagnóstico**:
1. [Passo]
2. [Passo]

**Solução**:
1. [Ação]
2. [Ação]

**Rollback**:
```bash
[Comando de rollback]
```

---

## Procedimentos

### Procedimento 1: [Nome]
**Pré-requisitos**:
- [ ] Requisito 1
- [ ] Requisito 2

**Passos**:
1. [Passo]
2. [Passo]

**Validação**:
[Como verificar que funcionou]

---

## Comandos Úteis

```bash
# Verificar status
curl -s http://localhost:3000/health

# Logs
kubectl logs -f deployment/app -n production

# Metrics
curl http://localhost:9090/metrics
```

## Contacts

| Role | Name | Contact |
|------|------|---------|
| On-call | [Nome] | [Contato] |
| Dev Lead | [Nome] | [Contato] |

## Links

- [Dashboard]
- [Alerts]
- [Documentation]
```

## Exemplo

```markdown
---
title: CaçambaGo Production Troubleshooting
type: troubleshooting
severity: P1
last_updated: 2026-04-17
tags: [ops, runbook, cacambago]
---

# Runbook: CaçambaGo Production

## Tipo
troubleshooting

## Severity Target
P1

## Overview
Procedimentos para troubleshooting de issues em produção.

---

## Troubleshooting

### Sintoma: erro de autenticação
**Severity**: P1

**Passos de Diagnóstico**:
1. Verificar Supabase Auth status
2. Verificar variáveis de ambiente
3. Verificar tokens nos logs

**Solução**:
1. Reiniciar edge function
2. Invalidar cache de sessão
3. Escalonar se necessário

---

## Comandos Úteis

```bash
# Verificar Supabase
supabase projects list

# Edge Functions
supabase functions serve emitir-ctr --no-local
```
```