# Executing Plans - Decompor Tarefas em Planos Executáveis

## Visão Geral

Skill para decompor tarefas complexas em plano executável step-by-step, garantindo:
- Clareza nos passos
- Identificação de dependências
- Critérios de sucesso
- Validações intermediárias

## Como Usar

### 1. Entender a Tarefa

Antes de criar o plano:
- Ler contexto do Obsidian (notas relacionadas)
- Ler contexto do código (arquivos relevantes)
- Identificar dependências externas
- Verificar restrições e SLAs

### 2. Decompor em Passos

Estrutura do plano:
```
## Plano: [Nome da Tarefa]

### Contexto
[Breve descrição do que precisa ser feito]

### Passos
1. [Passo inicial]
   - Sub-passos se necessário
   - Dependências: [Liste aqui]
   
2. [Passo seguinte]
   - Sub-passos...
   - Dependências: [Passo 1, outro recurso]

### Critérios de Sucesso
- [ ] Item verificado 1
- [ ] Item verificado 2

### Riscos Identificados
- Risco 1: [Descrição] → Mitigação: [Como evitar]

###rollback
[Plano de rollback se algo der errado]
```

### 3. Executar Passo a Passo

Para cada passo:
1. Executar o passo
2. Validar resultado
3. Documentar no Obsidian
4. Passar para próximo passo

### 4. Validar Resultado Final

Após executar todos os passos:
- Verificar cada item de critérios de sucesso
- Executar verificação final (verification-before-completion)
- Atualizar documentação no Obsidian

## Exemplo Prático

```
## Plano: Adicionar autenticação OAuth

### Contexto
Adicionar login social (Google, GitHub) via Supabase Auth

### Passos
1. Configurar OAuth providers no Supabase
   - Criar credenciais no Google Console
   - Adicionar configuracoes em site Supabase
   
2. Implementar client OAuth
   - Instalar @supabase/ssr
   - Criar auth-hooks.ts
   - Dependências: passo 1

3. Criar componentes de UI
   - Login button component
   - Auth callback page
   - Dependências: passo 2

### Critérios de Sucesso
- [ ] Login Google funciona
- [ ] Login GitHub funciona
- [ ] Logout funciona
- [ ] Sessão persiste

### Riscos
- Rate limit → Implementar retry com backoff
- Credenciais erradas → Validar em staging primeiro