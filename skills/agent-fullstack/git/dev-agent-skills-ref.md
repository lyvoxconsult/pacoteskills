# Dev Agent Skills - Git/GitHub

## Visão Geral

Skills para fluxo Git e GitHub:
- Commits atômicos
- PRs estruturados
- Code reviews

## Referência

Repositório: https://github.com/fvadicamo/dev-agent-skills

## Commits Atômicos

### Formato de Mensagem

```
tipo(scope): descrição curta

- Detalhe 1
- Detalhe 2
```

### Tipos de Commit

| Tipo | Descrição |
|------|-----------|
| `feat` | Nova funcionalidade |
| `fix` | Bug fix |
| `refactor` | Refatoração (sem mudança comportamento) |
| `perf` | Otimização de performance |
| `test` | Adicionar/atualizar testes |
| `docs` | Documentação |
| `chore` | Tarefas de manutenção |
| `style` | Formatação (sem mudança código) |
| `ci` | Mudanças em CI/CD |

### Regras

1. **Um commit = uma mudança lógica**
   - Não misturar features com fixes
   -Não misturar refactor com funcionalidade

2. **Mensagens claras**
   - "fix auth" → "fix: corrigir redirect após login OAuth"
   - "add test" → "test: adicionar testes para AuthService.login"

3. **Commits pequenos**
   - máximo ~400 caracteres total
   - Se maior, dividir em múltiplos commits

## Pull Requests

### Template de PR

```markdown
## Sumário
[Breve descrição da mudança]

## Contexto
- Issue: [link]
--decisão: [link ADR se aplicável]

## Mudanças
- [ ] Mudança 1
- [ ] Mudança 2

## Fluxo de Teste
1. Passo 1
2. Passo 2
3. Resultado esperado

## Riscos
- Risco 1: [descrição] → Mitigação: [como]

## Breaking Changes
- [ ] Cambio 1 → Migração: [como]

## Checklist
- [ ] Build passando
- [ ] Testes passando
- [ ] Lint passando
- [ ] Segurança OK
- [ ] Docs atualizadas

## Screenshots
[Se aplicável]
```

### Fluxo de PR

1. **Criar branch** (se não existir)
   ```bash
   git checkout -b feat/nome-da-feature
   ```

2. **Commits pequenos**
   ```bash
   git add src/feature/types.ts
   git commit -m "feat(auth): add types for OAuth providers"
   
   git add src/feature/
   git commit -m "feat(auth): implement OAuth login flow"
   ```

3. **Push e PR**
   ```bash
   git push -u origin feat/nome-da-feature
   gh pr create --title "..." --body "..."
   ```

4. **Atualizar com Reviews**
   ```bash
   git add .
   git commit -m "fix: responder feedback"
   git push
   ```

## Code Review

### Para Revisor

- Ser construtivo
- Explicar o "por quê"
- Sugerir alternativas
- Aprovar ou requerer mudanças

### Para Autor

- Responder todos os comentários
- Não tomar como pessoal
- Explorar quando discordar
- Atualizar basedo em feedback

## Regras de Ouro

> Commits atômicos = PRs pequenos = Reviews rápidas = Ship mais rápido