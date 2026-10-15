# Backup, NAS e disaster recovery

Use para politica, execucao, verificacao, retencao e restore. Entradas:
inventario/dados, consistencia, destinos, dominio de falha, agendas/timezone,
RPO/RTO, capacidade, chaves e acesso de emergencia.

## Politica

Mapeie por VM, host/config, identidade/System State, DB/app e shares/NAS.
Especifique ferramenta, job, tipo, origem, destino, escopo/discos incluidos,
janela, consistencia (VSS/guest freeze quando suportado), retries/alertas,
verificacao e restore. Criptografia requer chave recuperavel fora do dominio
de falha do unico backup. Snapshot nao e copia independente.

Incremental exige mecanismo real, nao modo snapshot ou nome do arquivo.
PBS possui semantica de chunks/indices/deduplicacao; cadeia tradicional de
incrementais possui dependencias diferentes. Nao gerenciar os dois apagando
arquivos genericamente por data. Prune e GC sao etapas distintas no PBS e
ambas exigem aprovacao humana especifica.

Exemplo de agenda, nao default universal: dias uteis 19h; fim de semana
madrugada em horario exato e timezone registrados. Calcule proxima execucao,
incluindo mudanca de calendario/timezone, e confirme job terminal/log.
Catalogo precisa de data/hora, origem, tipo, job, tamanho, integridade e status.
Cinco ultimos significa cinco pontos recuperaveis no escopo/classe aprovado;
nao apagar dependencias nem supor aprovacao de prune a partir dessa meta.

## NAS

VM NAS no mesmo host demonstra integracao, nao independencia contra perda
do Proxmox/pool. Registre 3-2-1/offsite/imutabilidade como estrategia conforme
risco e recursos, sem afirmar implementacao pelo numero de destinos virtuais.
Evite circularidade de restore: NAS nao pode depender exclusivamente de backup
localizado nele mesmo. Considere recuperacao de AD, chaves e rede do destino.

Diretoria pode ter visibilidade do catalogo/copias conforme politica,
preferencialmente somente leitura. Nao conceder escrita no repositorio
privilegiado nem acesso irrestrito a dados confidenciais dentro de dumps.
Pastas separadas para servidores, VMs e shares ajudam navegacao; validar ACL
real e integrity/copy status, nao apenas existencia de diretorio.

## Restore funcional

1. Escolha backup, escopo, destino livre e aprovacao do teste/cleanup. Confirme
   espaco e isolamento de todas as NICs/rotas; nao usar ID ou VLAN fixos.
2. Acompanhe restore task ate terminal e confirme ownership/run_id do destino.
3. Valide boot/SO/rede isolada e servico; para banco, carregar dump/backup e
   consultar objetos/dados. Para arquivos, validar conteudo e ACL necessarios.
4. Teste funcao e dependencias no isolamento apropriado. Clonar DC exige
   procedimento especifico; nao ligar clone na rede do dominio original.
5. Meca fases e RTO total ate servico contratado disponivel; RPO usa ultimo
   ponto comprovadamente recuperavel/transacao, nao nome do arquivo.
6. Cleanup permanece pendente sem aprovacao humana e ownership comprovados.

## Aceite e falhas

Separe configurado, executado, verificado e restaurado. Hash igual e evidencia
de igualdade do objeto medido, nao funcionalidade ou autenticidade universal.
Falha de backup implica janela de risco: alertar, diagnosticar e repetir quando
seguro, sem apagar ultima copia boa para liberar espaco automaticamente.
Nao prometer perda zero quando RPO permite perda entre jobs.

Fontes: [PVE backup](https://pve.proxmox.com/pve-docs/chapter-vzdump.html),
[PBS backup client](https://pbs.proxmox.com/docs/backup-client.html),
[PBS storage model](https://pbs.proxmox.com/docs/technical-overview.html).
