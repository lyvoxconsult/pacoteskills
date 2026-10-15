# Cofre, aprovacao humana, risco e custos

Leia antes de secrets ou qualquer operacao com exclusao direta/indireta.

## .env e cofre

Fonte de verdade: cofre aprovado com criptografia, ACL e trilha de acesso
adequadas. Pasta chamada cofre, .gitignore ou arquivo oculto nao comprovam
essas propriedades. Preferir entradas individuais/injecao minima em runtime;
se .env completa for necessaria, guarda-la como item protegido do cofre.
Nao incluir senha/chave de abertura no mesmo pacote protegido.

Copia local indispensavel fica fora do Git, restrita, com prazo/risco e backup
sensivel; sua remocao tambem exige aprovacao humana. Preferir memoria para
evitar passivo temporario. .env.example usa placeholders, nao valores reais.
Ansible Vault protege conteudo cifrado, mas nao substitui identidade/auditoria
de leitura de um servico de cofre. Declare limitacoes do produto escolhido.

Verifique recuperacao sem imprimir segredo, negativa de principal nao
autorizado, ACL, autenticacao, log de acesso quando suportado e recuperacao
de emergencia. Ferramenta sem esses controles nao recebe PASS generico.
Env vars, no_log e redacao nao sao garantia absoluta contra exfiltracao.

## Gate humano de exclusao

**Nenhuma exclusao sem aprovacao humana explicita anterior.** Inclui VMs,
containers/pods, discos/pools, arquivos/objetos de teste, dados/DB, backups,
snapshots, prune/GC/TTL, usuarios/grupos, regras/registros, recursos cloud e
retirada de gerenciamento (state rm/forget). Formatacao/sobrescrita destrutiva
e rollback com perda de dados tambem exigem gate.

1. Identifique alvos/owner, motivo, operacao exata, impacto/dependencias,
   recuperabilidade e alternativa nao destrutiva.
2. Apresente lote enumerado ou politica recorrente especifica e obtenha aceite
   humano antes de executar. Autonomia, laboratorio e instrucao termine tudo
   nao substituem esse aceite. Subagente nao aprova em nome do humano.
3. Registre aprovador, evidencia confiavel do aceite, momento, escopo/plano,
   validade e limites. Um JSON dizendo approved: true nao autentica o aprovador.
4. Reconfirme recurso e plano. Novo alvo, plano alterado ou aprovacao expirada
   invalida a permissao; falhar fechado e obter novo aceite.
5. Execute apenas escopo aprovado e documente resultado. Sem aprovacao,
   gere candidatos e risco/capacidade, nao exclua nem esconda cleanup em handler.

Agenda/meta de retencao nao autoriza prune. Uma politica recorrente pode ser
aprovada explicitamente com criterios, classe, owner, validade e limites;
somente essas exclusoes ficam cobertas. Avalie deletions indiretas de rollout,
GitOps, object lifecycle, rotacao e pipelines, nao apenas comandos delete.
Este procedimento depende de enforcement do runner/plataforma; texto de skill
nao garante impedir bypass. Descreva quais gates estao efetivamente instalados.

## Risco, seguranca e FinOps

Menor privilegio, segregacao, TLS, hardening, patches e logs conforme workload.
Excecao lab e risco aceito com owner/prazo, nao baseline de producao. Nao executar
pentest/forca bruta por skill instalada; exige escopo/autorizacao especificos.
Analise de compliance nao equivale a certificacao.

Custos: baseline, tags/owner, janela de uso, budgets, egress e rightsizing
medido. Recurso ocioso pode guardar backup/DR ou dependencia infrequente;
nenhum cleanup automatico sem gate. Medir custo/impacto depois da mudanca.

Fontes: [Ansible Vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html),
[Terraform sensitive](https://developer.hashicorp.com/terraform/language/manage-sensitive-data),
[FinOps Framework](https://www.finops.org/framework/).
