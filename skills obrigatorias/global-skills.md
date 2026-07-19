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
