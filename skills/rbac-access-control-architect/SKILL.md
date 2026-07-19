---
name: rbac-access-control-architect
description: >-
  Arquitetura, Implementação, Auditoria e QA de Controle de Acesso por Função
  (RBAC). Use quando o projeto envolver autenticação, autorização, papéis de
  usuário, permissões, cargos, níveis de acesso, Supabase RLS, controle de
  permissões no backend, sistemas multi-tenant, auditoria de acesso, políticas
  de segurança ou hardening de frontend, backend e banco.
---

# RBAC Access Control Architect

Arquitetura, Implementação, Auditoria e QA de Controle de Acesso por Função.

---

## Objetivo

Tornar o agente responsável por analisar, projetar, implementar, revisar, testar e documentar sistemas de autorização baseados em **RBAC — Role-Based Access Control**, garantindo que o controle de acesso seja seguro, escalável, auditável, multi-tenant quando necessário e compatível com boas práticas de engenharia.

Usar esta skill sempre que o projeto envolver:

- Autenticação
- Autorização
- Papéis de usuário
- Permissões / cargos / níveis de acesso
- Menus condicionais / rotas protegidas / módulos administrativos
- Sistemas multiempresa, multiunidade, multitenant ou workspace
- Supabase RLS
- Controle de permissões no backend
- Separação entre usuários comuns, admins, gestores, operadores, clientes ou colaboradores
- Auditoria de alterações de acesso / políticas de segurança / hardening de frontend, backend e banco

O objetivo principal é impedir que o agente implemente autorização superficial, frágil, apenas visual ou baseada somente no frontend.

---

## 1. Contexto Técnico Obrigatório

**RBAC = Role-Based Access Control** (controle de acesso baseado em papéis/funções).

O modelo correto parte da seguinte ideia:

- Usuários recebem papéis
- Papéis recebem permissões
- Permissões autorizam ações sobre recursos
- A aplicação valida permissões no backend e, quando houver banco com políticas, também no banco
- O frontend apenas reflete permissões, mas nunca deve ser a fonte real de segurança

O agente deve tratar RBAC como um tema de **segurança**, não apenas como organização de menu.

---

## 2. Fontes e Referências-base

### Referências conceituais

- IBM — O que é controle de acesso baseado em função
- NIST RBAC Model
- ANSI INCITS 359-2004
- Ferraiolo, Kuhn, Chandramouli e Sandhu — referências clássicas sobre RBAC
- OWASP Authorization Cheat Sheet
- OWASP ASVS — requisitos verificáveis de autorização

### Referências práticas

- Casbin documentation
- Spring Security Reference
- ASP.NET Core Authorization Docs
- CASL documentation
- Oso documentation
- Supabase RLS documentation (quando o projeto usar Supabase)
- Documentação oficial do framework usado no projeto

### Referências informadas pelo usuário

- IBM — O que é controle de acesso baseado em função
- Milvus — Explicação do RBAC
- IAM Tech Day — Modelos RBAC, ABAC e PBAC
- E-TRUST — Implementando um modelo RBAC com eficiência

### Links que devem ser ignorados para este contexto

Links da ANAC, biblioteca da ANAC, eBianch e aprendizagem criativa podem conter a sigla "RBAC" em outro sentido (Regulamentos Brasileiros da Aviação Civil ou portais institucionais). Não usar como base para controle de acesso, salvo se o projeto for explicitamente sobre aviação civil.

---

## 3. Quando Ativar Esta Skill

Ativar automaticamente quando a solicitação mencionar qualquer um destes termos ou intenções:

RBAC, role, roles, função, cargo, permissões, permissionamento, autorização, acesso, admin, gestor, usuário, colaboradores, multiempresa, tenant, unidade, workspace, organização, owner, supervisor, operador, cliente, RLS, policies, Supabase, rota protegida, menu por permissão, controle de acesso, middleware de autenticação, segurança de módulo, auditoria de permissão, hardening de acesso.

Também ativar quando o agente perceber que uma tarefa pode expor dados indevidamente entre usuários, empresas, clientes, unidades ou papéis.

---

## 4. Princípios Obrigatórios

Seguir estes princípios sem exceção:

