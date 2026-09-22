# DOCX Generator - Documentação em Word

## Visão Geral

Skill para gerar documentação técnica em formato Word (.docx).

## Referência

- Skill oficial: `anthropics/docx`
- URL: https://officialskills.sh/anthropics/skills/docx

## Como Usar

### 1. Instalar cliente

```bash
npm install docx
```

### 2. Criar Documento

```typescript
import { Document, Packer, Paragraph, TextRun } from 'docx'

const doc = new Document({
  sections: [{
    properties: {},
    children: [
      new Paragraph({
        children: [
          new TextRun({ text: "Título do Documento", bold: true, size: 48 }),
        ],
      }),
      new Paragraph({
        children: [
          new TextRun({ text: "Descrição...", size: 24 }),
        ],
      }),
    ],
  }],
})

const buffer = await Packer.toBuffer(doc)
```

## Templates

### Technical Spec

```markdown
# Technical Specification: [Feature Name]

## Overview
[Breve descrição]

## Requirements
- Requisito 1
- Requisito 2

## Architecture
[Diagrama se aplicável]

## API
### Endpoint 1
- Input: [schema]
- Output: [schema]

## Security
[Considerações]

## Testing
[Testes necessários]
```

### RFC Document

```markdown
# RFC: [Número] - [Título]

## Summary
[Resumo executivo]

## Motivation
[Por que isso é necessário]

## Detailed Design
[Especificação completa]

## Alternatives
[Alternativas consideradas]

## Open Questions
[Questões abertas]
```

### QA Report

```markdown
# QA Report: [Feature/Test]

## Test Scope
[Escopo]

## Test Results
| ID | Test | Status | Notes |
|----|------|--------|-------|
| 1 | Login | ✅ | |

## Coverage
[Percentual]

## Issues Found
[Issues]

## Sign-off
[Status final]
```

## Checklist

- [ ] Usar template adequado
- [ ] Heading hierarchy clara
- [ ] Tabelas quando apropriado
- [ ] Screenshots quando útil
- [ ] Versionar no Obsidian

## Regra

> Documentação boa = searchable = versionada = mantém-se.