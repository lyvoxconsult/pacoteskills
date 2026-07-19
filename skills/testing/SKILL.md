# TESTING_SKILL

Skill especializada em testes automatizados, TDD e BDD.

## Repositórios de Referência

- **Jest**: https://github.com/jestjs/jest
- **Playwright**: https://github.com/microsoft/playwright
- **Pytest**: https://github.com/pytest-dev/pytest

## Capacidades

### 1. Jest (JavaScript/TypeScript)
- Configurar Jest para projetos JS/TS
- Escrever testes unitários com Jest
- Usar Jest mocking (jest.fn, jest.spyOn, jest.mock)
- Configurar coverage reports
- Implementar testes de snapshot
- Configurar setupFiles e teardown

### 2. Playwright (E2E Testing)
- Configurar Playwright para testes E2E
- Escrever testes end-to-end robustos
- Usar locators para seleção de elementos
- Configurar screenshots e videos
- Implementar testes em múltiplos browsers
- Configurar parallel execution

### 3. Pytest (Python)
- Configurar Pytest para projetos Python
- Escrever testes com fixtures
- Usar parametrização de testes
- Implementar fixtures complexas
- Configurar plugins (pytest-cov, pytest-mock)
- Criar markers customizados

### 4. Estratégias de Teste
- **TDD**: Test Driven Development
- **BDD**: Behavior Driven Development com Gherkin
- **Test Pyramid**: Unit, Integration, E2E
- **Arrange-Act-Assert**: Padrão AAA
- **Given-When-Then**: Padrão BDD

## Boas Práticas de Testes

### Nomenclatura
```javascript
describe('Calculator', () => {
  it('should add two numbers correctly', () => {})
  it('should throw error when dividing by zero', () => {})
})
```

### Estrutura AAA
```javascript
test('should calculate total with tax', () => {
  // Arrange
  const price = 100;
  const taxRate = 0.1;

  // Act
  const total = calculateTotal(price, taxRate);

  // Assert
  expect(total).toBe(110);
});
```

### Mocks e Stubs
```javascript
jest.mock('./api');
const mockApi = require('./api');
mockApi.fetchUser.mockResolvedValue({ id: 1, name: 'Test' });
```

## Ferramentas Complementares

- **@testing-library/react**: Testing de componentes React
- **MSW**: Mock Service Worker para API mocking
- **Faker**: Geração de dados fake
- **Wallaby.js**: Test running em tempo real

## Quando Usar

Use esta skill quando:
- Precisa configurar suíte de testes do zero
- Precisa escrever testes unitários ou E2E
- Precisa implementar TDD em um projeto
- Precisa configurar CI para rodar testes
- Precisa fazer debugging de testes falhando
- Precisa configurar coverage reports