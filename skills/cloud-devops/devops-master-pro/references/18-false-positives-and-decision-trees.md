# Falsos positivos e arvores de decisao

Use quando um resultado superficial parece suficiente ou diagnostico entrou em loop.

## Acesso interno nao funciona

Hypervisor controla recurso? Se nao, verificar identidade/API/ACL. VM inicia?
Se nao, examinar task/console/disco/boot. SO instalado? Se nao, bootstrap
autorizado. IP/rota/listener certos? Se nao, diagnosticar camada. Autenticacao
negada? Verificar principal/protocolo/certificado, nao abrir firewall inteiro.
Console/QGA sao alternativas, nao evidencia de experiencia do usuario.

## Teste negativo de rede/ACL

Destino saudavel e controle positivo existe? Se nao, negativa inconclusiva.
Identidade e caminho corretos? Se nao, corrigir teste. Erro identificado de
permissao ou regra corroborada? Se sim, registrar operacao negada esperada.
Timeout sem log/captura? UNKNOWN, nao PASS. Revise IPv6, states e caminho
alternativo. Nao forcar log/captura intrusivo sem considerar risco e dados.

## Backup e restauracao

Ha politica? Configurado. Ha task terminal e artefato consistente? Executado.
Verificacao da ferramenta valida escopo? Verificado. Restore funcional no
nivel requerido passou? Recuperabilidade comprovada naquele teste/data.
Somente boot ou copia de dump? Nao elevar a servico/banco restaurado.
Destino mesmo host/pool? Limite de falha compartilhada, nao independencia.

## Evidencia contraditoria

Compare horarios/metodos/identidades/versoes. Prefira observacao recente
adequada ao criterio, mas preserve prova historica. Epoch deslocado nao
se corrige na narrativa dizendo timezone. Agentes nao podem eleger a saida
mais favoravel sem explicar conflito ou coletar nova evidencia.

## Exclusao detectada

Direta, replace, prune, rollout, cleanup ou state forget? Gate humano.
Ownership/run_id confirmados nao dispensam aprovacao. Politica recorrente
sem aceite especifico? Somente candidatos/alerta. Artefato de aprovacao
autogerado por agente? Nao e autoridade humana confiavel.

## Antipadroes e substitutos

| Atalho | Substituto |
|---|---|
| Restart indefinido | Hipotese, log, teste limitado, causa raiz |
| Everyone/Admin/ANY permanente | Menor privilegio e teste de fluxo |
| Catch generico = DENIED | Classificar erro e confirmar identidade |
| --check = idempotente | Suporte por tarefa e segunda execucao observada |
| SHA-256 = assinatura | Referencia confiavel/assinatura quando requerida |
| try/finally = limpeza garantida | Journal, ownership e reconciliacao com gate |
| Kubernetes/HA para tudo | Tradeoff proporcional a requisito |
| Documento homologado = verdade atual | Prova operacional por criterio |
| Skill/MCP citado = disponivel | Resolver, autenticar e testar permissao |

Depois de tres tentativas sem nova evidencia, reveja a hipotese e reduza
escopo do teste. Nao continuar mudancas aleatorias nem declarar bloqueio externo
apenas porque diagnostico e dificil. Interrompa em risco/gate real.
