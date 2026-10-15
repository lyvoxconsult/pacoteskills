# Ansible e configuracao por maquina

Use para inventory, roles, manutencao manual legivel e idempotencia.
Entradas: inventory efetivo, versoes/collections, acesso e alvo autorizado.

## Organizacao

Adapte [inventory exemplo](../assets/ansible/inventories/example/hosts.yml).
host_vars/<host>.yml contem configuracao especifica nao secreta; group_vars
contem defaults comuns; roles implementam comportamento reutilizavel.
Identidade/IP nao devem ter donos conflitantes em varios arquivos.
Playbooks individuais, se uteis, apenas selecionam host e roles; --limit
com um playbook existente pode dispensar wrappers. Nao impor YAML ao Terraform.

Registre precedencia/overrides e dono do parametro. Arquivos menores devem
ser separados por responsabilidade, nao por limite arbitrario de linhas.
Referencia ao cofre nao recupera segredo sozinha: integrar lookup/plugin real,
validar versao e disponibilidade sem incluir valores no inventory.

## Execucao e idempotencia

1. Leia inventory/vars/roles/tasks/handlers/templates e parametros do comando;
   confirme --list-hosts e inventory resolvido sem despejar secrets no log.
2. Verifique syntax/lint e collections instaladas. Prefira modulo nativo
   quando cumprir semantica/compatibilidade; nao presumir idempotencia pelo nome.
3. Inspecione suporte de check mode por tarefa. check_mode:false pode mutar
   mesmo com --check; diff pode revelar segredo. no_log/diff:false ajudam, mas
   nao protegem um codigo externo que imprime dados fora da tarefa.
4. Execute no escopo autorizado com janela/backup de configuracao adequados.
   command/shell precisam de predicados de estado e changed_when/failed_when
   honestos; nao usar failed_when:false para esconder falha requerida.
5. Reexecute quando apropriado. Mudancas de segunda rodada exigem explicacao;
   timestamp/refresh inevitavel difere de reconfiguracao inesperada.

## Gates

state: absent, cleanups, formatacao, replace indireto e rotinas de prune
precisam de aprovacao humana. Nao esconder essas tarefas em handler ou tag.
Para rede remota: validar sintaxe, acesso de recuperacao e escopo antes de
recarregar. Atualizacao manual deve voltar a fonte declarativa e ser revalidada.

Aceite: host certo, variaveis efetivas conhecidas, resultado funcional,
segunda execucao explicada e exclusoes bloqueadas sem aprovacao.
Templates de exemplo sao dados sinteticos, nao playbooks homologados em hosts.

Fontes: [inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html),
[check/diff](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html),
[Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html).
