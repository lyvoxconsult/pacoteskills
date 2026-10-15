# Active Directory, GPO e experiencia do colaborador

Use para AD/DNS, governanca, shares, politicas e testes como usuario real.
Pre-condicoes: dominio/foresta previstos, DNS e tempo funcionais, principals
de teste aprovados, topologia e baseline; nao usar administrador para provar ACL.

## Dominio e identidade

Execute conforme papel/versao/permissao: Get-ADDomain, Get-ADForest,
Get-ADOrganizationalUnit, Get-ADGroup, Get-ADUser, Get-GPO, dcdiag,
repadmin quando houver contexto de replicacao e Resolve-DnsName para SRV.
Inspecione FSMO, zonas/registros DNS, OUs, delegacoes e membership efetivo.
AD DS instalado nao prova promocao, DNS ou logon funcional. Um DC unico
nao precisa ter replicacao multi-DC ficticia; registrar esse limite de resiliencia.

Separar contas comuns, administrativas e de servico; limitar logon e delegacao.
AGDLP: principal -> global role -> domain-local permission -> ACL. Inspecione
heranca, deny e membership aninhado; group existente nao prova permissao aplicada.
Verifique LAPS e seu acesso conforme produto/versao efetivos, sem imprimir senha.

## GPO e sessao

1. Inspecione links/OU, security filtering, WMI filters, precedencia e itens.
2. Valide gpresult/RSoP no usuario/computador correto, processamento e logs.
   GPO criada/linkada nao prova aplicacao.
3. Para drives: teste logon do usuario, Explorer/This PC, UNC por DNS,
   reconnect e logoff/logon. Script remoto como SYSTEM nao representa sessao.
4. Verifique protocolo real de SMB/Kerberos. UNC por IP pode nao seguir o
   caminho Kerberos esperado; nao declarar equivalencia de autenticacao.
5. Teste restricoes de usuarios comuns e administrativos conforme politica,
   sem capturar credenciais no console/relatorio.

## File Server

Get-SmbShare, Get-SmbShareAccess, Get-Acl, volumes, FSRM/quotas quando
requeridos, auditoria/SACL e backup. ACL NTFS e share permissions se combinam;
drive mapeado nao concede acesso. ABE oculta listagem, nao substitui ACL.
Testar READ/WRITE especificos e pasta proibida com identidade confirmada.
Qualquer cleanup de arquivo criado exige aprovacao; use objeto unico e ownership.
Classifique UnauthorizedAccess, autenticao falha, caminho ausente e timeout,
nao catch generico como acesso negado.

## Aceite e limites

E2E: usuario -> DNS/AD -> logon/Kerberos -> GPO -> share/app -> evento no coletor.
Desktop funcional nao prova toda politica. Registrar requisitos testados, N/A
e UNKNOWN. Nao instalar AD CS, DHCP/IIS no DC so porque outra empresa usa.
Alteracao/remocao de grupos, links ou regras exige analise e aprovacao de exclusao.

Fontes: [AD PowerShell](https://learn.microsoft.com/en-us/powershell/module/activedirectory/),
[GroupPolicy](https://learn.microsoft.com/en-us/powershell/module/grouppolicy/),
[Windows LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview).
