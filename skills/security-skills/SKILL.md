# 🛡️ Security Skills — Auditoria e Proteção de Ambiente

Esta skill orienta a conduzir auditorias de segurança proativas e preventivas em todo o ciclo de desenvolvimento, mantendo o ambiente de trabalho e as aplicações comerciais blindados.

---

## 🚫 1. Varredura e Proteção contra Vazamento de Segredos

- **Auditoria Pré-Commit:** Antes de realizar qualquer commit, execute o script de verificação de segredos (`scripts/check-secrets.ps1` no Windows ou `scripts/check-secrets.sh` no Linux).
- **Detecção de Assinaturas Suspeitas:** O script varre recursivamente por chaves privadas, strings de conexão explícitas e tokens de API conhecidos.
- **Remediação Imediata:** Caso uma credencial real seja encontrada exposta, remova-a imediatamente, transfira o valor para um arquivo `.env` local listado no `.gitignore` e utilize placeholders no arquivo original.

---

## 🏗️ 2. Boas Práticas contra Ameaças Clássicas (OWASP Top 10)

1. **Prevenção de Injeção SQL:**
   - Nunca concatene strings cruas de input de usuário final em queries de banco de dados.
   - Sempre utilize queries parametrizadas (Prepared Statements) ou ORMs consolidados que realizem a sanitização automática.

2. **Prevenção contra Path Traversal:**
   - Ao lidar com uploads de arquivos locais, sanitize os nomes de arquivos para evitar que caracteres como `../` permitam ao usuário ler arquivos confidenciais do sistema operacional.

3. **Prevenção contra XSS e HTML Injections:**
   - Garanta que dados inseridos por usuários finais sejam devidamente escapados antes de renderizá-los em telas HTML para prevenir injeções de scripts maliciosos.

4. **Controle de Acessos Rígido:**
   - Valide tokens JWT em middlewares de backend e aplique políticas de RLS (*Row Level Security*) nas tabelas expostas em bancos Supabase.
