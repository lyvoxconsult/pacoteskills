# Conferencia do catalogo local — 2026-10-15

Comparacao por nome de pasta contendo `SKILL.md` entre os catalogos globais Codex/Agents e este repositorio, seguida de hash do `SKILL.md`. Nao e teste funcional de todas as skills nem inventario de arquivos auxiliares. MCPs e plugins foram conferidos separadamente em `mcp/`.

## Novidades incorporadas nesta atualizacao

- `business-analytics-master` criada em `skills/dados-analytics/`, com fontes e copias globais verificadas por hash.
- `composio-uso` e `devops-master-pro` ja estavam como arquivos locais pendentes de versionamento; foram preservados e revisados antes da publicacao. O segundo tem copia Antigravity identica e 24 testes locais aprovados.
- Nomes de MCPs e plugins observados na configuracao/cache atual foram registrados em `mcp/mcp-servers.md` e `mcp/plugins.md`, sem credenciais.

## Fora do repositorio por decisao anterior

Os unicos oito nomes de skill presentes na raiz dos dois catalogos globais e ausentes do repositorio sao `junta-leiloeiros`, `leiloeiro-avaliacao`, `leiloeiro-edital`, `leiloeiro-ia`, `leiloeiro-juridico`, `leiloeiro-mercado`, `leiloeiro-risco` e `pdf.backup.20260914_125842`. Os sete primeiros foram removidos intencionalmente do pacote em uma limpeza anterior; o ultimo e backup. Nao reintroduzir automaticamente.

## Conteudo local divergente ainda sem incorporacao

Ha 25 nomes cujo `SKILL.md` local nao corresponde ao hash de nenhuma copia homonima no repositorio. A diferenca **nao significa** que a versao local deva substituir a versionada:

- Referencias a leiloes removidos: `task-intelligence`, `multi-advisor`, `agent-orchestrator`.
- Trocas para caminhos absolutos desta maquina, que precisam ser neutralizados antes de qualquer publicacao: `10-andruia-skill-smith`, `earllm-build`, `claude-code-expert`, `007`, `speckit-updater`, `auri-core`, `context-guardian`, `skill-sentinel`, `context-agent`, `ai-studio-image`, `skill-installer`, `claude-monitor`, `advogado-criminal`, `instagram`, `image-studio`.
- Mudancas de conteudo/versao ou de formato que requerem revisao individual: `ui-ux-pro-max`, `impeccable`, `i-have-adhd`, `pdf`, `advogado-especialista`, `global-skills`, `aws-iam-best-practices`.

Antes de sincronizar uma dessas 25, comparar tambem referencias/scripts da pasta, manter portabilidade e revisar licenca, segredos e comportamento. A versao local das skills usadas nesta sessao nao foi sobrescrita.