1. **Autorização nunca deve depender apenas do frontend.** Botões, menus e telas podem ser ocultados no frontend, mas a validação real deve estar no backend, banco ou camada de autorização confiável.

2. **Autenticação e autorização são coisas diferentes.** Autenticação confirma quem é o usuário. Autorização confirma o que ele pode fazer.

3. **Usar o princípio do menor privilégio.** Todo usuário deve receber apenas as permissões necessárias para sua função real.

4. **Permissões devem ser atômicas.** Evitar permissões genéricas demais como `admin_all` quando o sistema precisa de controle granular.

5. **Roles não devem ser confundidas com cargos organizacionais.** Um cargo pode sugerir um papel, mas a autorização deve ser baseada em permissões técnicas claras.

6. **Toda ação sensível precisa de validação no servidor.** Criar, editar, excluir, exportar, aprovar, cancelar, visualizar dados sensíveis e alterar permissões são ações sensíveis.

7. **Multi-tenant exige isolamento real.** Em sistemas com empresas, unidades, clientes ou workspaces, toda permissão deve respeitar o escopo do tenant.

8. **Permissões devem ser auditáveis.** Alterações em papéis, vínculos e permissões devem gerar logs de auditoria quando o sistema tiver maturidade para isso.

9. **Não expor chaves sensíveis.** Nunca expor `service_role`, tokens administrativos, secrets ou chaves privadas no frontend.

10. **Não confiar em dados enviados pelo cliente.** `role`, `tenant_id`, `user_id`, `is_admin` ou permissões vindas do frontend devem ser tratadas como dados não confiáveis.

---

## 5. Modelos RBAC Suportados

Identificar qual modelo se aplica melhor ao projeto.

### 5.1 RBAC básico

Usar quando o sistema é simples.

Estrutura: usuário → papel → permissão.

- Usuário recebe papel
- Papel recebe permissão

Exemplo: usuário Pedro, papel Administrador, permissões `users.create`, `users.update`, `reports.view`.

### 5.2 RBAC hierárquico

Usar quando existem papéis com herança.

Exemplo: Owner herda Admin → Admin herda Gestor → Gestor herda Operador.

Evitar heranças confusas ou circulares.

### 5.3 RBAC com constraints

Usar quando existem regras adicionais:

- Usuário pode aprovar pagamento, mas não o próprio pagamento
- Operador pode editar lead somente se for responsável por ele
- Gestor pode ver dados apenas da própria unidade
- Suporte pode acessar conta de cliente apenas com justificativa

### 5.4 RBAC por domínio, tenant ou organização

Usar em sistemas SaaS, multiempresa, multiunidade ou multiworkspace.

Exemplo: o mesmo usuário pode ser Admin na Empresa A, Operador na Empresa B e sem acesso à Empresa C.

Nesse caso, a tabela `user_roles` precisa conter `tenant_id`, `organization_id`, `workspace_id` ou equivalente.

### 5.5 RBAC híbrido com ABAC

Usar quando RBAC puro não é suficiente. RBAC decide pelo papel/permissão. ABAC complementa com atributos como: dono do recurso, unidade, status, horário, plano contratado, tipo de cliente, região, contexto da ação.

Exemplo: um usuário com permissão `leads.update` só pode editar leads atribuídos a ele ou à sua equipe.

---

## 6. Estrutura Mínima Recomendada de Banco

### Estrutura mínima

```
users
roles
permissions
user_roles
role_permissions
```

### Estruturas opcionais

```
role_hierarchy
tenants
organizations
workspaces
user_tenants
audit_logs
sessions
permission_groups
resource_policies
```

---

## 7. Modelo SQL Base

Usar como referência inicial. Adaptar nomes, tipos e constraints ao stack real do projeto.

```sql
create table roles (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  slug text not null unique,
  description text,
  is_system boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table permissions (
  id uuid primary key default gen_random_uuid(),
  resource text not null,
  action text not null,
  slug text generated always as (resource || '.' || action) stored,
  description text,
  created_at timestamptz not null default now(),
  unique (resource, action)
);

create table role_permissions (
  role_id uuid not null references roles(id) on delete cascade,
  permission_id uuid not null references permissions(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (role_id, permission_id)
);

create table user_roles (
  user_id uuid not null references users(id) on delete cascade,
  role_id uuid not null references roles(id) on delete cascade,
  tenant_id uuid null,
  created_at timestamptz not null default now(),
  created_by uuid null,
  primary key (user_id, role_id, tenant_id)
);
```

