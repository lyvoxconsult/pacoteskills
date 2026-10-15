# Roteamento opcional de especialistas

Descubra entradas reais com find-skills local antes de alternativa externa.
Este pacote funciona sem dependencias adicionais; skills abaixo nao concedem
permissao, provem credenciais nem instalam MCPs. Se ausentes, usar referencias
internas e documentacao oficial. Nao carregar catalogo inteiro.

No catalogo pacoteskills, estas entradas ficam como irmas em cloud-devops.
Em instalacao independente, procurar nos roots reais do agente; nao presumir
que path relativo existe. Confirmar frontmatter e compatibilidade ao abrir.

| Necessidade | Entradas identificadas no catalogo fonte |
|---|---|
| Arquitetura | cloud-architect, hybrid-cloud-architect, multi-cloud-architecture |
| Rede | network-engineer, hybrid-cloud-networking |
| Proxmox | proxmox-datacenter, proxmox-admin, proxmox-host-operator, proxmox-vm-recovery |
| Configuracao | ansible-proxmox, terraform-specialist, terraform-skill |
| Incidente | devops-troubleshooter, linux-troubleshooting |
| Shell | bash-defensive-patterns, windows-shell-reliability, powershell-windows |
| Containers | docker-expert, kubernetes-architect, k8s-security-policies, helm-chart-scaffolding |
| Entrega | deployment-pipeline-design, github-actions-templates, gitlab-ci-patterns, gitops-workflow |
| Observabilidade | observability-engineer, prometheus-configuration, grafana-dashboards |
| IAM/custos | aws-iam-best-practices, aws-security-audit, aws-cost-optimizer |
| Dados/ferramentas | database, data-engineer, mcp-builder, mcp-integration |

Nao herdar exemplos com root/Administrator global, --privsep 0, desativacao
de verificacao ou exclusao automatica. O gate humano desta skill continua
valendo em subskills, pipelines, retries e scripts.

O router cloud-devops cita tambem skills nao presentes em todas as instalacoes;
nome citado nao e inventario confiavel. Pentest/privesc requer autorizacao
especifica e nao e carregado por padrao na auditoria defensiva.

## Contrato com subagentes

Dar objetivo limitado, recursos permitidos, leitura/mutacao, owner e formato
de evidencia. Rede/firewall/state compartilhados tem um implementador por vez.
Analistas independentes podem ler em paralelo. Coordenador reconcilia gaps e
aprova consistencia, mas nao substitui humano para exclusao.
Se ferramentas de subagente nao existem, trabalhar sequencialmente e declarar
autorrevisao. Nunca chamar um role simulado de auditoria independente real.
