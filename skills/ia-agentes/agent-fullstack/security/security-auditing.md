# Security Auditing - Auditoria de Segurança

## Visão Geral

Executar revisão de segurança em cada PR significativo:
- Análise de código
- Vulnerabilidades conhecidas
- Auth e Authorization
- Input validation
- Output encoding

## Fluxo de Auditoria

### 1. Pre-Scan

```bash
# Dependencies
npm audit
npm outdated

# Secrets
semgrep --config=p/secrets src/
```

### 2. Autenticação e Authorization

Verificar:
- [ ] Login requer credentials válidas
- [ ] Tokens expiram
- [ ] Refresh tokens funcionam
- [ ] Logout invalida tokens
- [ ] RBAC implementado
- [ ] Acesso verificado em cada endpoint

### 3. Input Validation

Verificar:
- [ ] Todos os inputs validados
- [ ] Tipos verificados
- [ ] Ranges verificados
- [ ] SQL injection-prevenido
- [ ] XSS-prevenido

### 4. Output Encoding

Verificar:
- [ ] HTML entities encoded
- [ ] URLs validadas
- [ ] JSON content-type correto

### 5. Error Handling

Verificar:
- [ ] Stack traces não expostos
- [ ] Log inappropriate details
- [ ] Generic error messages

## Common Findings

| Vulnerabilidade | Severidade | Fix |
|-----------------|------------|-----|
| SQL Injection | Critical | Parameterized queries |
| XSS | High | Sanitize output |
| Weak Auth | High | MFA + tokens |
| Secrets in code | Critical | .env only |
| No rate limiting | Medium | Add rate limit |

## Checklist Final

- [ ] `npm audit` sem critical/high
- [ ] Semgrep passing
- [ ] Auth verificado
- [ ] Input validation presente
- [ ] Output encoding presente
- [ ] Error handling seguro
- [ ] Rate limiting implementado

## Documentar Finding

Para cada vulnerability encontrada:

```markdown
## Finding: [Title]

### Severity
[Critical/High/Medium/Low]

### Location
`file:line`

### Description
[Descrição]

### Fix
[Código correto]

### Status
[Open/Fixed/Accepted]
```

## Regra

> Se passing security audit = pode merge. Se não = bloqua.