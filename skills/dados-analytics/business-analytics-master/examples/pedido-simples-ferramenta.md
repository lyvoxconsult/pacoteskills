# Exemplo sintetico: de pedido simples a documentacao BA

**Entrada do usuario:** "Quero uma ferramenta para minha equipe abrir pedidos internos, anexar arquivos, ver o andamento e receber aviso quando mudar. Crie a documentacao."

**Interpretacao:** o usuario pediu uma documentacao pronta. O texto abaixo e apenas um trecho ilustrativo do artefato; uma entrega real deve completar as secoes aplicaveis apos consultar contexto e fontes disponiveis.

## Trecho de documento resultante

### Objetivo e escopo

Propor uma ferramenta para registrar, acompanhar e comunicar o andamento de pedidos internos. O objetivo de negocio e reduzir perda de solicitacoes e dar visibilidade ao solicitante. **Premissa:** ha uma equipe responsavel por tratar os pedidos; seu tamanho e fluxo atual precisam ser confirmados.

MVP proposto: cadastro de pedido, anexo opcional, lista com estado atual, historico de mudancas e aviso ao solicitante quando o estado mudar. A escolha do canal de aviso (e-mail, aplicativo ou outro) esta **pendente de validacao**. Nao foi pedido um fluxo de aprovacao; ele fica fora do MVP ate que exista regra de negocio confirmada.

### Atores e fluxo

- **Solicitante:** cria pedido e consulta seus pedidos.
- **Atendente:** visualiza pedidos atribuidos, altera estado e registra comentario de andamento.
- **Gestor:** acompanha fila e indicadores agregados. Este papel e uma **proposta**, a confirmar.

Fluxo principal: solicitante envia pedido valido → sistema atribui identificador → pedido fica disponivel na fila → atendente registra andamento → solicitante visualiza o historico e recebe aviso no canal configurado. Fluxos alternativos: arquivo invalido, falha de entrega do aviso, falta de permissao, pedido duplicado e cancelamento; as regras de cada caso exigem decisao do negocio.

### Requisitos e aceite ilustrativos

| ID | Requisito | Criterio de aceite | Estado |
|---|---|---|---|
| RF-01 | O solicitante autorizado registra um pedido com titulo e descricao. | Com campos validos, o sistema cria um ID unico e mostra o estado inicial. Com campo obrigatorio vazio, nao cria o pedido e informa o campo. | Proposta baseada no pedido |
| RF-02 | O solicitante anexa arquivo ao pedido. | Um arquivo permitido aparece no pedido apos envio; tamanho/tipo permitidos e tratamento de malware dependem da politica real. | Funcao confirmada; limites pendentes |
| RF-03 | O solicitante consulta estado e historico dos proprios pedidos. | Um usuario nao autorizado nao acessa pedido de outra pessoa; toda mudanca autorizada aparece com data e responsavel. | Proposta de controle |
| RF-04 | O sistema solicita um aviso quando o estado muda. | A mudanca fica registrada mesmo se o envio falhar; a falha e visivel para reprocessamento. | Canal e regra de retentativa pendentes |

### Arquitetura proposta

Interface de usuario → servico de pedidos → armazenamento de pedidos/anexos; a mudanca de estado gera um evento para o componente de notificacao. Autenticacao e autorizacao devem ser integradas ao mecanismo corporativo confirmado. Este desenho **nao afirma** que tais componentes ja existem nem escolhe tecnologia sem inspecionar o ambiente.

### Validacao e decisao pendente

Validar com os responsaveis: tipos de pedido, estados permitidos, quem pode ver cada pedido, politica de anexos, canal de aviso, retencao e prazo de atendimento. O UAT deve cobrir os quatro requisitos, permissao negada, anexo invalido e falha de aviso. O indicador de resultado proposto e a proporcao de pedidos com estado atualizado dentro do prazo acordado; formula e prazo precisam ser definidos antes de medir.

**Se a entrada fosse "crie um prompt para documentar essa ferramenta"**, a saida principal seria um prompt executavel com contexto, escopo, fontes a consultar, criterios de aceite e instrucoes de verificacao. **Se fosse "crie a ferramenta"**, a saida exigiria implementacao e testes no projeto real.
