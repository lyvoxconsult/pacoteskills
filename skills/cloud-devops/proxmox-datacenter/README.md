# Proxmox Datacenter Pack

Subpasta curada para Proxmox VE, MCPs Proxmox e gerenciamento de datacenter.
Ela isola tudo em um unico pacote para nao baguncar a ordem do catalogo geral de
skills do repositorio.

## Conteudo

- `skills/core/`: skills Proxmox da pesquisa original.
- `skills/complementares/`: skills relacionadas para automacao, rede, dados, storage, monitoramento e MCP.
- `mcp-servers/`: snapshots dos MCPs/ferramentas baixados do GitHub, sem `.git`, `node_modules`, `.venv` ou caches.
- `SOURCES.md`: fontes usadas e observacoes de validacao.
- `OPERATIONS.md`: fluxo seguro para usar agents/MCPs contra Proxmox real.
- `MANIFEST.md`: lista resumida do pacote.

## Como usar em conjunto

1. Comece por `proxmox-datacenter/SKILL.md`.
2. Escolha uma skill principal:
   - API/REST e scripts: `openclaw-proxmox-api`
   - Status e power management: `openclaw-proxmox-skill`
   - CLI admin: `bastos-proxmox-admin`
   - Referencia operacional ampla: `waypoint-proxmox`
   - Automacao idempotente: `ansible-proxmox`
   - Onboarding/manutencao por plugin: `proxmox-mgmt-onboard` e `proxmox-mgmt-maintenance`
3. Para operacao real, escolha um MCP em `mcp-servers/` e configure somente com variaveis locais.
4. Use complementares para fechar lacunas: rede, Terraform, monitoramento, dados, database, governanca MCP e recuperacao de VMs.

## Regras de seguranca

- Nao usar credenciais reais em arquivos versionados.
- Nao executar acoes destrutivas sem confirmar VMID/CTID, node, backup/snapshot e impacto.
- Preferir tokens Proxmox de menor privilegio.
- Separar ambientes de teste e producao.
- Registrar limites: sem cluster real, a validacao fica restrita a estrutura, docs e ausencia de segredos.

## MCPs incluidos

- `RekklesNA-ProxmoxMCP-Plus`
- `antonio-mello-ai-mcp-proxmox`
- `heybearc-mcp-server-proxmox`
- `ry-ops-proxmox-mcp-server`
- `Bldg-7-proxmox-mcp`
- `danielrosehill-Proxmox-Mgmt-Plugin`
- `canvrno-ProxmoxMCP`

## Complementos incluidos

- Proxmox MCP tool reference
- Proxmox infrastructure
- Proxmox VE reference
- Proxmox host operator
- Proxmox system administration
- Proxmox VM recovery
- Proxmox Mgmt Plugin onboarding/manutencao
- MCP builder/integration/governance
- Network engineer
- Hybrid cloud networking
- Terraform
- Monitoring
- Data engineer
- Database
