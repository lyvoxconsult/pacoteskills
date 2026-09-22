# Playwright - Automação de Browser para E2E

## Visão Geral

Skill para automação de browser com Playwright, para testes E2E de fluxos críticos da aplicação.

## Instalação

```bash
# No projeto
npm init playwright@latest
# ou
npm install -D @playwright/test playwright
npx playwright install chromium
```

## Configuração

### playwright.config.ts
```typescript
import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
  ],
})
```

### Estrutura de Tests
```
tests/e2e/
├── auth/
│   ├── login.spec.ts
│   └── oauth.spec.ts
├── rentals/
│   ├── create-rental.spec.ts
│   └── workflow.spec.ts
└── map/
    └── marker-interaction.spec.ts
```

## Fluxos Críticos para Testar

### 1. Autenticação
- Login com email/senha
- OAuth (Google, GitHub)
- Logout
- Sessão expira

### 2. Fluxo de Locação
- Criar nova locação
- Editar locação
- Cancelar locação
- Status muda automaticamente

### 3. Mapa
- Marcadores carregam
- Popup abre/fecha
- Localização atual funciona
- Busca de endereço

### 4. CTR
- Gerar número CTR
- Emitir CTR (PDF)
- Download CTR

## Exemplo de Teste

```typescript
import { test, expect } from '@playwright/test'

test('login with email', async ({ page }) => {
  await page.goto('/login')
  
  await page.fill('[name=email]', 'user@test.com')
  await page.fill('[name=password]', 'password123')
  await page.click('button[type=submit]')
  
  await expect(page).toHaveURL('/mapa')
  await expect(page.locator('[data-testid=user-menu]')).toBeVisible()
})
```

## Commands Úteis

```bash
# Rodar todos os E2E
npm run test:e2e

# Rodar em modo UI
npx playwright test --ui

# Rodar com trace
npx playwright test --trace on

# Gerar boilerplate
npx playwright codegen
```

## Integração com TDD

1. **Criar teste E2E primeiro** (RED)
2. **Implementar funcionalidade** (GREEN)
3. **Refatorar mantendo testes** (REFACTOR)
4. **Adicionar à suíte de regressão**

## Regra de Ouro

> Fluxos críticos = Playwright. Lógica de negócio = Jest/Vitest.