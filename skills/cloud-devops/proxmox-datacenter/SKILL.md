---
name: proxmox-datacenter
description: Pacote curado para administrar Proxmox VE, clusters, VMs, LXC, storage, rede, backups, snapshots, Ceph, automacao Ansible/Terraform e MCPs Proxmox com guardrails de datacenter. Use quando o usuario pedir Proxmox, PVE, hypervisor, homelab, datacenter, VM/LXC, cluster, HA, ZFS, Ceph, Proxmox API, MCP Proxmox ou automacao de infraestrutura virtualizada.
---

# Proxmox Datacenter

Use este pacote como roteador antes de operar Proxmox ou preparar automacoes para
datacenter. Ele agrupa skills, ferramentas e MCPs baixados de fontes externas e
skills complementares do proprio repositorio.

## Ordem recomendada

1. Leia `README.md` e `MANIFEST.md` deste pacote.
2. Escolha uma skill em `skills/core/` para o fluxo principal.
3. Use `skills/complementares/` para temas de apoio: Ansible, MCP, rede, Terraform, monitoramento, banco e dados.
4. Use `mcp-servers/` apenas como snapshot/fonte de instalacao; nao coloque segredos nesses arquivos.
5. Para acoes destrutivas em Proxmox, exija confirmacao explicita e plano de rollback.

## Guardrails obrigatorios

- Nunca commitar host real, token, senha, cookie, chave SSH ou URL autenticada.
- Preferir API token com menor permissao possivel, em variaveis de ambiente.
- Separar leitura, planejamento e escrita: primeiro inventario, depois mudanca.
- Antes de start/stop/delete/migrate/rollback, identificar node, VMID/CTID, impacto e backup/snapshot.
- Para MCPs, tratar todas as ferramentas de escrita como operacoes privilegiadas.
- Declarar exatamente o que foi validado e o que ficou sem teste real em cluster.

## Onde procurar

- Skills principais: `skills/core/`
- Skills complementares: `skills/complementares/`
- MCPs e ferramentas baixadas: `mcp-servers/`
- Manifesto de origem: `SOURCES.md`
- Checklist operacional: `OPERATIONS.md`
