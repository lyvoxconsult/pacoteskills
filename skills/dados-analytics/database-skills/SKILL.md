# 🗄️ Database Skills — Interações Seguras com Supabase e Postgres

Esta skill define as melhores práticas para desenhar schemas de bancos de dados, gerenciar migrations com segurança e interagir de forma performática com instâncias de PostgreSQL e do ecossistema Supabase.

---

## 🔐 Segurança do Banco de Dados (Row Level Security)

1. **RLS Ativo por Padrão:**
   - Toda tabela criada em ambientes Postgres expostos (como Supabase) deve ter o **RLS** habilitado imediatamente.
   - **Comando SQL obrigatório:**
     ```sql
     ALTER TABLE nome_da_tabela ENABLE ROW LEVEL SECURITY;
     ```

2. **Políticas de Acesso Granulares (Policies):**
   - Nunca crie políticas genéricas de leitura/escrita irrestritas para perfis anônimos.
   - Restrinja operações de inserção, deleção e atualização aos usuários autenticados correspondentes:
     ```sql
     CREATE POLICY "Usuários autenticados podem ler seus próprios dados"
     ON nome_da_tabela
     FOR SELECT
     TO authenticated
     USING (auth.uid() = user_id);
     ```

---

## 📈 Performance e Escalabilidade

- **Índices Estratégicos:** Crie índices (`CREATE INDEX`) em colunas que sofrem buscas frequentes no frontend ou que são usadas em chaves estrangeiras (joins).
- **Gerenciamento de Conexões (Pooling):** Conexões diretas a partir de funções serverless podem estourar rapidamente o pool de conexões do Postgres. Sempre utilize o proxy do banco de dados (ex: pgBouncer no Supabase, Prisma Accelerated ou pools locais do Neon DB).
- **Migrations Seguras:** Evite alterações destrutivas em banco em produção (`DROP COLUMN` ou `ALTER COLUMN TYPE` que necessitem de travar a tabela inteira). Favoreça migrations incrementais idempotentes.
