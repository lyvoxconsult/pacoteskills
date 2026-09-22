# DEVOPS_SKILL

Skill especializada em infraestrutura, containers, orquestração e IaC.

## Repositórios de Referência

- **Docker**: https://github.com/docker/docker-ce
- **Kubernetes**: https://github.com/kubernetes/kubernetes
- **Terraform**: https://github.com/hashicorp/terraform

## Capacidades

### 1. Docker
- Escrever Dockerfiles otimizados
- Usar multi-stage builds
- Configurar docker-compose.yaml
- Criar networks e volumes
- Implementar Docker networking
- Otimizar imagens (alpine, distroless)
- Configurar Dockerfile best practices

### Dockerfile Exemplo
```dockerfile
# Multi-stage build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

### Docker Compose
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      - db
      - redis
  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
  redis:
    image: redis:7-alpine

volumes:
  postgres_data:
```

### 2. Kubernetes
- Criar manifests (Deployment, Service, ConfigMap, etc.)
- Configurar Helm charts
- Implementar Ingress controllers
- Configurar horizontal pod autoscaling
- Implementar health checks (liveness, readiness)
- Usar secrets e configMaps
- Configurar RBAC

### K8s Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:latest
        ports:
        - containerPort: 3000
        resources:
          limits:
            cpu: "500m"
            memory: "256Mi"
```

### 3. Terraform
- Escrever código Terraform (HCL)
- Configurar providers (AWS, GCP, Azure)
- Criar modules reutilizáveis
- Implementar state management
- Usar workspaces
- Configurar remote state (S3, etc.)
- Implementar terratest para testing

### Terraform Exemplo
```hcl
provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  name    = "my-vpc"
  cidr    = "10.0.0.0/16"
  azs     = ["us-east-1a", "us-east-1b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
}

module "ecs" {
  source = "./modules/ecs"
  vpc_id = module.vpc.vpc_id
}
```

### 4. CI/CD Pipeline
- Configurar GitHub Actions / GitLab CI
- Build, test, deploy automatizados
- Artifact management
- Environment promotion (dev → staging → prod)
- Canary deployments
- Rollback strategies

## Quando Usar

Use esta skill quando:
- Precisa containerizar uma aplicação
- Precisa orquestrar containers com K8s
- Precisa gerenciar infraestrutura como código
- Precisa configurar pipelines de CI/CD
- Precisa fazer deploy em cloud (AWS, GCP, Azure)
- Precisa configurar monitoring de infraestrutura