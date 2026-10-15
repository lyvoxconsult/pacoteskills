# Templates de trabalho

Copiar/adaptar na documentacao protegida do projeto. Nao versionar registros
reais de acesso, evidencia bruta, endpoints administrativos ou secrets na skill.
Templates nao constituem aprovacao ou prova de teste.

## Registro de acesso

| Campo | Conteudo requerido |
|---|---|
| Recurso/ambiente/owner | Identificador estavel e responsavel |
| Como conectar | Protocolo, endpoint/porta, VPN/bastion/rede de origem |
| Confirmar destino | Certificado/host key e ID esperados |
| Quem acessa | Conta/grupo humano, servico ou automacao e privilegio efetivo |
| Cofre | Referencia ao item protegido, nunca segredo |
| Autorizacao | Aprovador, escopo, prazo e revisao |
| Evidencia | ACL, teste positivo/negativo e logs de autenticacao |
| Emergencia | Canal independente e procedimento protegido |

## Matriz de gap/aceite

| Componente | Requisito | Real observado | Status | Evidencia | Acao | Dependencia | Risco/gate |
|---|---|---|---|---|---|---|---|
| <resource> | <criterion> | <observation> | UNKNOWN | <protected-ref> | <action> | <dependency> | <risk> |

## Pedido de aprovacao de exclusao

Operacao: <exact-operation>. Ambiente/owner: <scope>.
Alvos enumerados: <stable-identifiers>. Motivo: <reason>.
Impacto/dependencias: <impact>. Recuperabilidade: <tested-recovery-or-limit>.
Alternativa nao destrutiva: <alternative>. Plano/commit: <protected-digest>.
Validade/limites: <window-and-bounds>.

Registrar aceite humano autentico na ferramenta/documentacao protegida.
Nao preencher aprovado pelo proprio agente. Mudanca de plano/alvo exige
novo aceite. Para politica recorrente, especificar algoritmo, classes, escopo,
validade e limites; meta de retencao nao basta.

## Checkpoint/handoff

Objetivo e escopo autorizado: <goal>.
Fontes e versoes consultadas: <sources>.
Recursos, owners e tasks ainda ativas: <ids>.
Mudancas feitas e estado reconsultado: <observations>.
Testes/evidencias por criterio: <results-and-protected-refs>.
Gates, riscos e temporarios pendentes: <pending>.
Retomada segura: <first-read-only-check>.
Credenciais: somente referencia ao cofre e procedimento de acesso.

## Relatorio de entrega

Declarar artefato local, instalacao e publicacao separadamente. Para ambiente:
listar criterios comprovados, falhas, UNKNOWN/BLOCKED e motivo exato;
distinguir implementacao, execucao, validacao e restore. Nao dizer 100% quando
ha testes faltando. Nao apresentar fixture/mocks como teste de infraestrutura.
