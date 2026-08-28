# Stack Catalog

Este diretório complementa `skills/` e `mcp/` com documentação de frameworks, runtimes e ferramentas de base para configurar novas máquinas de trabalho.

## Regras deste catálogo

- Não versionar segredos, tokens, chaves ou credenciais.
- Não usar caminhos absolutos de uma máquina específica.
- Documentar de forma neutra para macOS, Windows e Linux.
- Separar claramente:
  - baseline recomendado;
  - ferramentas opcionais;
  - ferramentas observadas na máquina auditada.

## Estrutura

- `foundations.md`: critérios de baseline e política de documentação.
- `languages-and-runtimes.md`: linguagens, runtimes e gerenciadores.
- `dev-tools.md`: ferramentas de desenvolvimento e automação local.
- `infra-and-containers.md`: containers, virtualização e infraestrutura local.
- `config-templates/tooling-checklist.md`: checklist para provisionar uma nova máquina.

## Escopo

O objetivo aqui não é instalar nada automaticamente. O objetivo é registrar o stack importante para que outro agente consiga:

1. clonar o repositório;
2. entender o ambiente desejado;
3. instalar apenas o que faz sentido;
4. validar a configuração sem depender de caminhos ou segredos locais.
