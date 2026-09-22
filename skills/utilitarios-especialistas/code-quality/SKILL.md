# CODE_QUALITY_SKILL

Skill especializada em linting, formatação e análise de qualidade de código.

## Repositórios de Referência

- **ESLint**: https://github.com/eslint/eslint
- **Prettier**: https://github.com/prettier/prettier
- **SonarQube**: https://github.com/SonarSource/sonarqube

## Capacidades

### 1. ESLint (JavaScript/TypeScript)
- Configurar regras de linting para projetos JS/TS
- Integrar ESLint com editors e IDEs
- Criar regras customizadas
- Configurar extends e plugins
- Implementar autofix em saves

### 2. Prettier (Formatação)
- Configurar Prettier para formatação consistente
- Definir padrões de formatação (single quote, semicolons, etc.)
- Integrar Prettier com ESLint
- Configurar Prettier para diferentes linguagens

### 3. SonarQube (Análise de Qualidade)
- Configurar análise estática com SonarQube
- Interpretar métricas de qualidade
- Definir quality gates
- Analisar dívida técnica
- Configurar regras específicas por linguagem

### 4. Qualidade de Código
- Verificar complexidade ciclomática
- Identificar code smells
- Analisar cobertura de código
- Detectar código duplicado
- Avaliar manutenibilidade

## Regras de Qualidade

### JavaScript/TypeScript
```javascript
// .eslintrc.js
module.exports = {
  extends: ['eslint:recommended', 'plugin:@typescript-eslint/recommended'],
  rules: {
    'no-console': 'warn',
    'no-unused-vars': 'error',
    'prefer-const': 'error'
  }
}
```

### Prettier Config
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80
}
```

## Integração CI/CD

- Executar ESLint no pre-commit hook
- Rodar Prettier --check no CI
- Integrar SonarQube no pipeline
- Bloquear merge se quality gates falharem

## Quando Usar

Use esta skill quando:
- Precisa configurar linting em um novo projeto
- Precisa padronizar formatação de código
- Precisa configurar análise de qualidade no CI
- Precisa revisar code smells e dívida técnica
- Precisa criar configuration files de linting/formatting