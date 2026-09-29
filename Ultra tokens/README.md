# Ultra Tokens

Pacote portatil de skills para economia de tokens, engenharia de prompt, coleta
de contexto, raciocinio e qualidade de entrega. Esta pasta substitui a antiga
`tokens` e foi organizada para que colegas possam copiar somente este conjunto,
sem baixar o repositorio inteiro.

## Objetivo

Usar as melhores skills em conjunto para:

- reduzir tokens por tarefa, nao apenas por resposta;
- evitar loops, buscas amplas e repeticao desnecessaria;
- transformar pedidos vagos em prompts tecnicos executaveis;
- coletar contexto real sem carregar ruido;
- preservar decisoes, caminhos, erros e evidencias importantes;
- entregar respostas curtas, verificaveis e acionaveis.

## Ordem recomendada de uso

1. `find-skills`: descobrir se existe uma skill local mais especifica para a tarefa.
2. `i-have-adhd`: manter comunicacao curta, numerada, objetiva e facil de escanear.
3. `devpromptarchitect` ou `dev-prompt-architect`: transformar pedido aberto em prompt tecnico executavel.
4. `zipai-optimizer`: filtrar contexto, limitar exploracao e evitar gasto inutil de tokens.
5. Skills de contexto: coletar so o necessario, salvar estado e restaurar continuidade.
6. Skills de prompt: reduzir ambiguidade, melhorar instrucoes e evitar retrabalho.
7. Skills de saida: organizar e limpar a entrega final.

## Estrutura

### 00-core

- `find-skills`: roteamento e descoberta de skills relevantes.
- `i-have-adhd`: resposta objetiva, numerada e orientada a acao.
- `devpromptarchitect`: arquitetura de prompt tecnico para tarefas complexas.
- `dev-prompt-architect`: variante compativel do arquiteto de prompt.

### 10-token-economy

- `zipai-optimizer`: otimizacao adaptativa de tokens, contexto e saida.
- `context-optimization`: compressao, mascaramento, cache e particionamento.
- `context-compression`: compactacao orientada a tokens por tarefa.
- `prompt-caching`: reaproveitamento de prefixos e padroes estaveis.
- `concise-planning`: planejamento atomico e enxuto.
- `caveman`: modo de comunicacao ultra comprimido quando fizer sentido.

### 20-context-engineering

- `context-window-management`: gestao de janela de contexto e degradacao.
- `context-guardian`: preservacao de contexto critico antes de compactacao.
- `context-fundamentals`: fundamentos de contexto.
- `context-driven-development`: desenvolvimento guiado por contexto real.
- `context-management-context-save`: salvar estado util de uma sessao.
- `context-management-context-restore`: restaurar estado util em outra sessao.

### 30-prompt-engineering

- `llm-prompt-optimizer`: melhorar prompts, reduzir alucinacao e cortar tokens.
- `prompt-engineering`: tecnicas gerais de engenharia de prompt.

### 40-output-quality

- `bulletmind`: estruturar respostas, notas e resumos em bullets claros.
- `unslop`: remover vicios de texto gerado por IA antes de publicar.

## Receita pronta para usar com colegas

```text
Use as skills da pasta Ultra Tokens em conjunto:

1. Comece com find-skills para localizar skills relevantes.
2. Use i-have-adhd para manter comunicacao curta, numerada e acionavel.
3. Use devpromptarchitect para transformar o pedido em instrucao tecnica clara.
4. Use zipai-optimizer, context-optimization, context-compression e prompt-caching para reduzir tokens por tarefa.
5. Use context-guardian, context-save e context-restore quando a tarefa for longa ou houver risco de perder contexto.
6. Use llm-prompt-optimizer e prompt-engineering para melhorar prompts.
7. Use bulletmind e unslop para entregar uma resposta final organizada e limpa.

Priorize contexto real, comandos reais, validacao objetiva e economia de tokens.
Nao declare sucesso sem evidencia.
Nao invente estado, teste, build, deploy ou comportamento.
```

## Criterio de qualidade

Uma boa execucao com este pacote deve terminar com:

- objetivo entendido;
- contexto minimo suficiente coletado;
- decisoes importantes preservadas;
- validacao real informada;
- riscos e limites declarados;
- entrega final clara, curta e acionavel.
