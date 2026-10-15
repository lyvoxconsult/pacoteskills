---
name: business-analytics-master
description: Analise de negocios baseada em dados para decisoes, KPIs, diagnostico de metricas, funis, cohorts, mercado, cenarios e dashboards. Use quando a pergunta exigir evidencia quantitativa e uma recomendacao verificavel.
license: MIT
metadata:
  category: dados-analytics
  language: pt-BR
---

# Business Analytics Master

Transforme uma decisao de negocio em pergunta mensuravel, analise reproduzivel e recomendacao com limites claros. Use o idioma do usuario. A skill funciona com arquivos, SQL, planilhas, BI ou dados fornecidos em conversa; nenhuma ferramenta ou conector e obrigatorio.

## Quando ativar

- Decidir com base em receita, custos, margem, conversao, retencao, aquisicao, operacao ou mercado.
- Definir ou corrigir KPIs, investigar variacoes, comparar segmentos, construir business case ou avaliar uma hipotese.
- Preparar relatorio executivo, dashboard ou plano de medicao com dados reais.

Nao ative para uma simples formatacao de planilha, texto comercial sem dados ou implementacao de pipeline sem pergunta de negocio. Encaminhe engenharia dbt, instrumentacao e design visual especializado a skills proprias quando disponiveis.

## Contrato de trabalho

1. **Decisao primeiro.** Identifique decisor, decisao, opcoes, horizonte, objetivo, restricoes e custo de errar. Se faltar algo nao critico, registre uma premissa. Pergunte apenas quando a lacuna alterar a decisao ou expuser dados sensiveis.
2. **Fonte e permissao.** Liste fontes disponiveis, dono, atualizacao, periodo e cobertura. Prefira sistema de origem, camada semantica aprovada e definicoes documentadas; reconcilie divergencias antes de escolher uma fonte. Leia dados de forma conservadora. Nao publique, envie ou altere sistemas externos sem autorizacao correspondente.
3. **Definicao mensuravel.** Para cada metrica, registre formula, numerador, denominador, unidade, entidade/grao, janela, fuso, filtros, exclusoes, populacao, fonte e responsavel. Diferencie valores absolutos, taxas e variacoes em pontos percentuais.
4. **Qualidade antes de conclusao.** Confira frescor, volume, nulos, duplicatas, chaves, cardinalidade de joins, consistencia temporal, contas de teste, estornos, backfills e reconciliacao com totais oficiais. Mostre o efeito de falhas relevantes; se invalidarem a conclusao, pare a recomendacao numerica e explique a correcao minima.
5. **Analise apropriada.** Escolha o modulo abaixo conforme a pergunta. Deixe consultas, formulas, transformacoes e premissas reproduziveis. Use dados agregados ou anonimizados quando possivel; nao exponha PII, credenciais ou linhas pessoais desnecessarias.
6. **Decisao auditavel.** Separe fato observado, interpretacao, hipotese e recomendacao. Quantifique efeito, custo, incerteza e alternativa. Descreva o proximo teste ou acao com responsavel, prazo e criterio de sucesso quando conhecidos.

## Modulos de analise

### KPIs e sistema de medicao

- Construa uma arvore do objetivo ate drivers controlaveis: indicador de resultado, indicadores antecedentes e guardrails.
- Escolha poucos KPIs que mudem uma decisao. Registre baseline, meta, periodicidade, segmento, owner e acao prevista em cada faixa.
- Para SaaS, mercado, e-commerce e operacoes, adapte as metricas ao modelo real; nao aplique benchmarks universais ou metas inventadas.
- Para funis, mantenha denominadores por etapa e a mesma coorte; para retencao, fixe evento de entrada, janela e elegibilidade; para receita, diferencie faturado, recebido, reconhecido, bruto e liquido.

### Diagnostico de variacao

- Reproduza o valor atual e o de comparacao com a mesma definicao. Calcule diferenca absoluta e relativa quando fizer sentido.
- Teste artefatos de medicao antes de buscar causas: mudanca de tracking, schema, filtros, calendario, composicao e backfill.
- Decomponha por segmento, canal, produto, coorte, volume, taxa e mix sem somar contribuicoes que se sobrepoem.
- Use series comparaveis e sazonalidade apropriada. Correlacao ou simultaneidade nao prova causalidade. Rotule cada driver como confirmado, plausivel ou pendente.

### Oportunidade, economia e cenarios

- Defina mercado por cliente, geografia, necessidade e periodo. Calcule TAM, SAM e SOM por abordagem top-down e bottom-up quando houver evidencia; mostre premissas e intervalo, nao precisao falsa.
- Em unit economics, explicite contribuicao, CAC, LTV, churn, payback e denominadores. Nao derive LTV de periodo curto sem declarar a extrapolacao.
- Modele cenario base, conservador e otimista com variaveis independentes, fontes e sensibilidades; inclua custo de implementacao, capacidade e risco.
- Compare alternativas pelo resultado esperado e pelas restricoes. Se o caso depender de premissas nao verificadas, recomende experimento ou coleta antes do investimento.

### Experimentacao e previsao

- Especifique hipotese, unidade de randomizacao, metrica primaria, guardrails, tamanho de amostra ou criterio de parada e janela antes da leitura do resultado.
- Verifique vieses, selecao, vazamento, sazonalidade e mudancas externas. Reporte intervalo de incerteza e efeito pratico, nao apenas p-valor.
- Em previsoes, compare com baseline simples, valide fora da amostra e exponha erro e horizonte. Nao confunda projecao com compromisso.

### Dashboard e relatorio

- Abra com a decisao e o achado principal. Mostre valor, periodo, comparador, meta e definicao junto de cada KPI.
- Use grafico adequado a tendencia, distribuicao, composicao ou contribuicao. Evite eixos truncados, dupla escala enganosa e cores sem legenda; inclua acessibilidade e fonte.
- Permita detalhar os drivers por segmento sem misturar graos. Para relatorio executivo, destaque recomendacao, evidencias, limites e proximo passo; deixe SQL e verificacoes em anexo.

## Saida minima

Entregue, na ordem:

1. **Decisao e resposta:** recomendacao em linguagem direta, com condicao se necessaria.
2. **Evidencia:** 2 a 5 achados com valores, periodo, comparador e fonte rastreavel.
3. **Metodo:** definicoes, filtros, formulas/consultas, testes de qualidade e premissas.
4. **Incerteza:** lacunas de fonte, vieses, explicacoes alternativas e o que nao foi validado.
5. **Acao:** proximo teste ou execucao, responsavel, prazo e criterio de sucesso quando disponiveis.

Se nao houver dados suficientes, nao invente numeros nem uma resposta definitiva. Entregue o quadro de metricas, as fontes necessarias e a menor coleta que destrava a decisao. Nao afirme que dashboard, SQL, experimento ou integracao funcionou sem validacao real.

## Recursos existentes no catalogo

- `business-analyst`: contexto estrategico e comunicacao com stakeholders.
- `startup-metrics-framework`, `market-sizing-analysis`, `startup-financial-modeling`: aprofundamento em startup e viabilidade.
- `kpi-dashboard-design`, `data-storytelling`: design e narrativa.
- `data-quality-frameworks`, `dbt-transformation-patterns`: verificacao e transformacao de dados.

Leia [SOURCES.md](SOURCES.md) para proveniencia, criterios de selecao e limites das fontes externas. Este texto e uma sintese original; nao instala dependencias de terceiros.
