# Dev Tools

## Baseline recomendado

| Ferramenta | Papel | Prioridade | Observado na maquina auditada |
| --- | --- | --- | --- |
| Git | controle de versao e sincronizacao de repositorios | alta | sim |
| npx | execucao ad hoc de CLIs Node.js | alta | derivado de npm |
| terminal shell | execucao local de scripts e automacoes | alta | sim |

## Complementares importantes

| Ferramenta | Papel | Prioridade | Observado na maquina auditada |
| --- | --- | --- | --- |
| Playwright CLI | testes E2E e validacao real de UI | media-alta | nao auditado aqui |
| ripgrep | busca rapida em repositorios grandes | media-alta | nao auditado aqui |
| editor com suporte a Markdown | manutencao de skills, MCPs e notas | media | nao auditado aqui |

## Estado observado

- Git: `2.53.0.windows.1`
- O host auditado tinha ambiente de terminal funcional para Git e tooling Node.js.

## Notas

- `npx` entra como utilitario importante porque varias skills e ferramentas externas dependem dele.
- `ripgrep` e fortemente recomendado para exploracao de base e auditoria tecnica, mesmo quando nao for parte obrigatoria do setup minimo.
