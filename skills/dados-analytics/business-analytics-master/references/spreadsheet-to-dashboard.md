# Da planilha ao dashboard que responde perguntas reais

## 1. Entender a decisao

Registre quem vai usar o dashboard, as perguntas que ele precisa responder, a frequencia da decisao e o que faria depois de ver cada indicador. Uma coluna disponivel nao vira KPI automaticamente. Diferencie painel operacional, tatico e executivo.

## 2. Ler a planilha real

Inventarie abas, cabecalhos, linhas, formulas, celulas mescladas, filtros, campos calculados, datas, unidades, moeda, IDs, dados pessoais, vazios e duplicatas. Identifique o grao de cada aba: uma linha representa pessoa, pedido, evento, fatura, dia ou outra entidade? Se houver varias abas, verifique chaves e cardinalidade antes de unir. Nao use amostra sintetica como prova sobre o arquivo real.

## 3. Criar dicionario e mapa de transformacao

| Campo/aba de origem | Significado confirmado ou pendente | Tipo, unidade e grao | Validacao | Transformacao | Metrica/visual | Decisao apoiada |
|---|---|---|---|---|---|---|
| Campo observado no arquivo | Definicao do negocio, com fonte | Data/valor/ID; uma linha por entidade | Nulos, formato, intervalo, duplicidade | Normalizar, agregar ou filtrar | Formula e filtro documentados | Acao que o usuario tomara |

Para cada metrica, documente formula, numerador, denominador, periodo, fuso, filtros, exclusoes, fonte, frequencia de atualizacao e dono da definicao. Mostre exemplos calculados com linhas reais somente se os dados puderem ser expostos; caso contrario use exemplo sintetico rotulado e valide o calculo separadamente.

## 4. Mapear o fluxo de ponta a ponta

`arquivo anexado → validacao de tipo/tamanho → leitura de abas e schema → mapeamento de campos → regras de limpeza → calculo → armazenamento/acesso → dashboard → exportacao/atualizacao`

Para cada etapa, especifique entrada, saida, responsavel, erro e recuperacao. Diferencie upload unico de atualizacao recorrente. Defina se cada novo arquivo substitui, acrescenta ou versiona dados; sem essa regra, totais podem duplicar. Verifique permissão por usuario/equipe, retencao, exclusao e auditoria quando houver dados sensiveis.

## 5. Especificar o painel

- Hierarquia: perguntas principais, KPIs, tendencias, detalhamento, filtros e notas de definicao.
- Cada visual tem pergunta, eixo, unidade, periodo, formula, fonte, estado vazio e criterio de interpretacao.
- Filtros devem preservar denominadores e evitar comparacoes de periodos/populacoes incompatíveis.
- Teste com casos de arquivo valido, vazio, colunas renomeadas, datas invalidas, moeda misturada, duplicidade, planilha atualizada e usuario sem permissao.
- Use prototipo ou wireframe simples quando reduzir ambiguidade; nao alegue que o dashboard funciona sem implementar e testar com os dados reais.

Se o arquivo nao foi fornecido, produza uma especificacao preliminar com perguntas, campos esperados e decisoes pendentes. Solicite a menor amostra segura necessaria para fechar o mapeamento.
