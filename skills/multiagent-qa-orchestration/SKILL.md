---
name: multiagent-qa-orchestration
description: Mandatory global execution protocol for decomposing user requests into specialist subagents or simulated role stages, with required context research, testing when technical changes occur, QA review, final validation, and Obsidian documentation. Use for every task; enforce multiple subagents whenever a request spans more than one subject, layer, module, technical area, or responsibility.
---

# Skill Global - Orquestracao Multiagente com QA Obrigatorio

## Objetivo

Garantir que toda tarefa seja executada com organizacao, divisao de responsabilidades, pesquisa de contexto, testes proporcionais, QA obrigatorio e validacao final.

## Regra principal

Sempre que uma tarefa envolver mais de um assunto, camada, modulo ou responsabilidade, decompor a execucao em subagentes especializados.

Mesmo em tarefas simples, executar QA/revisao antes da entrega final.

Se o ambiente nao suportar subagentes nativos, simular subagentes como etapas independentes e nomeadas: orquestracao, pesquisa/contexto, execucao tecnica, testes, QA, validacao final e documentacao.

## Criterios para criar multiplos subagentes

Criar multiplos subagentes quando a tarefa combinar qualquer item abaixo:

- Front-end
- Back-end
- Banco de dados
- Supabase
- Autenticacao
- RBAC
- RLS
- API
- Integracao externa
- UI/UX
- Performance
- Seguranca
- Documentacao
- Infraestrutura
- Deploy
- Testes
- Refatoracao
- Correcao de bug
- Migracao
- Organizacao de arquivos
- Obsidian
- Regras de negocio

## Agentes obrigatorios

### Orquestrador Principal

Entender solicitacao, mapear escopo, identificar assuntos/camadas, decidir subagentes, coordenar execucao, consolidar entrega e garantir que nenhum requisito foi esquecido.

### Pesquisa e Contexto

Obrigatorio quando a tarefa depender de arquivos existentes, documentacao, historico, regras de negocio, integracoes, Obsidian ou internet. Buscar contexto antes de implementar e bloquear achismo quando houver fonte consultavel.

### Subagentes Tecnicos

Criar por area conforme escopo: front-end, back-end, banco/Supabase, autenticacao/RBAC/RLS, UI/UX, integracoes/API, infra/deploy, documentacao, seguranca, performance ou outra camada necessaria. Cada subagente atua apenas na propria responsabilidade.

### QA Obrigatorio

Sempre obrigatorio. Revisar solicitacao original, comparar antes/depois, checar pendencias, riscos de regressao, coerencia entre camadas e pontos esquecidos. Nao finalizar com falha critica aberta.

### Testes

Obrigatorio quando houver alteracao em codigo, banco, tela, API, fluxo, autenticacao, regra de negocio, integracao ou documentacao operacional sensivel. Rodar testes existentes quando possivel, criar testes quando fizer sentido, validar build/lint/typecheck/execucao local conforme risco, e registrar o que nao foi possivel testar.

### Validacao Final

Pode ser combinado com QA em tarefa pequena. Em tarefa media/grande, manter etapa separada para confirmar requisitos, documentacao, escopo, ausencia de remocao indevida, ausencia de duplicacao desnecessaria e prontidao para revisao/uso.

## Fluxo obrigatorio de execucao

1. Ler e entender a solicitacao.
2. Mapear assuntos, camadas e responsabilidades envolvidos.
3. Consultar documentacao, codigo, Obsidian e contexto existente quando aplicavel.
4. Criar subagentes necessarios ou simular papeis separados quando nao houver suporte nativo.
5. Planejar execucao curta e verificavel.
6. Implementar por etapas, preservando comportamento existente.
7. Rodar testes e validacoes proporcionais ao risco.
8. Executar QA.
9. Corrigir pendencias encontradas.
10. Atualizar documentacao quando a acao for relevante ou persistente.
11. Fazer checklist final.
12. Entregar resumo claro com feito, arquivos alterados, testes executados, pendencias, riscos e proximos passos recomendados.

## Checklist obrigatorio antes de finalizar

- [ ] A solicitacao original foi completamente atendida?
- [ ] Todos os assuntos envolvidos tiveram subagente ou etapa dedicada?
- [ ] O QA revisou a entrega?
- [ ] Os testes possiveis foram executados?
- [ ] O projeto continua funcionando?
- [ ] Nao houve alteracao fora de escopo?
- [ ] Nenhum arquivo importante foi removido indevidamente?
- [ ] A documentacao foi atualizada quando aplicavel?
- [ ] O Obsidian foi atualizado sem duplicacao quando aplicavel?
- [ ] Pendencias e riscos foram registrados?
- [ ] A entrega final esta clara para o usuario?
