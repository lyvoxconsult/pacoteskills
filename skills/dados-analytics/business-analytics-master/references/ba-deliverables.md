# Escolha do artefato BA

Use apenas as secoes que ajudam o leitor a tomar uma decisao ou executar o trabalho. Nao transforme toda solicitacao em um documento gigante. Em cada artefato, separe fatos, premissas, propostas e pendencias.

| Pedido do usuario | Entrega principal | Perguntas de qualidade |
|---|---|---|
| "Anexei a gravacao/transcricao da call. Estruture o que o cliente precisa" | Pacote de descoberta para validacao do cliente, com rastreabilidade | O que foi dito, inferido ou sugerido? Quais dependencias sao indispensaveis? O que precisa de aprovacao? |
| "O cliente aprovou os requisitos. Planeje a construcao" | Especificacao consolidada, arquitetura proposta, backlog e validacao | Qual versao foi aprovada? Que decisoes mudaram? O plano respeita as dependencias? |
| "Transforme esta planilha em dashboard" | Dicionario de dados, mapa campo → metrica → visual e fluxo de importacao | O significado, grao, formula e qualidade de cada dado foram conferidos? |
| "Documente a ferramenta que quero criar" | Especificacao funcional e tecnica proposta | Quem usa? Qual problema? Quais fluxos, regras, dados, permissoes, integracoes e aceite? |
| "Explique como melhorar este processo" | Diagnostico AS-IS/TO-BE, lacunas e plano de transicao | Onde ha espera, retrabalho, erro, controle, dependencia e medicao? |
| "Transforme minha ideia em requisitos" | BRD/PRD enxuto, backlog e rastreabilidade | Cada requisito cria valor? E observavel e testavel? |
| "Vale a pena fazer?" | Business case e alternativas | Beneficio, custo, riscos, capacidade, premissas e sensibilidade foram explicitados? |
| "O que medir?" | Arvore de metricas e dicionario de KPIs | Formula, grao, fonte, owner, baseline, guardrail e acao estao definidos? |
| "Por que o indicador caiu?" | Diagnostico de metricas | Comparacao reproduzida, qualidade testada e drivers quantificados? |
| "Avalie fornecedores" | Criterios ponderados e decisao rastreavel | Pesos, evidencias, requisitos eliminatorios e riscos sao comparaveis? |
| "Prepare a validacao" | Plano UAT e matriz requisito → teste | Ha cenarios positivos, negativos, permissoes, excecoes e aceite do negocio? |
| "Crie um prompt para fazer isso" | Prompt executavel para outro agente | O executor sabe o que ler, fazer, testar e relatar? |

## Especificacao de ferramenta digital

Estrutura recomendada para uma ferramenta nova. Omitir ou reduzir secoes que nao se aplicam; aprofundar riscos altos.

1. **Resumo e problema:** objetivo, publico, dor atual, resultado esperado e evidencia disponivel.
2. **Escopo:** dentro, fora, MVP, fases futuras e dependencias.
3. **Stakeholders e usuarios:** papeis, necessidades, permissoes e responsaveis por decisoes.
4. **Jornadas e processos:** gatilho, caminho principal, alternativas, erros, cancelamento, estados e notificacoes quando relevantes.
5. **Requisitos funcionais:** IDs estaveis (`RF-01`), verbo observavel, ator, entrada, processamento, saida, regra, prioridade e criterio de aceite.
6. **Regras de negocio:** IDs (`RN-01`), condicoes, excecoes, precedencia e origem da regra.
7. **Dados e integracoes:** entidades, campos sensiveis, fonte de verdade, validacoes, sincronizacao, falhas, retencao e migracao quando aplicavel.
8. **Arquitetura proposta:** componentes, fronteiras, fluxo de dados, autenticacao/autorizacao, dependencias, alternativas e decisoes pendentes. Nao afirmar stack existente sem inspecao.
9. **Requisitos nao funcionais:** seguranca, LGPD, acessibilidade, desempenho, disponibilidade, observabilidade, backup, suporte e compatibilidade; metas numericas somente com base ou marcadas como proposta.
10. **Riscos e premissas:** impacto, probabilidade quando justificavel, mitigacao, responsavel e modo de validar.
11. **Aceite e validacao:** matriz requisito → teste/UAT; testes funcionais, permissao, erro, recuperacao e medicao de resultado.
12. **Decisoes pendentes:** somente lacunas que alteram produto, arquitetura, custo, risco ou aceite.

Em descoberta com cliente, use [discovery-from-call.md](discovery-from-call.md) antes da especificacao final. Em painel baseado em anexo, use [spreadsheet-to-dashboard.md](spreadsheet-to-dashboard.md) antes de escolher graficos ou tecnologia.

Modelo de requisito:

| ID | Ator e comportamento | Regra vinculada | Prioridade | Criterio de aceite | Estado da informacao |
|---|---|---|---|---|---|
| RF-01 | O solicitante registra uma demanda com tipo, descricao e anexos opcionais | RN-01 | MVP | Dado um usuario autorizado, quando envia dados validos, a demanda recebe ID e estado inicial visivel | Exemplo proposto |

Escreva o aceite em termos verificaveis, incluindo casos de erro quando relevantes. Evite "o sistema deve ser intuitivo" sem indicador ou teste com usuarios definido. A arquitetura e uma hipotese de desenho ate que o ambiente real e as restricoes sejam conferidos.

## Prompt executavel, somente quando solicitado

1. Contexto e fatos verificados, com fontes.
2. Objetivo e artefatos finais esperados.
3. Escopo, restricoes, seguranca e privacidade.
4. Requisitos funcionais/nao funcionais e arquitetura proposta, se pertinente.
5. Ordem de execucao: inspecionar, resolver ambiguidades criticas, implementar/documentar, testar, corrigir e relatar.
6. Ferramentas e fontes que o executor deve consultar quando disponiveis.
7. Criterios de aceite objetivos e evidencias de validacao.
8. Obrigacao de distinguir fatos, premissas, resultados testados e limites.

Se o pedido original for executar ou documentar, use a estrutura para orientar seu proprio trabalho e entregue o resultado, sem despejar esse prompt como substituto.
