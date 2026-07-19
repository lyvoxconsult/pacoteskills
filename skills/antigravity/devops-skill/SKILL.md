---
name: devops-skill
description: Use for Docker, Kubernetes, Terraform, CI/CD, deployment pipelines, environment configuration, secrets, build reproducibility, release safety, infrastructure as code, containers, and operational automation. Trigger for deployment, runtime, infrastructure, build, or environment changes.
---

# DevOps Skill

Use this skill when code must run reliably outside the local editor.

Reference repositories:
- https://github.com/docker/docker-ce
- https://github.com/kubernetes/kubernetes
- https://github.com/hashicorp/terraform

## Workflow

1. Identify the target environment: local, CI, staging, production, container, cluster, or serverless.
2. Read existing Dockerfiles, compose files, manifests, Terraform modules, and CI workflows before editing.
3. Prefer reproducible builds, pinned major versions, explicit environment variables, and clear health checks.
4. Keep secrets out of images, logs, source control, and generated artifacts.
5. Make deployment changes reversible and observable.
6. Validate syntax and dry-run plans when tooling is available.

## Commands To Prefer When Available

- `docker build .`
- `docker compose config`
- `kubectl apply --dry-run=server -f <file>`
- `terraform fmt -check`
- `terraform validate`
- `terraform plan`

## Review Checklist

- Build context excludes unnecessary or secret files.
- Runtime configuration is explicit and documented in existing config patterns.
- Health checks and readiness behavior match the app.
- IaC changes are scoped and reviewable.
- Rollback and failure signals are understood.
