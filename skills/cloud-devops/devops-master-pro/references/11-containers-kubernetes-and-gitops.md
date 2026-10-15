# Containers, Kubernetes e GitOps

Use apenas quando existentes ou justificados pela tarefa. Entradas:
runtime/cluster/context, namespace, imagens, owners, dados persistentes,
RBAC/CNI e ambiente. Nao introduzir cluster para resolver script simples.

## Container

Build reproduzivel, fonte confiavel, dependencias/versionamento, imagem por
digest quando viavel, usuario non-root conforme compatibilidade, capabilities
minimas, secrets fora de layers/build args e healthcheck funcional.
Confirme volumes e dados persistentes; container restarted nao prova app saudavel.
Limites de CPU/RAM e permissions precisam de teste com workload real.

## Kubernetes

1. Confirme contexto/namespace e identidade; leia objetos/events sem assumir
   que kubeconfig apontou para o ambiente solicitado.
2. Inspecione Deployment/StatefulSet, rollout, readiness/liveness/startup,
   requests/limits, OOM/throttling e disponibilidade dos endpoints.
3. Teste Service/Ingress/DNS/TLS e NetworkPolicy no CNI efetivo. Manifest
   criado nao prova enforce; pod Ready pode ter probe superficial.
4. Verifique ServiceAccount/RBAC, secrets, volumes/storage classes e backup
   dos dados. Backup de manifests/etcd nao garante restore de PV externo.
5. Teste transacao, politica negativa corroborada e logs; reconsulte depois
   da reconciliacao e janela de observacao.

## GitOps

Identifique repositorio, path, revisao, owner e reconciliador. Desired state
e intencao; Synced nao e saude funcional. Correcao manual pode ser revertida
automaticamente: alinhe ownership e fonte declarativa.
Auto-sync/prune nao recebe autorizacao por existir no manifesto. Exclusoes,
replace, garbage collection, TTL e finalizers precisam de analise e aprovacao
humana especifica. Atualizacao declarativa pode excluir pods antigos; avalie
essas consequencias antes de rollout, nao apenas kubectl delete explicito.

## Aceite e rollback

Deployment saudavel + transacao + dados + observabilidade no contexto certo.
Rollback pode excluir recursos ou conflitar com migracao de dados; requer gate
humano para exclusoes e estrategia de compatibilidade. Nao remover finalizer
ou PVC para fazer status ficar verde. Policy/CNI/provider sao sensiveis a versao.

Fontes: [Kubernetes docs](https://kubernetes.io/docs/),
[Docker build secrets](https://docs.docker.com/build/building/secrets/),
[OpenGitOps principles](https://opengitops.dev/).
