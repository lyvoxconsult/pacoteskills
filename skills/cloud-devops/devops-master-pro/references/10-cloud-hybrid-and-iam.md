# Cloud, hibrido e IAM

Use para AWS/Azure/GCP, landing zones e ligacao on-prem/cloud. Nao requer
multi-cloud; entradas incluem conta/tenant/subscription/project, regiao,
owner, billing, limites, dados, conectividade e identidade efetiva.

## Procedimento

1. Confirme contexto da CLI/API e permissao efetiva, nao apenas login bem-sucedido.
   Separe humanos, workloads e CI; prefira identidade temporaria/federada quando
   suportada, com menor privilegio e autenticacao adequada ao risco.
2. Desenhe VPC/VNet, subnets, rotas, firewalls/security groups, DNS, NAT,
   peering/VPN/interconnect, MTU e fluxos de ida/volta. Sobreposicao de CIDRs
   e restricoes transitivas podem impedir roteamento esperado.
3. Defina disponibilidade e dominio de falha real: zona/regiao/site/conta,
   dados e identidade. Replica entre zonas nao prova DR regional nem backup.
4. Mapeie servicos gerenciados e suas responsabilidades: acesso privado,
   autenticao, criptografia, logs, backup, quotas e operacao em incidente.
5. Teste DNS, conectividade e transacao com principal real; teste negativo
   autorizado e logs. API autorizada no control plane nao prova data plane.

## Tradeoffs

Considere latencia, data gravity, egress, custo fixo de NAT/interconnect,
compliance e capacidade de operar. Nao usar servico publico por conveniencia
quando requisito pede isolamento, nem expor management ao mundo para bootstrap.
TLS do endpoint nao implica restricao de origem ou IAM correto.

## Recuperacao e aceite

IaC respeita referencia 08; deletar resource group, bucket, key ou permissao
exige gate humano. KMS/key e dependencia de restore: nao criar backup que
depende apenas de chave perdida junto da conta principal.
Validar quotas/capacidade para DR, identidade alternativa e runbook.
Nao presumir disponibilidade Azure de skill ausente; usar docs oficiais.

Fontes: [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html),
[Azure architecture](https://learn.microsoft.com/en-us/azure/architecture/),
[Google Cloud architecture](https://cloud.google.com/architecture/framework).
