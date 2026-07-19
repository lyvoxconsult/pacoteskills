# Obsidian MCP - Integração com Obsidian

## Visão Geral

Integração com Obsidian via:
- **obsidian-local-rest-api**: API REST local
- **MCP Server**: Servidor MCP

## Referência

- Obsidian MCP: https://github.com/MarkusPfundstein/mcp-obsidian
- Local REST API: https://github.com/coddingtonbear/obsidian-local-rest-api

## Instalação

### 1. obsidian-local-rest-api

No Obsidian:
1. Community Plugins → Buscar "obsidian-local-rest-api"
2. Instalar e ativar
3. Configurar porta (padrão: 27123)

### 2. Configurar no Agente

```bash
# Variáveis de ambiente
export OBSIDIAN_API_URL=http://localhost:27123
export OBSIDIAN_API_TOKEN=seu_token_aqui
export OBSIDIAN_VAULT_PATH=D:\Lyvox Core\Lyvox Core
```

## Como Usar

### 1. Buscar Notas

```bash
# GET /notes - Listar notas
curl -X GET http://localhost:27123/notes \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"

# GET /notes/{vault}/{note} - Ler nota
curl -X GET "http://localhost:27123/notes/Agente%20full%20stak/Bem-vindo" \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"
```

### 2. Criar Nota

```bash
# POST /notes - Criar nota
curl -X POST http://localhost:27123/notes \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "vault": "Agente full stak",
    "name": "Nova Nota",
    "content": "# Nova Nota\n\nConteúdo..."
  }'
```

### 3. Atualizar Nota

```bash
# PUT /notes/{vault}/{note} - Atualizar nota
curl -X PUT "http://localhost:27123/notes/Agente%20full%20stak/Nova%20Nota" \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "# Nova Nota Atualizada\n\nNuevo conteúdo..."
  }'
```

### 4. Buscar por Tags

```bash
# GET /tags/{vault} - Listar tags
curl -X GET "http://localhost:27123/tags/Agente%20full%20stak" \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"
```

### 5. search

```bash
# GET /search/{vault} - Buscar notas
curl -X GET "http://localhost:27123/search/Agente%20full%20stak?q=auth" \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"
```

## No Agente (Bash)

### Ler Nota

```bash
# Função helper
get_obsidian_note() {
  curl -s "http://localhost:27123/notes/$1/$2" \
    -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"
}

# Uso
get_obsidian_note "Agente full stak" "Arquitetura"
```

### Criar Nota

```bash
create_obsidian_note() {
  local vault=$1
  local name=$2
  local content=$3
  
  curl -s -X POST http://localhost:27123/notes \
    -H "Authorization: Bearer $OBSIDIAN_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d "{\"vault\":\"$vault\",\"name\":\"$name\",\"content\":\"$content\"}"
}
```

## Fluxo de Trabalho

1. **Antes de decidir**: Buscar notas relacionadas no Obsidian
2. **Após implementação**: Criar nota de feature/ADR/incidente
3. **Sempre**: Manter notas atualizadas com links de PR

## Regras

> Toda decisão de arquitetura = nota ADR no Obsidian.
> Todo incidente = nota com root cause e solução.
> Toda feature = nota com escopo e progresso.

## Templates no Obsidian

Ver: `templates/` directory