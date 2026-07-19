# 💡 Global Skills — Análise de Contexto e Engenharia de Prompts

Esta skill define as metodologias comportamentais, operacionais e de engenharia de prompts obrigatórias para os agentes.

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

---

## Skill 3: Spec-Driven Development (SDD)

- **Objetivo:** Ativar a skill global `sdd` quando o trabalho envolver GitHub Spec-Kit, Spec-Driven Development, `/speckit`, `specify init`, especificacoes executaveis, fluxos greenfield/brownfield, reverse engineering de codebase, planejamento por requisitos ou gestao de features.
- **Roteiro Operacional:**
  1. **Classificacao:** Confirmar se a tarefa realmente pede SDD/Spec-Kit antes de ativar; nao usar em tarefa comum de codigo sem relacao com SDD.
  2. **Workflow:** Escolher greenfield ou brownfield, carregar `C:\Users\pedro\.agents\skills\sdd\SKILL.md` e seguir as referencias relevantes.
  3. **Artefatos:** Ler especificacoes, planos, tasks e checklists gerados antes de resumir decisoes.
  4. **Validacao:** Separar decisoes geradas por IA de validacao comprovada por codigo, testes e criterios de aceite.
  5. **Documentacao:** Manter rastreio em Obsidian quando a decisao ou workflow for persistente.
