# Proxmox, virtualizacao e storage

Use para auditoria do host, VM lifecycle, desempenho, backup/clone/restore.
Pre-condicoes: node/VMID/CTID confirmados, ownership, permissao efetiva,
versao, acesso de recuperacao e destino com capacidade conhecida.

## Host

Colete versao/kernel, CPU/RAM e pressao, discos/SMART quando disponivel,
storages, ZFS status/capacidade/erros, mounts, interfaces/bridges/VLAN awareness,
rotas, DNS/NTP, firewall, contas/ACL, jobs, backups, snapshots, ISOs/templates
e logs. Em cluster, examine quorum/replicacao e dominios de falha; single-node
nao precisa fingir quorum multi-node ou garantia de HA.

Read-only conforme suporte: pveversion, pvesm status, zpool status/list,
zfs list, lsblk, df, ip, ss, journalctl, pvesh get e qm config/status.
Saida pode conter metadados privados; sumarize em evidencia protegida.
ZFS ONLINE nao prova disco sem desgaste, capacity suficiente ou restore.

## VMs e lifecycle

1. Leia configuracao de CPU/RAM, discos e backup flags, firmware/TPM,
   boot, NIC/bridge/tag e ISO. Windows 11 precisa atender requisitos reais;
   nao contornar silenciosamente requisitos ou trocar produto.
2. Observe task e estado; running pode ser installer/BSOD. Use evidencia
   interna da referencia 05 e teste da funcao.
3. Verifique locking antes de retry. Nao apagar lock porque uma task demora;
   consultar a operacao proprietaria e sua saude.
4. API task aceita exige acompanhar UPID ate status terminal, ler exitstatus
   e reconsultar objeto. Timeout do cliente nao prova task remota parada.
5. Clone/restore usam identificador livre consultado, run_id e isolamento
   validado em todas as NICs; nunca VMID/VLAN fixa como garantia de seguranca.

## Storage e discos

Mapeie serial/device, volume, pool, VM e filesystem interno. Disco unused
pode conter dados ou rollback; ausencia de mount nao autoriza remover.
Separacao DATA/WAL em discos virtuais do mesmo pool nao cria independencia
fisica. Planeje espaco temporario, snapshots, thin provisioning e crescimento.
OSD/formatacao/destroy/remove exigem aprovacao humana de alvo e impacto.

## Aceite e rollback

PASS por camada: configuracao hypervisor, guest, rede, funcao e backup.
Preserve configuracao antes de mudar. Restore e cleanup seguem referencias
15/16, sem destroy automatico. Major upgrade, bridge/gateway de gestao e
alteracao de pool exigem planejamento de compatibilidade e risco especificos.

Fontes: [Proxmox VE administration](https://pve.proxmox.com/pve-docs/),
[API viewer](https://pve.proxmox.com/pve-docs/api-viewer/),
[Backup/Restore](https://pve.proxmox.com/pve-docs/chapter-vzdump.html).
