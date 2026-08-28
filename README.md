# pacoteskills

Repositório de catálogo e distribuição de ambiente para agentes, skills, MCPs e stack complementar de desenvolvimento.

## Objetivo

Este repositório existe para centralizar o que precisa ser replicado com segurança em outras máquinas, como macOS, Windows e Linux:

- skills locais;
- skills obrigatórias e seus critérios de uso;
- catálogo de MCPs, plugins e conexões;
- documentação complementar de runtimes, frameworks e ferramentas-base.

O foco é permitir que outro agente ou outra máquina consigam reconstruir o ambiente com menos atrito e sem depender de caminhos locais, segredos ou anotações espalhadas.

## Estrutura

- `skills/`: catálogo principal de skills disponíveis.
- `skills obrigatorias/`: definição do pack obrigatório, manifestos e documentação operacional.
- `mcp/`: inventário de servidores MCP, plugins, conexões e templates de configuração.
- `stack/`: documentação complementar de runtimes, frameworks e ferramentas importantes.
- `graphify-out/`: artefatos locais de apoio à exploração estrutural do repositório quando gerados.

## O que este repositório documenta

- quais skills devem existir no ambiente;
- quais skills são obrigatórias por padrão;
- quais ferramentas MCP e plugins fazem parte do setup;
- quais runtimes e ferramentas de base vale validar em uma nova máquina;
- como manter o setup portável entre sistemas operacionais.

## O que este repositório nao deve conter

- segredos, tokens, chaves ou credenciais;
- caminhos absolutos de uma máquina específica;
- instruções destrutivas sem necessidade;
- resíduos de projetos fora de escopo;
- dependências de ferramentas pagas sem necessidade clara.

## Uso esperado

Fluxo típico para provisionar outro ambiente:

1. clonar este repositório;
2. revisar `skills obrigatorias/README.md`;
3. revisar `mcp/README.md`;
4. revisar `stack/README.md`;
5. instalar e configurar somente o que for pertinente ao host e ao trabalho;
6. validar o ambiente com checagens simples de versão, autenticação e disponibilidade.

## Regras de manutenção

- manter documentação neutra para macOS, Windows e Linux;
- registrar apenas o que é importante para reprodução do ambiente;
- distinguir baseline recomendado de estado apenas observado em uma máquina auditada;
- evitar duplicação desnecessária entre skills, MCPs e stack;
- limpar referências locais sensíveis antes de commitar.

## Estado atual

Em 2026-08-28, o repositório foi organizado para funcionar como fonte única de sincronização de:

- skills;
- skills obrigatórias;
- MCPs, plugins e conexões;
- stack complementar de desenvolvimento.
