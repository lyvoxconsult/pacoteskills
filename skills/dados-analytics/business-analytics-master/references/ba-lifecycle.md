# Ciclo completo de Business Analysis

Use este guia para estrategia, processos, produtos, mudancas e avaliacao de solucoes. As seis frentes se sobrepoem: escolha somente as tarefas que ajudam a decisao atual. Uma solicitacao pode comecar na avaliacao de uma solucao existente, sem passar por um projeto novo.

## 1. Planejar a analise e a colaboracao

Defina objetivo da analise, decisao, prazo, nivel de detalhe, fontes, restricoes, participantes e quem decide. Mapeie interesse, influencia, necessidade de informacao e possiveis conflitos dos stakeholders. Combine como requisitos, decisoes e mudancas serao registrados, revisados e aprovados. Verifique se o custo da analise e proporcional ao risco da decisao.

## 2. Elicitar e confirmar necessidades

Escolha entrevista, observacao do trabalho real, oficina, analise documental, dados operacionais ou prototipo conforme a lacuna. Descubra a tarefa que a pessoa tenta concluir, o contexto, os contornos de sucesso, a solucao manual atual e as excecoes. Triangule relatos com artefatos e outras pessoas. Registre divergencias e confirme a sintese com os envolvidos; nao trate uma opiniao isolada como consenso.

Para calls e transcricoes, use [discovery-from-call.md](discovery-from-call.md). Uma gravacao e evidencia de fala, nao de aprovacao de arquitetura.

## 3. Analisar estrategia, estado atual e futuro

Descreva problema, causa hipotetica, capacidade atual, fluxo, atores, sistemas, dados, custos, controles, gargalos e riscos. Diferencie observacao de causa demonstrada. Defina resultado futuro mensuravel e compare opcoes, inclusive simplificar processo, configurar ferramenta existente, automatizar, construir algo novo ou manter o estado atual. Compare valor, custo total, tempo, risco, viabilidade, dependencia e reversibilidade. Uma recomendacao deve dizer por que supera as alternativas no contexto do cliente.

Em processos, represente atores, eventos, handoffs, decisoes, esperas, retrabalho, excecoes, controles e metricas no AS-IS e no TO-BE. Use BPMN ou outro diagrama somente se facilitar alinhamento; nao produza notacao pesada para um fluxo simples. Em mudanca organizacional, inclua treinamento, comunicacao, suporte, dono operacional, transicao e medicao de adocao.

## 4. Definir, verificar e gerir requisitos

Classifique quando pertinente: **negocio** (resultado e restricao da organizacao), **stakeholder** (necessidade do papel), **solucao funcional** (comportamento), **solucao nao funcional** (qualidade/limite) e **transicao** (migracao, treinamento, operacao temporaria). Nao chame uma preferencia de tecnologia de necessidade de negocio sem evidencia.

Para cada requisito relevante, preserve ID, fonte, dono, status, prioridade justificada, dependencia, regra, aceite observavel e relacao com objetivo. Verifique clareza, singularidade, consistencia e viabilidade; valide se resolve a necessidade. Rastreie `objetivo → requisito → desenho/opcao → teste/UAT → medida de resultado`. Requisitos inferidos ou propostos ficam assim rotulados ate a decisao. Mudanca posterior pede analise de impacto em prazo, custo, escopo, dados, operacao e beneficios, com historico de versoes.

Priorize por valor, risco, urgencia e dependencias. Use MoSCoW, RICE ou matriz simples somente se houver informacao para pontuar; nao invente scores. Diferencie MVP, obrigacao indispensavel e melhoria futura.

## 5. Definir opcoes e preparar entrega

Desenhe alternativas de processo ou solucao com limites claros, fluxo ponta a ponta, responsaveis, integracoes e controles. Para software, a arquitetura e proposta ate inspecionar stack, contratos e restricoes reais. Produza backlog ou plano de transicao com ordem por dependencia, criterios de aceite, UAT, risco e responsaveis. Se a solicitacao for executar, avance para implementacao e verificacao; nao pare no documento.

## 6. Avaliar a solucao e realizar valor

Antes da mudanca, estabeleca baseline, objetivo, fonte, periodo e responsavel por cada medida. Depois, compare resultado e adocao com a linha de base; investigue limitacoes da solucao e da organizacao, efeitos indesejados e custo operacional. Recomende manter, corrigir, ampliar, reverter ou aposentar com base em evidencia. Relate beneficios realizados separadamente dos previstos; uma entrega tecnicamente concluida nao comprova valor de negocio.

## Entregas comuns por pergunta

| Pergunta | Entrega minima util |
|---|---|
| Qual problema resolver? | Diagnostico, estado atual, causa a testar e resultado desejado |
| Qual opcao escolher? | Alternativas, business case, riscos, dependencia e recomendacao |
| O que construir/mudar? | Requisitos rastreaveis, regras, fluxos, dados, aceite e transicao |
| Como alinhar pessoas? | Mapa de stakeholders, decisoes, comunicacao e responsabilidades |
| Funcionou? | Baseline, medicao, limites, adocao, beneficios e proxima decisao |

Adapte a profundidade ao custo de errar. Uma resposta curta pode ser completa se abordar a decisao, as evidencias e as dependencias que realmente importam.
