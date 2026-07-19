# SECURITY_SKILL

Skill especializada em segurança de aplicações, OWASP e DevSecOps.

## Repositórios de Referência

- **OWASP Top 10**: https://github.com/OWASP/Top10
- **DevSecOps Guide**: https://github.com/TaptuIT/DevSecOps-Guide
- **Trivy**: https://github.com/aquasecurity/trivy

## Capacidades

### 1. OWASP Top 10
- Identificar e mitigar vulnerabilidades do OWASP Top 10 (2021)
- A01: Broken Access Control
- A02: Cryptographic Failures
- A03: Injection
- A04: Insecure Design
- A05: Security Misconfiguration
- A06: Vulnerable and Outdated Components
- A07: Identification and Authentication Failures
- A08: Software and Data Integrity Failures
- A09: Security Logging and Monitoring Failures
- A10: Server-Side Request Forgery

### 2. DevSecOps
- Integrar segurança no pipeline de CI/CD
- Implementar Security as Code
- Realizar扫描ões de vulnerabilidade automatizadas
- Configurar políticas de segurança em infraestrutura

### 3. Scanning e Auditoria
- Usar Trivy para scanning de vulnerabilidades em containers e código
- Realizar análise estática de código (SAST)
- Realizar análise dinâmica de aplicação (DAST)
- Executar análise de dependências (SCA)

### 4. Segurança em Desenvolvimento
- Validar entrada de dados (input validation)
- Prevenir injection attacks (SQL, XSS, Command)
- Implementar autenticação e autorização corretas
- Criptografar dados sensíveis em repouso e em trânsito
- Gerenciar segredos de forma segura

## Boas Práticas de Segurança

- **Defense in Depth**: Múltiplas camadas de segurança
- **Least Privilege**: Mínimo privilégio necessário
- **Fail Secure**: Falhar de forma segura
- **Zero Trust**: Nunca confiar, sempre verificar
- **Secure by Default**: Seguro por padrão

## Ferramentas de Segurança

- **Trivy**: Scanner de vulnerabilidades para containers, código e infraestrutura
- **OWASP ZAP**: Proxy de teste de segurança
- **Bandit**: Scanner de segurança para Python
- **npm audit**: Auditoria de dependências npm

## Quando Usar

Use esta skill quando:
- Precisa revisar código em busca de vulnerabilidades
- Precisa configurar pipelines seguros de CI/CD
- Precisa implementar políticas de segurança
- Precisa fazer scanning de vulnerabilidades
- Precisa implementar autenticação e autorização seguras
- Precisa configurar segurança em infraestrutura