Quando o projeto usar Supabase Auth, substituir `users(id)` por `auth.users(id)` ou por uma tabela de perfil relacionada, conforme a arquitetura já existente.

---

## 8. Padrão de Nomenclatura de Permissões

Preferir o formato `recurso.ação`:

```
dashboard.view
users.view
users.create
users.update
users.delete
roles.view
roles.create
roles.update
roles.delete
permissions.manage
leads.view
leads.create
leads.update
leads.delete
leads.convert
clients.view
finance.view
finance.create
finance.approve
support.view
support.reply
settings.view
settings.update
reports.export
audit.view
```

Evitar nomes vagos como `access_all`, `manage_everything`, `super_permission`, `full_access`, `admin`.

Roles podem ser amplas. Permissões devem ser específicas.

---

## 9. Papéis Comuns Recomendados

Sugerir papéis conforme o projeto, sempre validando o contexto real.

### Exemplos genéricos

```
owner
admin
manager
financial
commercial
support
operator
developer
viewer
client
```

### Em projetos Lyvox (quando fizer sentido)

```
proprietario
administrador
gestao
financeiro
comercial
desenvolvedor
contador
suporte
cliente
operador
```

Não assumir que todos os projetos usam os mesmos papéis. Primeiro inspecionar a documentação, o banco e o código.

---

## 10. Workflow Obrigatório

Antes de implementar ou alterar RBAC, executar este fluxo.

### Etapa 1 — Entendimento do contexto

Ler e mapear: objetivo do sistema, tipos de usuários, módulos existentes, regras de negócio, stack do projeto, estrutura de banco, rotas, endpoints, componentes de frontend, autenticação atual, autorização atual, documentação existente, Obsidian do projeto, README, migrations, policies, middlewares, hooks, guards, serviços de API.

Não implementar antes de entender o modelo atual.

### Etapa 2 — Diagnóstico

Identificar: onde a autorização está sendo feita, se existe validação apenas no frontend, se existem rotas sem proteção, se endpoints confiam no frontend, se há vazamento entre tenants, se roles estão hardcoded, se há permissões duplicadas, se existe RLS, se RLS está coerente, se service role está exposta, se há logs de auditoria, se há testes, se há inconsistência entre menu, tela, backend e banco.

### Etapa 3 — Proposta de arquitetura

Antes de alterar código, definir: modelo RBAC escolhido, tabelas necessárias, permissões necessárias, papéis necessários, escopo por tenant, regras por módulo, fluxo de validação no backend, reflexo no frontend, regras RLS, plano de migração sem quebrar dados existentes, plano de testes, critérios de aceite.

### Etapa 4 — Implementação

Implementar em camadas:

1. Banco e migrations
2. Seeds de roles e permissions
3. RLS/policies (quando aplicável)
4. Serviços de autorização
5. Middlewares/guards no backend
6. Hooks/helpers no frontend (apenas para UX)
7. Proteção de rotas
8. Controle de menus
9. Controle de botões e ações
10. Auditoria
11. Testes
12. Documentação

### Etapa 5 — QA e validação

Validar:

- Usuário sem permissão não acessa pela URL
- Usuário sem permissão não acessa via API direta
- Usuário sem permissão não consegue executar ação via payload manual
- Usuário de um tenant não acessa dados de outro tenant
- Menu oculto não é tratado como segurança real
- Backend bloqueia corretamente
- Banco bloqueia corretamente (quando houver RLS)
- Logs são gerados para ações sensíveis
- Roles e permissions estão documentadas
- Testes automatizados passam
- Build passa
- Lint passa

### Etapa 6 — Documentação

Atualizar: README técnico, documentação do módulo, matriz de permissões, migrations aplicadas, políticas RLS, decisões de arquitetura, pendências, riscos, notas no Obsidian, checklist de QA.

---

## 11. Uso Obrigatório de Subagentes

Quando a tarefa envolver RBAC em sistema real, usar subagentes sempre que possível.

