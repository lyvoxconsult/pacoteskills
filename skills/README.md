# Skills curadas

O arquivo canônico é [skills-manifest.json](skills-manifest.json). Ele registra o baseline operacional e seu estado observado; não autoriza instalação automática.

- Dez skills estavam disponíveis no ambiente consultado.
- `lyvox-core-reader` está ausente e exige criação/revisão antes de uso.
- `devpromptarchitect` é obrigatória quando acionada por prompt, arquitetura de prompt ou preparação de tarefa técnica.
- `skills-pack/` é referência histórica, não catálogo autorizado para cópia integral.

## Instalar apenas metadados

```bash
./skills/install-skills.sh --target /opt/lyvox/skills
```

## Sincronizar conteúdo revisado

```bash
./skills/sync-skills.sh --source "$HOME/.codex/skills"
cp skills/skills-approval.example /tmp/skills-approval
# preencher approved_by e selection_sha256 exibido no dry-run
./skills/sync-skills.sh --source "$HOME/.codex/skills" --approval /tmp/skills-approval --apply
```

O sync aceita somente nomes presentes no manifest com status disponível, exige `SKILL.md`, rejeita arquivos sensíveis e qualquer symlink. O hash de aprovação cobre o conteúdo selecionado e impede troca entre revisão e aplicação.

Catálogos por domínio: [global](global-skills.md), [frontend](frontend-skills.md), [backend](backend-skills.md), [design](design-skills.md), [database](database-skills.md), [DevOps](devops-skills.md), [QA](qa-skills.md), [security](security-skills.md) e [documentation](documentation-skills.md).
