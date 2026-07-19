# Verification Before Completion - Validação Obrigatória

## Visão Geral

Skill para validar o trabalho antes de concluir qualquer tarefa:
- Verificações técnicas
- Sanity checks
- Checklist de qualidade
- Auditoria de segurança

## Ejecutar Antes de Finalizar

### Checklist Obrigatório

1. **Build succeeds**
   ```bash
   npm run build
   ```
   - Sem erros de Typescript
   - Sem warnings críticos

2. **Lint passing**
   ```bash
   npm run lint
   ```
   - Sem erros de lint
   - Código formatado

3. **Testes passando**
   ```bash
   npm test
   # ou
   npm run test:ui
   ```
   - Unit tests passando
   - Integration tests passando

4. **Segurança OK**
   - Nenhum secret em código
   - Input validation presente
   - Auth/Authorization verificado

5. **Documentação atualizada**
   -Notas do Obsidian criadas/atualizadas
   -README ou inline docs presentes
   -TipoScript types documentados

### Validações de Código

6. **Qualidade de código**
   - Nomes claros e consistentes
   - Funções pequenas (< 50 linhas)
   - Sem código duplicado
   - Tratamento de erros presente

7. **Padrões do projeto**
   - Segue estrutura de diretórios
   - Naming convention respeitado
   - Imports organizados

### Validações de Arquitetura

8. **Arquitetura**
   - Separação de concerns respeitada
   - Camadas não violadas
   - Dependencies injeção usada

9. **Estado**
   - State management apropriado
   - Não há estado redundante
   - Cleanup em unmount

### Validações de UI/UX

10. **Interface**
    - Responsivo
    - Acessível (contrast, keyboard)
    - Loading states presentes
    - Error states presentes

## Fluxo de Verificação

```
1. Executar npm run build
   ↓
2. Executar npm run lint
   ↓
3. Executar testes
   ↓
4. Executar auditoria de segurança
   ↓
5. Verificar documentação Obsidian
   ↓
6. Revisar código manualmente
   ↓
7. Checklist completo → Concluir
```

## Quando Encontrar Problemas

1. **Build fail** → Corrigir erros antes de continuar
2. **Lint fail** → Corrigir ou documentar exception
3. **Teste fail** → Corrigir ou criar ticket
4. **Segurança fail** → Bloquear e documentar
5. **Docs fail** → Criar documentação

## Regra de Ouro

> **NUNCA** marque uma tarefa como "concluída" sem executar todas as verificações acima.
> Se algo falhar, corrija ou crie um follow-up ticket.