# Proveniencia e manutencao

Versao inicial: 1.0.0. Conteudo original destilado, criado em 2026-10-05.
Nao incorpora copias integrais de skills externas, logs, secrets ou scripts
operacionais Antlia. O pacote nao pretende redistribuir materiais de licenca
incerta; antes de incorporar novos trechos, revisar atribuicao/licenca.

## Fontes utilizadas

| Fonte | Contribuicao | Alcance |
|---|---|---|
| Conversa e proposta DevopsMasterPro aprovada para criacao | Contrato, cofre, YAML por host, acesso e gate humano | Requisitos do usuario; nao prova de infraestrutura atual |
| Historico documental/evidencias Antlia | Falsos positivos de clocks, ACL, backup/restore e sessao | Exemplos sanitizados; nao certificacao atual |
| book-to-skill | Destilar frameworks, decisao e antipadroes | Metodo, sem copiar manual |
| devpromptarchitect | Escopo, risco, testes, aceite e autonomia limitada | Metodo para instrucoes operacionais |
| skill-creator | Frontmatter, UI e progressive disclosure | Formato de skill e avaliacao |
| cloud-devops e entradas selecionadas | Cobertura de nuvem/IaC/rede/entrega | Leitura seletiva; nao alegacao de todo catalogo lido |
| Documentacao oficial vinculada por referencia | Semantica e versoes | Revalidar antes de operacao sensivel a versao |

Baseline local do catalogo na criacao:
`323c22dfe4c8a474ccbdeabc526aed16b0252635`.
O baseline identifica a fonte consultada, nao o commit deste pacote novo.
Entradas consultadas nesta criacao incluem cloud-devops, ansible-proxmox,
devops-troubleshooter, network-engineer, cloud-architect, terraform-specialist,
windows-shell-reliability e deployment-pipeline-design. A proposta anterior
tambem registrou descoberta e leitura seletiva de outras entradas pertinentes.
Inventario de nomes nao implica leitura integral ou teste funcional.

Fontes primarias verificadas para as regras mais frageis: Terraform plan,
lifecycle/removed e sensitive/state; Ansible inventory/check mode; pfSense
states; PBS prune/GC. Os demais links de referencia sao pontos de consulta,
nao uma afirmacao de verificacao integral de cada manual nesta criacao.

## Fatos, interpretacoes e limites

- Fato historico: coleta Epoch mostrou offset de aproximadamente quatro horas;
  survey posterior entre peers nao comprovou referencia externa correta.
- Fato historico: evidencia de restore combinou task/boot e hash de copia de
  dump; isso tem alcance menor que recuperacao funcional de banco/aplicacao.
- Interpretacao aplicada: status deve acompanhar criterio e qualidade da
  prova, nao a conclusao favoravel de um relatorio anterior.
- Preferencia do usuario: nenhuma exclusao sem aceite humano; nao e uma
  alegacao de comportamento padrao de todas as ferramentas DevOps.
- Sem homologacao ao vivo de ambientes, playbooks ou conectores por criar
  esta skill. Avaliacoes locais usam entradas sinteticas e revisao comportamental.

## Manutencao

Atualizar por falha demonstrada, mudanca de produto ou requisito aprovado.
Para nova fonte: registrar URL/caminho portavel, versao/data, parte lida,
licenca quando houver reutilizacao e alcance da conclusao. Nao juntar manuais
inteiros, usar arquitetura Antlia como default ou acrescentar dependencia
ficticia. Preservar historia sem secrets e rotular resultados nao executados.

Instalacao no agente e publicacao remota sao etapas separadas da criacao
no catalogo fonte; verificar cada uma antes de declara-las concluidas.

Resultados da criacao: [validacao local e independente](../evals/validation-results.md).
