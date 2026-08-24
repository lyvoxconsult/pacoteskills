# 💡 Global Skills — Análise de Contexto e Engenharia de Prompts

Esta skill define as metodologias comportamentais, operacionais e de engenharia de prompts obrigatórias para os agentes.

---

## Skill global obrigatória: Find Skills

- **Objetivo:** Em todo pedido, descobrir quais skills locais ou externas atendem melhor ao domínio solicitado, somando-as ao pack obrigatório.
- **Regra:** Primeiro carregar as skills obrigatórias; depois consultar o catálogo local em `${HOME}/.codex/skills` e `${HOME}/.agents/skills`; só usar `npx skills find <consulta>` ou leaderboard externo quando não houver cobertura local adequada ou quando o usuário pedir extensão de capacidades.
- **Limite:** Não instalar automaticamente por resultado de busca. Antes de recomendar ou instalar, verificar reputação da fonte, installs/stars quando disponíveis e revisar `SKILL.md` ou fonte equivalente.
- **Fonte instalada:** `vercel-labs/skills`, skill `find-skills`, instalada em 2026-08-24.

---

## Ferramenta global condicional prioritária: Graphify

- **Objetivo:** Antes de investigação arquitetural, exploração de repositório não trivial, mudanças transversais ou análise multi-arquivo, mapear a base com `graphify` e consultar o grafo antes de varrer arquivos em massa.
- **Regra:** `graphify` não é “sempre”; é a primeira escolha obrigatória quando a tarefa depende de entendimento estrutural real.
- **Limite:** Não usar para perguntas rápidas ou alteração isolada e evidente.
- **Fonte instalada:** `Graphify-Labs/graphify`, versão `0.9.42`.

---

## Skills obrigatórias condicionais por domínio

- `project-skill-audit`: setup/auditoria de skills e padrões recorrentes por projeto.
- `frontend-skill`: UI, frontend, React/Next/Tailwind/shadcn, formulários, acessibilidade e responsividade.
- `backend-skill`: APIs, serviços, persistência, auth/autorização, migrations e integrações backend.
- `devops-skill`: Docker, CI/CD, deploy, build, runtime, env vars, Vercel, infra e produção.
- `playwright`: validação real em navegador, UI flows, screenshots, responsividade, login, formulário e E2E funcional.
- `postgres-best-practices`: Postgres, Supabase, SQL, RLS, índices, schema e performance de banco.
- `react-best-practices`: React/Next.js, data fetching, bundle, renderização, waterfalls, componentes e performance.
- `api-security-testing`: segurança REST/GraphQL, auth, autorização, rate limit, input validation, CORS e erros.
- `skill-scanner`: antes de instalar/adotar/recomendar skill externa ou desconhecida.

---

## 🔍 Skill 1: Análise de Contexto Sistêmico

- **Objetivo:** Garantir que o agente compreenda todo o ecossistema antes de tocar em qualquer linha de código.
- **Roteiro Operacional:**
  1. **Varredura Preventiva:** Liste a pasta raiz do projeto ativo e leia arquivos como `package.json`, `pnpm-lock.yaml`, `tsconfig.json` ou `requirements.txt` para entender dependências e versões.
  2. **Consulta a Notas:** Leia o arquivo de visão geral correspondente no Obsidian (`10 - Projetos/NomeDoProjeto/00 - Visão Geral.md`).
  3. **Identificação de Riscos:** Mapeie possíveis efeitos colaterais em áreas e arquivos importadores.
  4. **Proposta de Plano:** Elabore um plano de execução claro em `/implementation_plan.md` detalhando as fases.

---

## 🧠 Skill 2: Engenharia de Prompts e Delegação

- **Objetivo:** Otimizar prompts de tarefas e orquestrar subagentes especialistas com eficiência máxima de tokens.
- **Roteiro Operacional:**
  1. **Contexto Limpo:** Ao delegar tarefas para subagentes, envie apenas os trechos de arquivos e documentações cruciais. Evite enviar códigos inteiros irrelevantes para economizar contexto.
  2. **Critérios Explícitos:** Insira instruções diretas de aceitação (ex: "Visual Premium", "Tipagem Zod" ou "RLS ativo").
  3. **Validação Técnica:** Ordene ao subagente que teste e valide a compilação local de forma simulada ou executando os lints correspondentes antes de retornar o resultado.
  4. **Integração de Logs:** Integre as entregas parciais mantendo o histórico de fases em `task.md`.
