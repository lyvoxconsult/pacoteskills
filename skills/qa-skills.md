# 🧪 QA & Testes Skills — Automatização e Qualidade de Código

Esta skill documenta as abordagens de qualidade recomendadas para garantir a estabilidade do sistema e prevenir regressões durante a evolução dos produtos comerciais.

---

## 🧪 Estratégia de Testes Automatizados

1. **Testes Unitários Rápidos (Vitest):**
   - Use frameworks leves e com execução extremamente veloz como **Vitest** para testar componentes puros, funções utilitárias e regras de negócios isoladas.
   - Aplique o ciclo de TDD (*Test-Driven Development*) quando for pertinente para acelerar a robustez e a legibilidade do código durante a implementação inicial.

2. **Testes de Integração e APIs:**
   - Teste fluxos inteiros de rotas de backend (ex: requisição de post, inserção no banco de testes e payload de retorno) garantindo que todas as validações de schemas (Zod/Pydantic) e lógicas de autenticação funcionem juntas sem atritos.

3. **Testes e2e de Navegadores (Playwright):**
   - Utilize Playwright para orquestrar scripts funcionais que simulam a navegação real do usuário final (login, cliques em botões, preenchimento de inputs e navegação de rotas protegidas).
   - Testes e2e reduzem significativamente erros visuais e bugs de fluxos cruciais em novos releases de frontend.

---

## 🔍 Regra de Validação Antes de Finalizar

- É expressamente proibido para qualquer IA simular verbalmente o sucesso de uma alteração sem executar as suites de testes do projeto correspondente.
- Garanta que todos os testes sejam passantes antes de commitar ou abrir Pull Requests na branch principal.
