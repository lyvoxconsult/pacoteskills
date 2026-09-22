# AIAssist - Agente Context-Aware com RAG

## Visão Geral

Agente de código context-aware com suporte a:
- RAG (Retrieval Augmented Generation)
- Tree-sitter para parsing
- Unified Diff
- Code Blocks e Search-Replace

## Referência

Repositório: https://github.com/mehdihadeli/AIAssist

## Como Usar

### 1. Carregar Contexto do Projeto

Antes de modificar código:
```bash
# Usar glob para encontrar arquivos relevantes
glob pattern="**/features/**/*"

# Usar grep para buscar código relacionado
grep pattern="useAuth" include="*.ts"
```

### 2. Analisar Múltiplos Arquivos

```bash
# Ler arquivos relacionados
read filePath="src/features/auth/types.ts"
read filePath="src/features/auth/hooks.ts"
read filePath="src/infrastructure/supabase/auth.ts"
```

### 3. Gerar Plano de Alteração

Ao analisar contexto, criar:
1. Lista de arquivos a modificar
2. Dependências entre módulos
3. Pontos de atenção (breaking changes)
4. Testes necessários

### 4. Aplicar Mudanças com Diff

Para cada alteração:
```diff
-// Código antigo
+// Código novo
```

## Configuração Recomendada

### tree-sitter Languages
```json
{
  "languages": ["typescript", "tsx", "javascript", "json"]
}
```

### RAG Configuration
- Indexar: `.ts`, `.tsx`, `.md`
- Excluir: `node_modules`, `.next`, `dist`

## Integração com Agente

### Workflow
1. Receber tarefa
2. Ler arquivos relacionados (glob/grep)
3. Analisar estrutura (read múltiplos)
4. Gerar plano deの変更
5. Aplicar com diffs revisáveis
6. Criar/atualizar testes
7. Documentar no Obsidian

## Regra de Ouro

> **SEMPRE** carregar contexto antes de modificar código.

Não fazer mudanças sem entender:
- O que o código atual faz
- Como se relaciona com outros módulos
- Quais são as dependências
- Quais testes precisam existir