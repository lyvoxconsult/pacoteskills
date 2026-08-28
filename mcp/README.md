# MCP Catalog

Inventario saneado do ambiente para replicacao em outras maquinas.

Escopo:
- `plugins.md`: plugins habilitados no Codex
- `mcp-servers.md`: servidores MCP ativos e desabilitados
- `connections.md`: conexoes, autenticacao, approvals e observacoes de portabilidade
- `config-templates/`: templates sem segredos para Windows e macOS

Regras:
- nao versionar tokens, api keys, cookies ou headers secretos
- usar placeholders para paths locais e credenciais
- tratar este diretório como catalogo de referencia, nao como dump bruto da config local

Fonte desta captura:
- ambiente local auditado em `2026-08-28`
- origem operacional: `C:\Users\pedro\.codex\config.toml`
