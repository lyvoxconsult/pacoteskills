# UI Skills - Constraints de UI

## Visão Geral

Constraints de UI para guiar o agente na criação de interfaces front-end:
- shadcn/ui
- Tailwind CSS
- Radix UI
- Componentes consistentes

## Stack de UI

### Componentes shadcn/ui
```
src/components/ui/
├── button.tsx
├── input.tsx
├── dialog.tsx
├── dropdown-menu.tsx
├── select.tsx
├── form.tsx
├── label.tsx
├── toast.tsx
└── ...
```

### Tailwind Configuration
```typescript
// tailwind.config.ts
export default {
  darkMode: ['class'],
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: { DEFAULT: 'hsl(var(--primary))', foreground: 'white' },
        // ...
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
}
```

## Regras de UI

### 1. Usar Componentes shadcn
- **Nunca** criar buttons/input/dialogs do zero
- Usar componentes da lib
- Extend apenas quando necessário

### 2. Consistência Visual
- Same padding/margins
- Same border-radius
- Same fonts
- Same colors

### 3. Responsividade
```tsx
// Mobile-first
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
```

### 4. Acessibilidade
- Alt text em imagens
- Labels em inputs
- Keyboard navigation
- Contrast ratios

## Padrões de Componentes

### Form
```tsx
<Form>
  <FormField name="email" label="Email" placeholder="seu@email.com" />
  <FormField name="password" label="Senha" type="password" />
  <Button type="submit">Entrar</Button>
</Form>
```

### Data Table
```tsx
<DataTable columns={columns} data={data} filtering sorting pagination />
```

### Card
```tsx
<Card>
  <CardHeader>
    <CardTitle>Título</CardTitle>
    <CardDescription>Descrição</CardDescription>
  </CardHeader>
  <CardContent>Conteúdo</CardContent>
  <CardFooter>Rodapé</CardFooter>
</Card>
```

## Typography

### Headings
- H1: 3rem/bold → h1.fontSize.h1
- H2: 2.25rem/semibold
- H3: 1.875rem/medium

### Body
- Large: 1.125rem
- Base: 1rem
- Small: 0.875rem
- XS: 0.75rem

## Spacing

### Scale
- p-0 = 0
- p-1 = 0.25rem (4px)
- p-2 = 0.5rem (8px)
- p-4 = 1rem (16px)
- p-6 = 1.5rem (24px)
- p-8 = 2rem (32px)

## Checklist de UI

- [ ] shadcn/ui component usado
- [ ] tailwind tokens aplicados
- [ ] Dark mode funciona
- [ ] Mobile responsive
- [ ] Keyboard navigation works
- [ ] Focus states visíveis
- [ ] Loading states presentes
- [ ] Error states presentes
- [ ] Empty states tratados

## Regra de Ouro

> UI consistente = interface profissional. Usar o que já existe.