### 11.1 Subagente Orquestrador

Entender a solicitação, dividir o trabalho, coordenar subagentes, evitar duplicidade, consolidar decisões, garantir que nada fique pendente.

### 11.2 Subagente de Pesquisa e Contexto

Ler documentação do projeto, consultar Obsidian, verificar README, analisar migrations, buscar referências oficiais, consultar documentação da biblioteca usada, identificar o padrão já existente no projeto.

### 11.3 Subagente de Arquitetura RBAC

Definir modelo de autorização, propor tabelas, definir papéis, definir permissões, definir escopo multi-tenant, criar matriz de acesso, validar compatibilidade com o sistema.

### 11.4 Subagente Backend/API

Implementar guards, middlewares, services, policies, validações por endpoint, tratamento de erro, respostas seguras, proteção contra payload malicioso.

### 11.5 Subagente Banco/Supabase/RLS

Criar migrations, revisar RLS, criar policies, revisar relacionamentos, evitar vazamento entre tenants, validar queries, impedir uso indevido de service role.

### 11.6 Subagente Frontend/UI

Esconder menus conforme permissão, proteger rotas client-side, exibir estados de acesso negado, evitar botões que usuário não pode usar, manter UX clara, não tratar frontend como camada de segurança principal.

### 11.7 Subagente QA/Security

Testar acesso permitido, testar acesso negado, testar tentativa via URL direta, testar tentativa via API direta, testar multi-tenant, revisar privilege escalation, revisar IDOR, revisar falhas de RLS, revisar inconsistências entre frontend e backend.

### 11.8 Subagente Documentação

Atualizar Obsidian, atualizar README, criar matriz de permissões, registrar decisões, registrar riscos, registrar pendências, criar checklist final.

---

## 12. Regras Específicas para Supabase

### 12.1 Nunca expor service role

A chave `service_role` nunca pode aparecer no frontend, bundle, `.env` público, código client-side ou logs.

### 12.2 RLS deve ser tratada como camada crítica

Quando houver dados sensíveis, ativar e revisar RLS.

```sql
alter table projects enable row level security;
```

### 12.3 Policies devem considerar tenant

```sql
create policy "Users can view records from their tenant"
on projects
for select
using (
  tenant_id in (
    select tenant_id
    from user_roles
    where user_id = auth.uid()
  )
);
```

Adaptar a policy real ao schema do projeto.

### 12.4 Não confiar em tenant_id enviado pelo frontend

O backend e/ou RLS devem validar se o usuário realmente pertence ao tenant informado.

### 12.5 Separar permissões administrativas

Ações administrativas como gerenciar usuários, papéis, permissões e configurações devem ter permissões próprias:

```
users.manage
roles.manage
permissions.manage
settings.update
```

---

## 13. Regras Específicas para Frontend

### O frontend deve

- Ocultar menus não permitidos
- Bloquear rotas visualmente
- Exibir mensagem de acesso negado
- Evitar renderizar ações proibidas
- Atualizar UI conforme permissões reais do usuário
- Buscar permissões de fonte confiável
- Lidar com estado de carregamento
- Lidar com usuário sem role
- Lidar com role removida durante a sessão
- Evitar hardcode espalhado

### O frontend não deve

- Decidir sozinho se uma ação sensível pode ser executada
- Aceitar `isAdmin` vindo de localStorage como verdade absoluta
- Salvar permissões editáveis no navegador
- Expor regras críticas no client sem validação server-side
- Esconder botão e considerar isso segurança suficiente

---

## 14. Regras Específicas para Backend

O backend deve:

- Validar autenticação
- Carregar usuário real
- Carregar tenant real
- Verificar permissão antes da ação
- Bloquear acesso sem permissão
- Retornar erro adequado
- Não vazar dados sensíveis em mensagens de erro
- Registrar auditoria em ações sensíveis
- Centralizar lógica de autorização
- Evitar duplicação de regras espalhadas

Padrão recomendado de fluxo:

```
auth middleware → tenant resolver → permission checker → controller/action → audit log
```

---

## 15. Erros Comuns a Evitar

Nunca fazer:

