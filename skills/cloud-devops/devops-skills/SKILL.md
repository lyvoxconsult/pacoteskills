# 🚀 DevOps Skills — Deploy Contínuo e Infraestrutura

Esta skill detalha os padrões operacionais para provisionamento de containers, orquestração de deploys contínuos e configurações de pipelines CI/CD resilientes.

---

## 🗃️ Containerização (Docker e Docker Compose)

1. **Escrita de Dockerfiles Otimizados:**
   - Sempre utilize imagens base oficiais leves e seguras (ex: `node:20-alpine` ou `python:3.11-slim`).
   - Siga o padrão de build em múltiplos estágios (*Multi-stage builds*) para garantir que a imagem final de produção contenha apenas os assets compilados e as dependências mínimas necessárias, diminuindo o tamanho da imagem e a superfície de ataque.
   - Execute o container como um usuário não-root por padrão para aumentar a segurança.

2. **Docker Compose para Setup Local:**
   - Crie ambientes locais idênticos ao de produção usando o Docker Compose.
   - Configure redes isoladas, volumes persistentes para bancos de dados locais de teste e utilize o arquivo `.env` local para as injeções de portas e hosts com segurança.

---

## 🚀 Pipelines CI/CD e Deploys Contínuos

- **Esteiras do GitHub Actions:** Construa esteiras contínuas que rodem lints, compilações e suites de testes funcionais preventivos a cada Pull Request antes de liberar o merge na branch principal (`main`).
- **Deploy Otimizado na Vercel:** Utilize deploys por branches secundárias (*Preview Deploys*) para testar interfaces e funcionalidades em homologação antes de promover o commit final para produção.
- **Isolamento de Credenciais em CI/CD:** NUNCA grave credenciais brutas nos arquivos YAML das esteiras. Sempre utilize os repositórios de Secrets do GitHub (`Settings > Secrets and variables > Actions`) ou serviços de cofre como AWS Secrets Manager.
