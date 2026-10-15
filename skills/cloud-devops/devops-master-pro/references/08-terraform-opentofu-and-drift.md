# Terraform/OpenTofu e drift

Use para provisionamento declarativo, importacao, plano e state. Entradas:
produto/versao, providers/modulos, backend, state/ownership, ambiente e acesso.
Terraform e OpenTofu nao sao intercambiaveis em todas as funcionalidades.

## Antes do plano

Fixe versoes compativeis e lockfile de providers, quando aplicavel. Separe
ambientes e limites de state por ciclo de vida/risco, nao cada VM por padrao.
Backend deve ter ACL, transporte/armazenamento protegidos, locking suportado
e recuperacao/versionamento. Nao copiar automaticamente mecanismos de locking
de uma versao antiga para outro backend/produto.

fmt/validate testam configuracao, nao seguranca ou funcionamento do recurso.
init pode baixar codigo; valide fonte/versao antes. State, plano salvo e JSON
podem conter secrets mesmo com sensitive. Proteja-os fora do Git e logs.
Credencial em ambiente tambem exige cuidado com heranca e saida de processos.

## Plano e aplicacao

1. Inventarie recursos existentes e leia state; importar/moved pode evitar
   recriacao. Nao executar state rm para ocultar drift sem aprovacao humana.
2. Gere plan no ambiente certo. Codigo de plan -detailed-exitcode tem semantica
   propria; nao tratar mudanca como falha ou sucesso operacional automaticamente.
3. Inspecione create/update/delete/replace/forget e efeitos indiretos de
   provisioners/scripts, politicas de lifecycle e servicos de dados.
4. Qualquer exclusao, substituicao ou retirada de gerenciamento exige aprovacao
   humana de alvo, impacto e plano. create_before_destroy continua excluindo.
   prevent_destroy nao protege recurso cuja configuracao foi removida.
5. Associe aprovacao a digest protegido do plano, ambiente, commit/versoes,
   prazo e recursos. Hash vincula artefato, nao autentica aprovador.
6. Aplique plano efetivamente revisado quando suportado. Mudanca/staleness
   exige nova revisao e novo aceite das exclusoes. -auto-approve nao e aprovacao
   humana; -target e excecao justificada, nao isolamento garantido.
7. Reconsulte tarefas/recursos/servicos e rode novo plan quando apropriado.
   Erro de apply pode deixar estado parcial; diagnosticar antes de retry.

## Auxiliar local de revisao

`python3 scripts/review_terraform_plan.py <protected-plan-json>` le JSON de
`terraform show -json`/equivalente compativel. Nao gera plano, nao chama provedor,
nao escreve arquivo e nunca autoriza apply. Exit 0: nenhuma exclusao reconhecida;
3: revisao humana exigida; 2: formato/entrada incompleta nao analisavel.

Nao imprima JSON bruto no terminal. O auxiliar mostra apenas enderecos e acoes;
enderecos podem conter metadados privados e a saida tambem deve ser protegida.
Formato desconhecido ou plano incompleto falha fechado. Ausencia de delete
explicito nao detecta exclusoes dentro de update/script/provisioner ou politicas
remotas; revise codigo e o plano integral em ambiente protegido.

Objetos deposed sao identificados por address e chave deposed em conjunto;
o auxiliar preserva ambos para revisar a exclusao do objeto antigo, sem
confundi-lo com a instancia atual. JSON com chaves repetidas e rejeitado.

Para testar sem infraestrutura, execute o leitor com
[plano sintetico](../assets/terraform-plan.example.json); deve retornar exit 3,
listar a exclusao do objeto deposed e manter authorization_granted false.
Essa fixture nao e um plano de provedor e nunca deve ser passada para apply.

## Recuperacao e aceite

Preserve state antes de operacoes de maior risco e confirme lock proprietario
antes de force-unlock. Voltar state antigo nao reverte recursos cloud. Rollback
de configuracao tambem gera plano e pode incluir exclusoes: novo gate.
Aceite: drift explicado, plano correto, lock/ACL verificados, apply terminal e
funcionalidade testada. Nao executar destruicao para fazer codigo parecer limpo.

Fontes: [plan](https://developer.hashicorp.com/terraform/cli/commands/plan),
[sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data),
[lifecycle](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle),
[JSON plan format](https://developer.hashicorp.com/terraform/internals/json-format),
[OpenTofu docs](https://opentofu.org/docs/).