- RBAC apenas no frontend
- Autorização baseada só em menu
- Role hardcoded em dezenas de arquivos
- `if user.email === "admin@email.com"`
- Permissões baseadas apenas em nome visual de cargo
- Endpoint sem validação
- RLS desativada em dados sensíveis
- Policy permissiva demais
- `select *` sem escopo
- Usuário de uma empresa ver dados de outra
- Frontend enviar `role: admin` e backend aceitar
- Usar service role no navegador
- Excluir dados sem checar permissão
- Criar admin global sem necessidade
- Misturar autenticação com autorização
- Deixar permissões sem documentação
- Alterar roles sem auditoria
- Criar regras que quebram usuários existentes

---

## 16. Matriz de Permissões Obrigatória

Sempre que implementar ou revisar RBAC, gerar uma matriz como esta:

| Módulo | Ação | Permissão | Owner | Admin | Gestor | Operador | Cliente |
|---|---|---|---|---|---|---|---|
| Dashboard | Ver | dashboard.view | Sim | Sim | Sim | Sim | Limitado |
| Usuários | Ver | users.view | Sim | Sim | Sim | Não | Não |
| Usuários | Criar | users.create | Sim | Sim | Não | Não | Não |
| Usuários | Editar | users.update | Sim | Sim | Não | Não | Não |
| Usuários | Excluir | users.delete | Sim | Não | Não | Não | Não |
| Financeiro | Ver | finance.view | Sim | Sim | Sim | Não | Não |
| Relatórios | Exportar | reports.export | Sim | Sim | Sim | Não | Não |

A matriz real deve ser criada conforme os módulos do projeto.

---

## 17. Checklist de Segurança

- [ ] Rotas privadas exigem autenticação
- [ ] Rotas sensíveis exigem permissão específica
- [ ] Endpoints validam permissão no servidor
- [ ] Frontend não é a única barreira
- [ ] Menus respeitam permissões
- [ ] Botões respeitam permissões
- [ ] API bloqueia usuário sem permissão
- [ ] URL direta não burla acesso
- [ ] Payload manual não burla acesso
- [ ] Usuário sem tenant não acessa dados
- [ ] Usuário de tenant A não acessa tenant B
- [ ] RLS está ativa onde necessário
- [ ] Policies foram testadas
- [ ] Service role não está exposta
- [ ] Alterações de roles são auditadas
- [ ] Permissões estão documentadas
- [ ] Testes foram executados
- [ ] Build foi executado
- [ ] Lint foi executado
- [ ] Pendências foram registradas

---

## 18. Checklist de Testes Práticos

### Usuário sem login

- Não pode acessar dashboard privado
- Não pode chamar API privada
- Deve ser redirecionado ou receber erro seguro

### Usuário comum

- Vê apenas módulos permitidos
- Não acessa rota admin via URL direta
- Não consegue executar ação proibida via API
- Não vê dados de outro tenant

### Gestor

- Acessa módulos de gestão permitidos
- Não gerencia roles se não tiver permissão
- Não acessa configurações globais sem permissão

### Admin

- Gerencia usuários conforme escopo
- Não acessa tenant externo
- Não executa ação de owner se não permitido

### Owner

- Pode gerenciar papéis críticos
- Pode alterar permissões conforme regra do sistema
- Ações críticas geram auditoria

### Multi-tenant

- Mesmo usuário com roles diferentes por tenant recebe permissões corretas em cada tenant
- Troca de tenant atualiza permissões
- API valida tenant real
- RLS bloqueia vazamento cruzado

---

## 19. Bibliotecas por Stack

Escolher biblioteca conforme o stack existente. Não trocar stack sem necessidade.

### Node.js / TypeScript

Opções: CASL, accesscontrol, node-casbin, NestJS Guards, `@nestjs/casl`, middlewares próprios para projetos simples.

Uso recomendado: CASL para regras mais expressivas; Casbin para políticas externas e RBAC formal; Guards no NestJS para arquitetura organizada; middleware próprio para apps menores em Express, Fastify, Next.js API ou serverless.

### Python

Opções: pycasbin, casbin, oso, django-guardian, flask-principal, FastAPI dependencies customizadas.

### Java / Kotlin

Opções: Spring Security, Casbin Java, Apache Shiro.

### .NET

Opções: ASP.NET Core Authorization, policies, claims, roles, NetCasbin.

