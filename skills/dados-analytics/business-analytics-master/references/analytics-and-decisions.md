# Analise quantitativa e decisao de negocio

Use quando o pedido exigir numeros, metricas, mercado, experimento, previsao ou dashboard. Comece pela decisao: quem decide, quais opcoes, horizonte, objetivo, restricoes e custo de errar.

## Contrato de evidencia

1. Identifique fontes, dono, periodo, atualizacao, cobertura, permissao e definicoes. Prefira sistema de origem e camada semantica aprovada; reconcilie divergencias antes de concluir.
2. Para cada metrica, registre formula, numerador, denominador, unidade, grao, janela, fuso, filtros, exclusoes, populacao, fonte e responsavel. Diferencie valores, taxas e pontos percentuais.
3. Confira frescor, volume, nulos, duplicatas, chaves, cardinalidade de joins, estornos, backfills e conciliacao com totais oficiais. Quantifique o efeito de falhas relevantes. Se elas invalidarem a conclusao, suspenda a recomendacao numerica e indique a correcao minima.
4. Deixe calculos, consultas, transformacoes e premissas reproduziveis. Proteja dados pessoais; publique somente agregados ou exemplos sinteticos quando necessario.
5. Separe fato observado, interpretacao, hipotese e recomendacao. Compare opcoes com efeito, custo, risco e incerteza; indique o proximo teste quando a evidencia for insuficiente.

## Metodos por pergunta

**O que medir?** Construa arvore do objetivo ate drivers controlaveis: resultado, indicadores antecedentes e guardrails. Escolha poucos KPIs que mudem uma acao. Registre baseline, meta, periodicidade, segmento, dono e resposta prevista a cada faixa. Para funis, preserve denominadores por etapa e coorte; para retencao, fixe entrada e janela; para receita, diferencie faturado, recebido, reconhecido, bruto e liquido.

**Por que mudou?** Reproduza valor atual e comparador com a mesma definicao. Teste primeiro mudancas de tracking, schema, filtros, calendario, composicao e backfill. Decomponha por segmento, canal, produto, coorte, volume, taxa e mix sem somar contribuicoes sobrepostas. Rotule explicacao confirmada, plausivel ou pendente; correlacao nao prova causa.

**Vale a pena?** Defina cliente, geografia, necessidade e periodo. Para mercado, calcule TAM/SAM/SOM apenas com fontes e premissas explicitas, preferindo mais de uma abordagem quando possivel. Em economia da unidade, exponha contribuicao, CAC, LTV, churn e payback com denominadores; nao extrapole periodo curto silenciosamente. Compare cenarios base, conservador e otimista e teste sensibilidade de variaveis decisivas, custos, capacidade e risco.

**Qual experimento ou previsao?** Defina hipotese, unidade de randomizacao, metrica primaria, guardrails, janela, amostra ou criterio de parada antes da leitura. Verifique selecao, sazonalidade, vazamento e mudancas externas. Em previsao, compare com baseline simples e valide fora da amostra; exponha erro, intervalo e horizonte. Nao confunda projecao com compromisso.

**Como mostrar?** Abra com decisao e achado principal. Junto de cada KPI, mostre valor, periodo, comparador, meta, definicao e fonte. Selecione visual conforme tendencia, distribuicao, composicao ou contribuicao. Evite eixo enganoso, dupla escala confusa e cores sem legenda; permita detalhar drivers sem misturar graos. Para planilhas, leia [spreadsheet-to-dashboard.md](spreadsheet-to-dashboard.md).

Entregue resposta e recomendacao primeiro, depois 2 a 5 achados, metodo reproduzivel, incerteza e acao. Sem dados suficientes, entregue a estrutura da decisao e a menor coleta necessaria; nao fabrique numeros.
