# Descoberta BA a partir de call, gravacao ou transcricao

## 1. Preparar a evidencia

- Identifique arquivos, data, participantes/papeis conhecidos, idioma, versao da transcricao e trechos inaudiveis. Nao deduza identidade de falantes sem base.
- Se audio e transcricao existirem, confira no audio as afirmacoes que definem requisito, numero, prazo, permissao, integracao ou excecao. Marque divergencias entre fala e texto.
- Use referencias `Fonte: arquivo, falante, timestamp` quando existirem; sem timestamp, indique pagina, secao ou trecho identificavel. Nao espalhe transcricao integral ou PII pelo documento.
- Compare o relato com documentos, sistemas e planilhas anexos quando disponiveis. Distingua o que o cliente diz fazer do que o sistema real permite.

## 2. Extrair e testar o entendimento

Organize as observacoes por: objetivo, dor, processo atual, usuarios, volume/frequencia, entradas, regras, excecoes, ferramentas atuais, saidas, restricoes, metricas, riscos e pontos de desacordo. Reescreva em linguagem objetiva, preservando a intencao. Se uma frase admitir duas interpretacoes, registre ambas e a pergunta de decisao.

Para cada capacidade aparente, percorra:

1. **Gatilho:** quem ou o que inicia a acao?
2. **Pre-condicao:** dados, identidade, permissao, configuracao ou evento necessario.
3. **Transformacao:** validacao, regra, calculo, aprovacao, mudanca de estado ou integracao.
4. **Resultado:** saida, destino, visibilidade, notificacao e uso na decisao.
5. **Falhas:** dado ausente, duplicado, invalido, atraso, indisponibilidade e recuperacao.
6. **Dependencias:** componentes, decisoes, fornecedores ou equipes necessarios; classifique indispensavel ou opcional.

## 3. Pacote de validacao para o cliente

O documento deve ser legivel pelo cliente e suficiente para desenvolvimento posterior. Esconda detalhes de implementacao que ainda nao foram decididos, mas explicite toda regra que afeta o comportamento.

1. **Resumo:** problema, objetivo, usuarios, resultado esperado e limites do entendimento.
2. **Fluxo atual e fluxo proposto:** etapas, atores, ferramentas, entradas, saidas e pontos de dor.
3. **Escopo:** MVP, fora do escopo, dependencias e melhorias opcionais separadas.
4. **Requisitos funcionais:** IDs estaveis; comportamento atomico, gatilho, entrada, regra, saida, excecao, criterio de aceite e fonte/status.
5. **Regras e dados:** dicionario de termos, entidades, permissao, origem, qualidade, retencao e integracao.
6. **Requisitos nao funcionais:** privacidade, seguranca, acessibilidade, disponibilidade, volume, suporte e auditoria na medida relevante.
7. **Decisoes do cliente:** poucas perguntas materiais, com opcoes, impacto e recomendacao quando fundamentada.
8. **Aceite da descoberta:** o que sera aprovado agora e o que ficara para desenho tecnico apos aprovacao.

Tabela compacta de rastreabilidade:

| ID | Necessidade/ator | Comportamento e regra | Dependencia | Aceite observavel | Evidencia | Status |
|---|---|---|---|---|---|---|
| RF-01 | Exemplo: analista precisa consolidar solicitacoes | Ao importar arquivo valido, registrar itens sem duplicar IDs ja existentes | RD-01: chave unica definida | Importar duas vezes o mesmo arquivo nao duplica itens | Call 00:12:40; arquivo exemplo | Proposta a validar |

Tipos de status sugeridos: `declarado pelo cliente`, `observado no sistema/arquivo`, `inferido`, `proposto`, `em conflito`, `aprovado`. `Aprovado` exige evidência real de aprovação; ausência de objeção não basta.

## 4. Gate de aprovacao e continuidade

- Prepare o pacote para revisao. Nao o envie ao cliente sem pedido/autorizacao do usuario.
- Registre aprovador, data, versao, escopo aprovado e ressalvas somente quando a aprovacao existir. Se o cliente aprovar parcialmente, separe aprovado, rejeitado e pendente.
- Depois do aceite, consolide BRD/PRD ou especificacao funcional, desenho tecnico proposto, matriz de rastreabilidade, backlog com dependencias, plano de implementacao, testes/UAT e criterios de conclusao. Se a escolha tecnica depende do repositorio ou fornecedores, inspecione-os antes de fixar a arquitetura.
- Quando surgir pedido novo apos o aceite, registre mudanca, impacto em custo/prazo/risco e nova decisao. Nao altere silenciosamente a versao aprovada.