### Go

Opções: Casbin, middlewares do framework usado, policies próprias com testes.

---

## 20. Padrão de Implementação em TypeScript

Exemplo conceitual:

```ts
type Permission =
  | "dashboard.view"
  | "users.view"
  | "users.create"
  | "users.update"
  | "users.delete"
  | "roles.manage"
  | "finance.view"
  | "reports.export";

type UserContext = {
  userId: string;
  tenantId?: string;
  roles: string[];
  permissions: Permission[];
};

export function can(user: UserContext, permission: Permission): boolean {
  return user.permissions.includes(permission);
}

export function requirePermission(permission: Permission) {
  return async function guard(context: UserContext) {
    if (!context.userId) {
      throw new Error("UNAUTHENTICATED");
    }

    if (!can(context, permission)) {
      throw new Error("FORBIDDEN");
    }

    return true;
  };
}
```

Este exemplo não substitui a validação real do projeto. Adaptar ao framework, banco e autenticação existentes.

---

## 21. Padrão de Resposta de Erro

Usar respostas seguras:

```
401 Unauthorized — usuário não autenticado
403 Forbidden — usuário autenticado, mas sem permissão
404 Not Found — quando revelar existência do recurso for risco
```

Não retornar detalhes como "Você não pode acessar porque não tem a role admin global da empresa X". Preferir mensagens neutras:

```
Acesso negado.
Você não tem permissão para executar esta ação.
```

---

## 22. Auditoria

Sempre que o sistema permitir, auditar ações como: criação/alteração/desativação de usuário, reset de senha, alteração de role/permissão, criação/exclusão de role, alteração de configurações, exportação de relatório, exclusão de dados, acesso administrativo a dados de cliente.

Estrutura conceitual:

```sql
create table audit_logs (
  id uuid primary key default gen_random_uuid(),
  actor_user_id uuid not null,
  tenant_id uuid null,
  action text not null,
  resource text not null,
  resource_id uuid null,
  metadata jsonb,
  created_at timestamptz not null default now()
);
```

---

## 23. Integração com Documentação Obsidian

Quando o projeto tiver Obsidian ou documentação local, atualizar ou criar notas como:

```
Arquitetura/RBAC.md
Segurança/Matriz de Permissões.md
Banco/RLS e Policies.md
QA/Checklist RBAC.md
Pendências/Riscos de Autorização.md
Histórico/Atualizações RBAC.md
```

As notas devem conter: modelo escolhido, papéis existentes, permissões existentes, matriz de permissões, tabelas, policies, endpoints protegidos, pendências, riscos, decisões, testes executados, próximos passos.

Não criar nota vazia. Não duplicar documentação existente. Atualizar o arquivo correto quando já existir documentação equivalente.

---

## 24. Critérios de Aceite

A entrega só pode ser considerada concluída quando:

- O modelo RBAC estiver documentado
- Roles e permissions estiverem claras
- Frontend respeitar permissões
- Backend validar permissões
- Banco proteger dados sensíveis quando aplicável
- Multi-tenant estiver isolado quando aplicável
- Testes críticos forem executados
- Build/lint passarem ou falhas forem relatadas
- Riscos forem documentados
- Pendências forem explicitadas
- QA final confirmar que não existe autorização apenas visual

---

## 25. Relatório Final Obrigatório

Ao concluir uma tarefa usando esta skill, entregar um relatório com:

1. Contexto analisado
2. Modelo RBAC identificado ou implementado
3. Papéis mapeados
4. Permissões mapeadas
5. Arquivos alterados
6. Banco/migrations/policies alteradas
7. Regras de backend implementadas
8. Regras de frontend implementadas
9. Testes executados
10. Resultado do QA
11. Riscos encontrados
12. Pendências
13. Documentação atualizada
14. Próximos passos recomendados

Se algo não foi feito, explicar claramente.

---

## 26. Modo Auditoria

Quando o pedido for revisar um sistema existente, atuar como auditor.

Verificar: endpoints sem autorização, telas acessíveis por URL direta, roles hardcoded, permissões genéricas demais, ausência de RLS, policies erradas, vazamento multi-tenant, inconsistência entre frontend e backend, actions sensíveis sem log, usuários admin demais, dados carregados antes da validação, queries sem filtro por tenant, funções serverless sem guard, tokens expostos, erros revelando dados internos.

