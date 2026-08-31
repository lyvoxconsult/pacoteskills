# 💡 Global Skills — Análise de Contexto e Engenharia de Prompts

Esta skill define as metodologias comportamentais, operacionais e de engenharia de prompts obrigatórias para os agentes.

---

## Skill global obrigatória: Ponytail

- **Objetivo:** Aplicar em toda solicitação técnica a menor solução correta, seguindo YAGNI, reuso do código existente, biblioteca padrão e recursos nativos antes de abstrações ou dependências novas.
- **Regra:** `ponytail` substitui `caveman` como baseline obrigatório. Nunca reduzir validação de entrada, prevenção de perda de dados, segurança, acessibilidade ou requisito explícito.
- **Fonte e versão instalada:** `DietrichGebert/ponytail`, commit `2ed6c52c9d7e5e56942508591085fd45dea277d3`.

---

## Ferramentas globais condicionais

| Ferramenta | Gatilho obrigatório | Limite operacional |
|---|---|---|
| `graphify` | Primeira escolha obrigatória para arquitetura, investigação multi-arquivo, repositório não trivial e mudanças transversais | Gere ou atualize `graphify-out/` antes de varredura ampla; código é processado localmente e conteúdo sem código só usa backend externo se configurado. |
| `headroom` | Contexto longo, RAG, logs/saídas de ferramentas volumosas ou múltiplos agentes | Executar `headroom doctor` antes do uso; não executar `wrap`, `deploy` ou proxy persistente sem pedido explícito. |
| `outlines` | Funcionalidade de produto com geração LLM estruturada | Dependência por projeto; preferir schema na geração a parsing pós-resposta. |
| `codeburn` | Custo, orçamento, desperdício de tokens ou retrospectiva não trivial | Apenas leitura por padrão; ações, sincronização e compartilhamento exigem pedido explícito. |

Fontes instaladas/revisadas: `headroomlabs-ai/headroom` (0.35.0), `Graphify-Labs/graphify` (0.9.42), `dottxt-ai/outlines` e `getagentseal/codeburn` (0.9.20).

Regra operacional: quando houver dúvida entre começar por leitura manual ampla ou por mapeamento estrutural, começar por `graphify`.

---

## Skill global obrigatória: Find Skills

- **Objetivo:** Em todo pedido, descobrir quais skills locais ou externas atendem melhor ao domínio solicitado, somando-as ao pack obrigatório.
- **Regra:** Primeiro carregar as skills obrigatórias; depois consultar o catálogo local em `${HOME}/.codex/skills` e `${HOME}/.agents/skills`; só usar `npx skills find <consulta>` ou leaderboard externo quando não houver cobertura local adequada ou quando o usuário pedir extensão de capacidades.
- **Limite:** Não instalar automaticamente por resultado de busca. Antes de recomendar ou instalar, verificar reputação da fonte, installs/stars quando disponíveis e revisar `SKILL.md` ou fonte equivalente.
- **Fonte instalada:** `vercel-labs/skills`, skill `find-skills`, instalada em 2026-08-24.

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
- `reference-first-ui`: antes de criar interfaces novas ou fazer redesenho visual sem referência explícita.

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
