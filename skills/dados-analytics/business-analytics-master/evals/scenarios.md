# Cenarios de avaliacao manual

Use estes casos para revisar a skill depois de mudancas. Avalie a resposta produzida por um agente que carregou `SKILL.md`; a existencia deste arquivo, sozinha, nao prova comportamento do agente.

| Entrada simples | Deve produzir | Falha a evitar |
|---|---|---|
| "Quero uma ferramenta para pedidos internos com anexos e avisos. Documente." | Documento com objetivo, atores, fluxos, requisitos numerados, regras/pendencias, arquitetura proposta, seguranca, aceite e validacao. | Apenas um prompt para outro agente; stack ou regras inventadas. |
| "Crie um prompt para um agente documentar minha ferramenta de reservas." | Prompt executavel com fontes a inspecionar, requisitos, riscos, testes e criterios de aceite. | Criar documento final no lugar do prompt explicitamente pedido. |
| "Precisamos reduzir o tempo de atendimento. O que mudar?" | Diagnostico BA do processo atual, hipoteses, dados necessarios, opcoes, impactos e plano de medicao. | Afirmar causa raiz sem evidencia ou impor arquitetura de software. |
| "Nossa conversao caiu; descubra por que." | Definicao da metrica, periodos comparaveis, verificacao de qualidade, decomposicao por drivers e niveis de certeza. | Alegar causalidade ou inventar numeros sem dados. |
| "Qual fornecedor de CRM escolher?" | Criterios ponderados, requisitos eliminatorios, fontes, custos/riscos comparaveis e pendencias. | Recomendar por popularidade sem contexto e evidencias atuais. |
| "Crie a ferramenta de pedidos no repositorio." | Inspecao do projeto, estrategia, implementacao e testes reais, com relato do que foi ou nao validado. | Entregar apenas planejamento ou especificacao. |
| "Anexei a gravacao e a transcricao da call. Extraia requisitos para o cliente aprovar." | Conferencia dos trechos criticos no audio, referencias por falante/tempo, requisitos, dependencias indispensaveis, sugestoes opcionais e pacote de validacao. | Inventar fala/timestamp ou tratar hipotese como decisao aprovada. |
| "O cliente aprovou a versao 2 com estas ressalvas. Planeje a construcao." | Registro da evidencia de aceite e ressalvas, especificacao consolidada, dependencias, arquitetura proposta, fases e UAT. | Alterar silenciosamente requisito aprovado ou assumir aprovacao irrestrita. |
| "Quero anexar uma planilha e ver tudo num dashboard" sem arquivo | Perguntas de negocio, fluxo completo de importacao, dicionario preliminar de campos e pequena lista de dados a confirmar. | Inventar colunas, metricas, formulas ou graficos definitivos. |
| "Aqui esta a planilha; monte a especificacao do dashboard" com arquivo real | Inspecao de abas/grao/tipos, mapa campo → transformacao → metrica → visual, qualidade, permissoes, atualizacao e casos de erro. | Desenhar apenas telas ou somar linhas de graos incompatíveis. |
| "Quero so uma funcao para descrever a planilha" | Explicacao do fluxo de leitura, semantica das colunas, tratamento de erro, regras de resumo, origem das afirmacoes e requisitos habilitadores. | Repetir literalmente o pedido como um unico requisito vago. |

Checklist transversal: resposta atende ao verbo do pedido; fatos, inferencias, propostas e pendencias estao separados; requisitos sao verificaveis; o nivel de detalhe e proporcional; fontes e limites estao claros; nenhuma validacao foi inventada.
