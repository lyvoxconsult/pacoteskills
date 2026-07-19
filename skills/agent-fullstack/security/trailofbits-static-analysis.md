# Trail of Bits - Static Analysis

## Visão Geral

Análise estática com CodeQL, Semgrep e SARIF para segurança.

## Referência

- Repositório: https://github.com/trailofbits/superpowers
- Skill: `trailofbits/static-analysis`

## Instalação

```bash
# Semgrep
npm install -D semgrep

# CodeQL (via gh)
gh codeql install
```

##扫描

### Semgrep

```bash
# Scan local
semgrep --config=auto src/

# Scan com regras customizadas
semgrep --config=semgrep.rules.yaml src/

# Mode específico
semgrep --config p/javascript src/
```

### CodeQL

```bash
# Criar database
gh codeql database create codeql-db --language=typescript

# Analisar
gh codeql database analyze codeql-db --format=sarif-latest > results.sarif
```

## Regras de Segurança

### OWASP Top 10

| # | Vulnerabilidade | Regra Semgrep |
|---|---------------|--------------|
| A01 | Broken Access Control | `generic-error-disclosure` |
| A02 | Cryptographic Failures | `hardcoded-credentials` |
| A03 | Injection | `sql-injection` |
| A04 | Insecure Design | `weak-crypto` |
| A05 | Security Misconfiguration | `exec-literals` |
| A06 | Vulnerable Components | `outdated-deps` |
| A07 | Auth Failures | `sqli` |
| A08 | Data Failures | `path-traversal` |
| A09 | Logging Failures | `log-injection` |
| A10 | SSRF | `ssrf` |

## Vulnerabilidades Comuns

### secrets/Hardcoded

```typescript
// BAD
const apiKey = 'sk-1234567890abcdef'

// GOOD
const apiKey = process.env.API_KEY
```

### SQL Injection

```typescript
// BAD
db.query(`SELECT * FROM users WHERE id = ${userId}`)

// GOOD
db.query('SELECT * FROM users WHERE id = $1', [userId])
```

### XSS

```typescript
// BAD
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// GOOD (sanitize)
import DOMPurify from 'dompurify'
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />
```

## Checklist de Segurança

- [ ] Semgrep scan passing
- [ ] Nenhum secret em código
- [ ] Input validation presente
- [ ] Parameterized queries usadas
- [ ] Auth verificado em endpoints
- [ ] Rate limiting implementado
- [ ] Logging adequado

## Regras de Ouro

> Audit in every PR. Se não pode escanear, não pode fazer merge.