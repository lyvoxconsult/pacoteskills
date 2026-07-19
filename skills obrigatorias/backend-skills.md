# ⚙️ Backend Skills — APIs Robustas e Resilientes

Esta skill descreve as diretrizes operacionais para construir backends resilientes, escaláveis, seguros e de fácil manutenção corporativa.

---

## 🏗️ Padrões de Design e Estruturação

1. **Separação de Responsabilidades (SoC):**
   - Mantenha controllers, services, middlewares e repositories devidamente isolados para facilitar testes unitários e manutenção.
   - APIs devem ser auto-explicativas, seguindo as diretrizes de nomenclatura RESTful ou de schemas do tRPC.

2. **Validação Estrita de Contratos de Dados:**
   - Toda rota de API que receber dados externos deve validar os payloads usando schemas fortes (como **Zod** para JavaScript/TypeScript ou **Pydantic** para Python).
   - Tipagem robusta e validação evitam inserções corrompidas no banco de dados e mitigam injeções de código malicioso.

3. **Tratamento Explícito de Erros:**
   - Evite `try/catch` vazios ou omissões de erros de sistema.
   - Retorne sempre status codes HTTP adequados (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `500 Internal Server Error`).
   - Forneça payloads de erro claros, legíveis e livres de dados internos confidenciais do servidor (como stack traces brutas).

---

## 🔐 Segurança e Autenticação

- **Verificação de Token:** Rotas protegidas devem validar tokens JWT de forma explícita na camada de middleware antes de processar lógica de banco.
- **Limitação de Taxa (Rate Limiting):** Aplique middlewares de rate limiting em endpoints críticos para prevenir ataques do tipo denial of service (DoS).
- **CORS Seguros:** Configure políticas de CORS de forma restritiva em produção, liberando acessos apenas para os domínios de homologação e produção autorizados da marca.
