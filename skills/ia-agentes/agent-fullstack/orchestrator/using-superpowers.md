# Using Superpowers - Capacidades Centrais do Ambiente

## Visão Geral

Habilita o uso das capacidades centrais do ambiente de desenvolvimento:
- Ferramentas de análise de código
- Execução de comandos
- Gerenciamento de arquivos
-Integração com Git
- Comunicação com Obsidian

## Ferramentas Disponíveis

### Análise de Código
- **glob**: Buscar arquivos por padrão (ex: `**/*.ts`)
- **grep**: Buscar conteúdo em arquivos
- **read**: Ler arquivos específicos
- **codesearch**: Buscar exemplos de APIs/libs

### Execução
- **bash**: Executar comandos no terminal
- **task**: Agentes especializados para tarefas complexas

### Edição
- **edit**: Editar arquivos existentes
- **write**: Criar Sobrescrever arquivos
- **webfetch**: Baixar conteúdo de URLs

### Integração
- **skill**: Carregar skills especializadas
- **supabase_***: Operações de banco de dados

## Como Usar

### 1. Explorar Código
```bash
# Listar todos os arquivos TypeScript
glob pattern="**/*.ts"

# Buscar função específica
grep pattern="useAuth" include="*.ts"
```

### 2. Executar Comandos
```bash
# Build do projeto
npm run build

# Lint
npm run lint

# Testes
npm test
```

### 3. Ler Contexto Primeiro
SEMPRE ler o contexto relevante antes de sugerir mudanças:
- Arquivos relacionados ao código a 修改ar
- Notas no Obsidian sobre decisões anteriores
- ADRs e runbooks existentes

### 4. Criar Plano
Decompor grandes tarefas em passos menores:
1. Análise inicial
2. Implementação
3.Testes
4.Documentação
5.Validação

## Regras de Ouro

1. **Nunca assumir** - Sempre verificar contexto antes de agir
2. **Sempre validar** - Rodar checks antes de concluir
3. **Documentar** - Criar/atualizar notas no Obsidian
4. **Testar** - Nunca shippar sem testes
5. **Revisar** - PRs estruturados com checklist