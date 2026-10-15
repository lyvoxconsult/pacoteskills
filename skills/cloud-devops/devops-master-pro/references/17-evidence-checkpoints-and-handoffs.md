# Evidencia, checkpoints e retomada

Use para auditoria, trabalho longo, troca de agente e conclusao. Templates em
[assets](../assets/templates.md) e [registro sintetico](../assets/evidence-record.example.json).

## Registro por criterio

run_id, horario UTC, ambiente/recurso/owner, requisito, identidade/papel,
metodo e versao, esperado/observado, status, referencia protegida e incerteza.
Referencia sem artefato acessivel nao comprova PASS; registrar essa limitacao.
Hash so autentica integridade relativa a referencia confiavel, nao autoria.

| Status | Uso |
|---|---|
| PASS | Criterio verificado com evidencia suficiente |
| PARTIAL | Parte observada, requisito ainda nao integral |
| FAIL | Evidencia de comportamento/configuracao contraria ao criterio |
| NOT IMPLEMENTED | Ausencia de implementacao observada |
| NOT APPLICABLE | Fora do escopo com justificativa |
| UNKNOWN | Dados insuficientes ou teste inconclusivo |
| BLOCKED | Falta concreta de acesso/autorizacao/dependencia para executar |

Risco aceito nao e status PASS. Plan/config/task accepted/terminal/protocol
success sao etapas distintas. Teste negativo que falha por DNS nao comprova ACL.
Nao aplicar uma evidencia antiga como estado atual sem revalidar fatos mutaveis.

## Protecao e documentacao

Raw logs/planos/screens podem conter dados privados. Coletar campos allowlisted,
minimizar, redigir estruturalmente e revisar antes de distribuir. Regex ajuda,
nao garante sanitizacao. Nada sensivel em Git, exemplo ou memoria publica.
Usar nota oficial existente para estado/decisoes; novo documento apenas se
resolver lacuna organizacional. Historico nao deve ser reescrito para esconder erro.

## Checkpoint e handoff

Registre objetivo/escopo, fontes, recurso/task ID e owner, mudancas efetuadas,
testes/status/evidencias, riscos/gates, temporarios pendentes e retomada segura.
Nao transportar segredos; indicar cofre e procedimento de acesso protegido.
Ao retomar: ler checkpoint, verificar tasks ainda ativas e estado real antes
de repetir mutacoes. Nao interpretar ausencia de narracao como conclusao.

Coordenacao: especialistas leem areas independentes; owner unico por firewall,
state e recurso compartilhado. Auditor recebe requisitos e evidencia bruta
minima protegida, nao somente conclusao do implementador. Se nao houver agente
independente real, descrever como autorrevisao.

## Aceite

Declarar implementado/testado/nao testado separadamente. Bloqueio exige causa
exata; dificuldade normal pede investigacao. Gate de exclusao nao pode ser
contornado para satisfazer pedido de nao parar. Objetivo sem pendencias depende
de criterios verificaveis, nao de expressao 100% ou checklist marcado.
