# PDF Generator - Documentação em PDF

## Visão Geral

Skill para gerar documentos PDF técnicos.

## Referência

- Skill oficial: `anthropics/pdf`
- URL: https://officialskills.sh/anthropics/skills/pdf

## Como Gerar PDF

### 1. Usando jsPDF (Já no projeto)

```typescript
import jsPDF from 'jspdf'
import autoTable from 'jspdf-autotable'

const doc = new jsPDF()

// Título
doc.setFontSize(20)
doc.text('Título', 20, 20)

// Corpo
doc.setFontSize(12)
doc.text('Descrição...', 20, 40)

// Tabela
autoTable(doc, {
  head: [['Col1', 'Col2']],
  body: [['A', 'B']],
  startY: 50,
})

doc.save('documento.pdf')
```

### 2. Usando @react-pdf/renderer (React)

```typescript
import { Document, Page, Text, View, StyleSheet } from '@react-pdf/renderer'

const styles = StyleSheet.create({
  page: { padding: 30 },
  title: { fontSize: 20, marginBottom: 20 },
  section: { marginBottom: 10 },
})

const MyDocument = () => (
  <Document>
    <Page size="A4" style={styles.page}>
      <Text style={styles.title}>Título</Text>
      <View style={styles.section}>
        <Text>Conteúdo...</Text>
      </View>
    </Page>
  </Document>
)
```

## Templates

### API Documentation

```markdown
# API Documentation

## Endpoints

### GET /api/resource
- Description: [desc]
- Auth: [required/none]
- Input: [params]
- Output: [schema]
```

### Runbook

```markdown
# Runbook: [Service]

## Alerts
| Alert | Severity | Action |
|-------|---------|--------|
| High CPU | Critical | Scale up |

## Troubleshooting
### Step 1
[ação]

### Step 2
[ação]
```

### Architecture Diagram

```markdown
# Architecture: [System]

## Components
- Component 1 → Component 2
- Component 2 → Database

## Data Flow
[fluxo]
```

## Checklist

- [ ] Usar jsPDF (já disponível)
- [ ] Tabelas formatadas
- [ ] Headers/footers
- [ ] Page numbers
- [ ] Links clicáveis se possível

## Regra

> PDF = para impressão/leitura offline. Markdown = para manutenção.