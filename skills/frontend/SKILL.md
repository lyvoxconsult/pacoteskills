# FRONTEND_SKILL

Skill especializada em frameworks frontend modernos, styling e UI components.

## Repositórios de Referência

- **Next.js**: https://github.com/vercel/next.js
- **Tailwind CSS**: https://github.com/tailwindlabs/tailwindcss
- **shadcn/ui**: https://github.com/shadcn-ui/ui

## Capacidades

### 1. Next.js (React Framework)
- Criar aplicações Next.js (App Router e Pages Router)
- Implementar Server Components e Client Components
- Configurar routing com file-based routing
- Implementar data fetching (getStaticProps, getServerSideProps)
- Usar API Routes / Route Handlers
- Configurar middleware
- Implementar SSR, SSG, ISR
- Usar Next.js Image, Font, Script optimization

### Next.js App Router
```typescript
// app/page.tsx
export default function Home() {
  return <h1>Hello World</h1>
}

// app/blog/[slug]/page.tsx
export default async function BlogPost({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)
  return <article>{post.content}</article>
}
```

### 2. Tailwind CSS
- Configurar Tailwind em projetos
- Usar utility classes para styling
- Implementar design system custom
- Configurar dark mode
- Usar @apply e @layer
- Criar componentes reutilizáveis
- Configurar Purge/CSS

### Tailwind Exemplo
```jsx
<button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
  Click me
</button>

<div className="grid grid-cols-1 md:grid-cols-3 gap-4">
  {items.map(item => (
    <Card key={item.id} {...item} />
  ))}
</div>
```

### 3. shadcn/ui
- Configurar shadcn/ui no projeto
- Usar componentes Radix UI baseados
- Customizar componentes via CSS/Tailwind
- Implementar Forms com React Hook Form + Zod
- Usar command palette, dialogs, dropdowns
- Configurar tema (light/dark)

### shadcn/ui Exemplo
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export function Dashboard() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Welcome</CardTitle>
      </CardHeader>
      <CardContent>
        <Button variant="default">Get Started</Button>
      </CardContent>
    </Card>
  )
}
```

### 4. Boas Práticas Frontend
- **Performance**: Code splitting, lazy loading, image optimization
- **SEO**: Meta tags, semantic HTML, SSR
- **Accessibility**: ARIA labels, keyboard navigation, contrast
- **Responsiveness**: Mobile-first, breakpoints
- **State Management**: Context, Zustand, Redux Toolkit

## Ferramentes Complementares

- **TypeScript**: Tipagem estática
- **Zod**: Validação de schemas
- **React Hook Form**: Gerenciamento de formulários
- **Framer Motion**: Animações
- **React Query**: Data fetching e caching

## Quando Usar

Use esta skill quando:
- Precisa criar aplicações React/Next.js
- Precisa implementar UI com Tailwind CSS
- Precisa usar componentes shadcn/ui
- Precisa configurar SSR/SSG
- Precisa implementar design system
- Precisa otimizar performance frontend