Classificar problemas em:

```
Crítico
Alto
Médio
Baixo
Melhoria
```

---

## 27. Modo Implementação

Quando o pedido for implementar RBAC, seguir esta ordem:

1. Ler contexto
2. Mapear usuários, módulos e ações
3. Criar matriz de permissões
4. Definir schema
5. Criar migrations
6. Criar seeds
7. Implementar permission checker
8. Implementar guards/middlewares
9. Proteger endpoints
10. Proteger frontend
11. Criar estados de acesso negado
12. Implementar logs críticos
13. Testar usuários por perfil
14. Testar isolamento de tenant
15. Documentar
16. Entregar relatório final

---

## 28. Modo Correção de Bug

Quando o pedido for corrigir bug de permissão:

1. Reproduzir o bug
2. Identificar usuário, role, permissão e tenant
3. Verificar se o erro está no frontend, backend, banco ou policy
4. Corrigir a causa raiz
5. Criar teste de regressão
6. Validar com usuário permitido e não permitido
7. Documentar a correção

Não corrigir apenas escondendo botão ou menu.

---

## 29. Modo Design de Painel Administrativo

Quando RBAC envolver tela de administração, garantir que exista:

- Lista de usuários
- Status do usuário
- Papéis vinculados
- Tenant/unidade vinculada
- Ações permitidas
- Bloqueio de autoexclusão crítica
- Proteção contra remover o último owner/admin
- Confirmação para ações sensíveis
- Histórico ou auditoria
- Feedback visual claro (loading, erro, estado vazio)
- Responsividade

---

## 30. Regras para Agentes em Projetos Lyvox

Em projetos Lyvox, considerar como padrão:

- Uso frequente de Supabase
- Necessidade de RLS
- Preferência por sistemas SaaS
- Uso de multiempresa/multiunidade quando aplicável
- Documentação em Obsidian
- QA obrigatório
- Uso de subagentes
- Validação de frontend, backend e banco
- Cuidado com dados de clientes
- Visual profissional, mas segurança sempre acima da aparência
- Evitar implementação demonstrativa quando o módulo for de segurança real

---

## 31. Ativação da Skill

Quando esta skill for ativada, iniciar com este raciocínio operacional:

> Vou tratar esta tarefa como uma atuação de RBAC/controle de acesso. Antes de implementar, preciso entender o modelo atual de autenticação, autorização, usuários, papéis, permissões, banco, frontend, backend, rotas, endpoints e documentação. Depois vou propor ou ajustar a arquitetura, aplicar validação real no backend/banco, refletir permissões no frontend, executar QA e documentar.

---

## 32. Prompt para Chamar Esta Skill

Use este prompt quando quiser obrigar o agente a aplicar a skill:

> Ative a skill RBAC Access Control Architect.
>
> Analise o projeto antes de implementar. Mapeie usuários, papéis, permissões, módulos, rotas, endpoints, banco, RLS/policies e documentação existente.
>
> Use subagentes quando houver mais de uma frente: pesquisa/contexto, arquitetura RBAC, backend/API, banco/Supabase/RLS, frontend/UI, QA/security e documentação.
>
> Implemente ou corrija o controle de acesso com validação real no backend e, quando aplicável, no banco. O frontend deve apenas refletir permissões, nunca ser a única camada de segurança.
>
> Crie ou atualize a matriz de permissões, proteja endpoints, revise RLS, teste usuários com e sem permissão, teste isolamento multi-tenant, execute QA, registre riscos e atualize a documentação no Obsidian/README do projeto.
>
> No final, entregue relatório com arquivos alterados, permissões criadas, testes executados, riscos, pendências e validação final.

---

## 33. Resultado Esperado

Ao usar esta skill, produzir RBAC de nível profissional:

- Seguro
- Testável
- Documentado
- Auditável
- Escalável
- Compatível com multi-tenant
- Validado no backend
- Protegido no banco quando necessário
- Refletido corretamente no frontend
- Sem dependência de autorização apenas visual
- Alinhado às boas práticas de OWASP, NIST e arquitetura moderna de software
