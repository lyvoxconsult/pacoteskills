# CI/CD, entrega e rollback

Use para pipelines, releases e automacao de infraestrutura. Entradas: repo,
branch/commit, artefato, ambiente, runner, credenciais, gates e criterio de saude.

## Desenho e execucao

1. Separe build/test/promocao/deploy/validacao; promova o mesmo artefato
   identificado, nao recompilar versao diferente para cada ambiente.
2. Valide fontes e dependencias/actions, acesso do runner e protecao de branch.
   Nome environment: production nao comprova revisores habilitados. Atraso
   automatico nao e aprovacao humana.
3. Injete secrets por cofre/identidade temporaria quando suportados; previna
   exfiltracao por workflow de origem nao confiavel, logs e artefatos.
4. Escolha rolling, blue-green ou canary conforme capacity, routing e dados.
   Canary nao exige service mesh universal; exige controle real de trafego e
   criterios. Rolling nao garante zero downtime por nome.
5. Antes de deploy, revisar exclusoes indiretas: prune, cleanup, lifecycle,
   replace, pods antigos e migracao destrutiva. Gate humano especifico.
6. Acompanhe job/release ate terminal e valide transacao, erro/latencia e
   consistencia de dados durante janela suficiente; health 200 pode ser raso.

## Rollback

Defina gatilhos, versao anterior, compatibilidade de schema, dados e dependencias.
Voltar imagem nao desfaz DROP ou migracao irreversivel. Use expand/contract
quando apropriado; contract/remocao exige aprovacao humana.
Rollback automatizado que exclui recursos tambem exige escopo humano aprovado;
nao esconder essa operacao em if: failure().

## Aceite e limites

Artefato/commit/ambiente verificados, gate real, deploy observado e servico
funcional. Teste de pipeline com mocks nao prova deploy em cloud/producao.
Preserve trilha de aprovador/job, sem segredos. Pipeline pode falhar depois de
mutacao parcial: descobrir estado real antes de reexecutar.

Fontes: [GitHub deployment environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment),
[GitLab deployment approvals](https://docs.gitlab.com/ci/environments/deployment_approvals/).
