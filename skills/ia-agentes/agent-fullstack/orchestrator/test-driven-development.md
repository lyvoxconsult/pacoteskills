# Test-Driven Development (TDD)

## Visão Geral

Este skill força o TDD: gerar testes ANTES da implementação, guiando todo o fluxo de desenvolvimento.

## Workflow TDD

### 1. Red - Escrever teste que falha

```typescript
// Primeiro: escrever o teste descrevendo comportamento desejado
describe('AuthService', () => {
  it('should login with valid credentials', async () => {
    const result = await authService.login('user@test.com', 'password123')
    expect(result.user).toBeDefined()
    expect(result.token).toBeDefined()
  })
})
```

### 2. Green - Implementar o mínimo

```typescript
// Segundo: implementar o mínimo para teste passar
async login(email: string, password: string) {
  const user = await db.users.find({ email })
  if (!user || user.password !== hash(password)) {
    throw new Error('Invalid credentials')
  }
  return { user, token: generateToken(user.id) }
}
```

### 3. Refactor - Melhorar código

```typescript
// Terceiro: refatorar mantendo testes passando
async login(email: string, password: string) {
  const user = await this.findUserByEmail(email)
  if (!user || !await this.verifyPassword(user, password)) {
    throw new AuthError('Invalid credentials')
  }
  return this.createSession(user)
}
```

## Regras TDD

### Para Features Novas

1. **Criar testes primeiro**
   - Unit tests para lógica de negócio
   - Integration tests para fluxos
   - E2E tests para jornadas críticas

2. **Rodar testes ANTES de implementar**
   - Testes devem falhar (Red)
   - Isso define o comportamento esperado

3. **Implementar mínimo necessário**
   - Apenas código para testes passarem
   - Não otimizar prematuramente

4. **Refatorar com segurança**
   - Testes existentes como rede de segurança
   - Novos testes para comportamento desejado

### Para Refatoração

1. **Testes de caracterização PRIMEIRO**
   - Escrever testes que documentam comportamento ATUAL
   - Validar que passam antes de mudar anything

2. **Refatorar aos poucos**
   - Small steps
   - Testes passando a cada passo

3. **Novos testes para estado desejado**
   - Adicionar testes para novos comportamentos
   - Manter testes antigos se ainda relevantes

## Configuração de Testing

### Scripts npm
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:e2e": "playwright test"
  }
}
```

### Bibliotecas
- **Jest** ou **Vitest** - Unit/Integration tests
- **Testing Library** - Component tests
- **Playwright** - E2E tests

## Dica

> "Escreva testes que falham primeiro. O teste é a especificação."

Se não conseguir escrever o teste, é porque não entende bem o problema.