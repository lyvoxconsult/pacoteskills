# Exemplo sintetico: call sobre dashboard de planilha

Este exemplo nao representa cliente real, arquivo real nem aprovacao. Mostra como a skill deve ir alem de repetir "quero um dashboard".

## Material recebido

**Trecho de transcricao ficticia:**

> Cliente: "Toda sexta recebo uma planilha de pedidos. Copio os dados, vejo quanto cada vendedor fez e mando um grafico. Quero anexar a planilha e o painel aparecer pronto. Algumas linhas sao canceladas; hoje eu tiro elas na mao."

**Pedido do usuario:** "Transforme essa call em requisitos para eu validar com o cliente."

## Descoberta para validacao

**Objetivo observado:** reduzir trabalho manual semanal e permitir acompanhar pedidos por vendedor. **Processo atual declarado:** receber arquivo, copiar dados, excluir cancelados manualmente, calcular totais e enviar grafico. **Pendente:** o significado de "quanto fez" pode ser quantidade, valor bruto, valor liquido ou comissao; nenhuma dessas formulas esta aprovada.

| ID | Tipo | Capacidade ou decisao | Por que existe | Evidencia/estado |
|---|---|---|---|---|
| RF-01 | Pedido explicito | Permitir anexar uma planilha e gerar um painel a partir dela. | Substituir copia manual. | Trecho da call; declarado |
| RD-01 | Habilitador indispensavel | Identificar abas, cabecalhos, colunas e grao de cada linha antes do calculo. | Sem isso, o painel pode somar campos errados. | Inferido; validar com arquivo real |
| RD-02 | Habilitador indispensavel | Definir regra de exclusao de cancelados e tratamento de status ausente. | Hoje ha exclusao manual; totais ficam incorretos sem a regra. | Regra citada; detalhes pendentes |
| RD-03 | Habilitador indispensavel | Definir se a planilha semanal substitui ou acrescenta pedidos. | Sem chave e politica de atualizacao, importacoes repetidas podem duplicar resultados. | Inferido; decisao pendente |
| DC-01 | Decisao em aberto | Definir a formula de "quanto cada vendedor fez" e a data de referencia. | Determina metricas e graficos. | Termo ambiguo da call |
| OP-01 | Melhoria opcional | Exportar o painel em formato compartilhavel. | Pode reduzir envio manual, mas nao foi pedido explicitamente. | Proposta; fora do MVP ate aprovacao |

**Mapa de dependencias:** `anexar planilha (RF-01) → ler/mapear estrutura (RD-01) → aplicar status de cancelamento (RD-02) → definir atualizacao sem duplicidade (RD-03) → calcular metrica aprovada (DC-01) → escolher visual e filtros`. O mapa e uma hipotese de requisitos; a ordem tecnica final depende do arquivo e do ambiente real.

**Perguntas essenciais ao cliente:** (1) O que significa "quanto fez"? (2) Cancelado exclui do total ou aparece separado? (3) Cada arquivo substitui ou complementa a semana anterior? (4) Quem pode ver os resultados por vendedor?

**Criterio de aceite provisório:** com uma planilha de teste aprovada, importar duas vezes o mesmo arquivo nao altera o total; pedidos cancelados seguem a regra confirmada; cada grafico exibe formula, periodo e filtros. A planilha real ainda nao foi inspecionada, portanto nomes de colunas e valores nao aparecem como fatos.

## Apos aprovacao real

Registrar versao, aprovador, data e ressalvas; inspecionar o arquivo real; consolidar dicionario de dados, requisitos, regras, arquitetura proposta, backlog, testes/UAT e etapas de construcao. Se o cliente mudar a formula ou escopo, registrar impacto e nova versao para aceite.
