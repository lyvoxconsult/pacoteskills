# Languages And Runtimes

## Baseline recomendado

| Item | Papel | Prioridade | Observado na maquina auditada |
| --- | --- | --- | --- |
| Node.js | base para CLIs, MCPs, automações e ecossistema JS/TS | alta | sim |
| npm | gerenciador padrão do ecossistema Node.js | alta | sim |
| pnpm | gerenciador eficiente para monorepos e projetos modernos | alta | sim |
| Python | scripts, automação, utilitários e tooling auxiliar | alta | nao confirmado via comando `python` |
| uv | gerenciamento moderno de ambientes e pacotes Python | media-alta | sim |

## Complementares importantes

| Item | Papel | Prioridade | Observado na maquina auditada |
| --- | --- | --- | --- |
| Bun | runtime e toolkit JS/TS alternativo | media | nao |
| Java | necessario em projetos e ferramentas especificos | media | nao auditado |
| Go | util para CLIs, infraestrutura e ferramentas modernas | media | nao auditado |
| Rust | relevante para tooling, CLIs e componentes de alta performance | media | nao auditado |

## Notas

### Node.js

- Importante para MCPs, Playwright, ferramentas de build e muitos scripts de skill.
- Estado observado: `v24.14.0`.

### npm

- Necessario como baseline, mesmo quando `pnpm` for o padrao do projeto.
- Estado observado: `11.9.0`.

### pnpm

- Recomendado como complemento padrao do stack Node.js.
- Estado observado: `11.9.0`.

### Python

- Deve continuar documentado como item importante de baseline.
- Na maquina auditada em 2026-08-28, o comando `python --version` nao confirmou uma instalacao funcional pelo alias `python`.
- Isso significa que Python e importante no catalogo, mas nao ficou provado neste host pela verificacao executada.

### uv

- Relevante para ambientes Python reproduziveis com menos atrito.
- Estado observado: `0.10.8`.

### Bun

- Nao e obrigatorio para este pacote.
- Pode ser habilitado em maquinas que usam projetos JS/TS com foco em performance de tooling.
