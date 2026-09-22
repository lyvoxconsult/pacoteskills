# Insecure Defaults - Detectar Configurações Inseguras

## Visão Geral

Detectar configurações inseguras como:
- Secrets hardcoded
- Credenciais padrão
- Criptografia fraca
- Flags de debug em produção

##扫描

### 1. Secrets em Código

```bash
# Procurar secrets
grep -r "password\s*=" --include="*.ts" src/
grep -r "apiKey\s*=" --include="*.ts" src/
grep -r "secret\s*=" --include="*.ts" src/

# Usar semgrep
semgrep --config=p/secrets ./src
```

### 2. Credenciais Padrão

```typescript
// BAD
const DB_PASSWORD = 'admin'
const API_KEY = '123456'

// GOOD
const DB_PASSWORD = process.env.DB_PASSWORD
```

### 3. Debug Flags

```typescript
// BAD (produção)
const DEBUG = true
app.use(hotMiddleware)

// GOOD
const DEBUG = process.env.NODE_ENV !== 'production'
```

## Common Insecure Patterns

### Auth

```typescript
// BAD - sem validation
async function login(email, password) {
  return db.users.find({ email, password })
}

// GOOD - com validation
import { z } from 'zod'
const LoginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
})
async function login(data) {
  const { email, password } = LoginSchema.parse(data)
  // ...
}
```

### Error Handling

```typescript
// BAD - expõe detalhes
catch (e) {
  res.status(500).json({ error: e.stack })
}

// GOOD - mensagem genérica
catch (e) {
  log.error(e)
  res.status(500).json({ error: 'Internal server error' })
}
```

### Criptografia

```typescript
// BAD
crypto.createHash('md5')
crypto.createCipher('aes-128-cbc')

// GOOD
crypto.createHash('sha256')
crypto.createCipheriv('aes-256-gcm', key, iv)
```

## Checklist

- [ ] Nenhum secret hardcoded
- [ ] Credenciais de default removidas
- [ ] Debug flag off em produção
- [ ] Error messages genéricas
- [ ] strong crypto digunakan
- [ ] Dependencies atualizadas

## Regra

> Defaults inseguros = vulnerabilidades. Sempre verificar.