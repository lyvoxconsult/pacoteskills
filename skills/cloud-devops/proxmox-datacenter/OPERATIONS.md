# Fluxo Operacional Seguro

Use este fluxo antes de permitir que um agente ou MCP atue sobre Proxmox real.

## 1. Inventario primeiro

- Identificar cluster, nodes, storage pools, bridges, VLANs, VMs, LXCs e backups.
- Ler estado via API/MCP/CLI antes de propor mudanca.
- Conferir VMID/CTID, node atual, tags, HA, snapshots e tarefas em andamento.

## 2. Permissao minima

- Criar API token dedicado por agente ou workflow.
- Conceder apenas permissoes exigidas pela tarefa.
- Separar tokens read-only de tokens de escrita.
- Nunca gravar token em `README`, `.env`, config versionado ou historico de terminal compartilhado.

## 3. Mudancas com impacto

Antes de start, stop, reboot, shutdown, migrate, restore, rollback, delete,
resize ou alteracao de rede/storage:

- Confirmar alvo exato: node + VMID/CTID + nome.
- Confirmar impacto esperado.
- Confirmar backup ou snapshot recente quando aplicavel.
- Confirmar rollback.
- Executar primeiro em ambiente de teste quando houver risco operacional.

## 4. MCPs

- Tratar MCP como ferramenta com acesso operacional real.
- Revisar lista de ferramentas e permissoes antes de conectar ao cluster.
- Bloquear ou exigir aprovacao para ferramentas destrutivas.
- Usar allowlists para host/origin quando MCP HTTP estiver exposto.
- Preferir stdio/local quando nao houver necessidade de endpoint remoto.

## 5. Evidencia de validacao

Ao concluir uma tarefa, registrar:

- comandos ou ferramentas usados;
- saidas relevantes, sem segredos;
- arquivos alterados;
- testes executados;
- lacunas nao testadas;
- risco residual.
