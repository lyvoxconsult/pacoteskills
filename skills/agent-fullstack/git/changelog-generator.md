# Changelog Generator - Gerar Changelog de Commits

## Visão Geral

Skill para gerar changelog e release notes a partir de commits Git.

## Como Gerar Changelog

### 1. Collect Commits from Tag

```bash
# Todos os commits desde última release
git log --oneline v1.0.0..HEAD

# Commits com tipo
git log --oneline v1.0.0..HEAD --grep="feat"
git log --oneline v1.0.0..HEAD --grep="fix"
```

### 2. Parse Conventional Commits

```
tipo(scope): descrição
```

| Tipo | Categoria no Changelog |
|------|----------------------|
| `feat` | ✨ New Features |
| `fix` | 🐛 Bug Fixes |
| `perf` | ⚡ Performance |
| `refactor` | 🔨 Refactoring |
| `docs` | 📝 Documentation |
| `test` | ✅ Tests |
| `chore` | 🔧 Maintenance |

### 3. Generate Markdown

```markdown
# Changelog v1.1.0

## ✨ New Features
- Login com OAuth (Google, GitHub) (#45)
- Dark mode automático (#42)

## 🐛 Bug Fixes
- Corrigir redirect após logout (#44)
- Consistência de estado em formulários (#43)

## ⚡ Performance
- Otimizar render de markers no mapa (#41)

## 🔨 Refactoring
- Extrair AuthService para camada core (#40)
```

## Script Automation

### generate-changelog.sh

```bash
#!/bin/bash
TAG=${1:-$(git describe --tags --abbrev=0)}
CURRENT=$(git rev-parse HEAD)

echo "# Changelog ($TAG..$CURRENT)"

echo "## ✨ Features"
git log --pretty=format:"- %s" $TAG..$CURRENT --grep="feat"

echo "## 🐛 Fixes"
git log --pretty=format:"- %s" $TAG..$CURRENT --grep="fix"

echo "## ⚡ Performance"
git log --pretty=format="- %s" $TAG..$CURRENT --grep="perf"
```

## GitHub Releases

```bash
# Criar release no GitHub
gh release create v1.1.0 \
  --title "v1.1.0 - OAuth & Dark Mode" \
  --notes-file CHANGELOG.md
```

## Integração com Conventional Commits

### Commit Hook (pre-commit)

```yaml
# .commitlintrc.json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": ["feat", "fix", "docs", "style", "refactor", "test", "chore"]
  }
}
```

## Regras

1. Usar Conventional Commits
2. Commits atômicos = Changelog automático
3. Categorizar corretamente
4. Incluir PR numbers se possível