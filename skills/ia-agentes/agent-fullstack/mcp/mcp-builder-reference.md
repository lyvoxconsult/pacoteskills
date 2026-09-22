# MCP Builder - Criar Servidores MCP

## Visão Geral

Skill para criar servidores MCP (Model Context Protocol) para integrar ferramentas customizadas.

## Referência

- Skill oficial: `anthropics/mcp-builder`
- URL: https://officialskills.sh/anthropics/skills/mcp-builder

## Como Criar MCP Server

### 1. Instalar

```bash
npm install @anthropic/mcp-sdk
```

### 2. Criar Servidor

```typescript
import { MCPServer } from '@anthropic/mcp-sdk'

const server = new MCPServer({
  name: 'my-tool',
  version: '1.0.0',
  tools: [
    {
      name: 'query-db',
      description: 'Executar query no banco',
      inputSchema: {
        type: 'object',
        properties: {
          sql: { type: 'string', description: 'Query SQL' }
        },
        required: ['sql']
      }
    }
  ],
  async handleTool(tool, args) {
    if (tool.name === 'query-db') {
      return { content: [{ type: 'text', text: await db.query(args.sql) }] }
    }
  }
})

server.run()
```

### 3. Configurar

```json
// claude.settings.json
{
  "mcpServers": {
    "my-tool": {
      "command": "node",
      "args": ["path/to/server.js"]
    }
  }
}
```

## Ferramentas Customizadas para o Projeto

### Exemplo: Supabase Tool

```typescript
{
  name: 'supabase-query',
  description: 'Executar query no Supabase',
  inputSchema: {
    type: 'object',
    properties: {
      table: { type: 'string' },
      filters: { type: 'object' },
      limit: { type: 'number', default: 100 }
    }
  }
}
```

### Exemplo: CTR Generator

```typescript
{
  name: 'generate-ctr',
  description: 'Gerar número CTR',
  inputSchema: {
    type: 'object',
    properties: {
      customerId: { type: 'string' },
      rentalId: { type: 'string' }
    }
  }
}
```

## Integração com Agente

### Adicionar ao Agente

```bash
# No archivo claude.settings.json
{
  "mcpServers": {
    "obsidian": {
      "command": "node",
      "args": ["path/to/obsidian-mcp.js"]
    },
    "supabase": {
      "command": "node", 
      "args": ["path/to/supabase-mcp.js"]
    }
  }
}
```

## Checklist

- [ ] Ferramenta bem documentada
- [ ] Input validation
- [ ] Error handling
- [ ] Logging
- [ ] Tests

## Regra

> MCP = forma padronizada de criar tools. Segue o padrão.