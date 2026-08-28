# Tooling Checklist

Use este checklist ao configurar uma nova maquina.

## 1. Baseline minimo

- Git instalado e funcional
- Node.js instalado
- npm funcional
- pnpm instalado
- Python instalado e chamavel pelo terminal
- uv instalado
- Docker instalado e funcional

## 2. Validacoes simples

Executar e registrar as versoes efetivas:

- `git --version`
- `node --version`
- `npm --version`
- `pnpm --version`
- `python --version`
- `uv --version`
- `docker --version`

## 3. Complementares recomendados

- validar disponibilidade de `npx`
- instalar `ripgrep` para exploracao de codigo
- instalar Playwright CLI quando houver fluxo de UI ou E2E
- avaliar Bun apenas se houver projetos que realmente dependam dele

## 4. Regras de higiene

- nao salvar tokens em arquivos versionados;
- preferir variaveis de ambiente ou autenticacoes nativas do agente;
- nao documentar caminhos locais como padrao global;
- registrar apenas ferramentas relevantes para reproducao do ambiente.
