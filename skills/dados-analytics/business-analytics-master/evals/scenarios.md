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

Checklist transversal: resposta atende ao verbo do pedido; fatos, inferencias, propostas e pendencias estao separados; requisitos sao verificaveis; o nivel de detalhe e proporcional; fontes e limites estao claros; nenhuma validacao foi inventada.
