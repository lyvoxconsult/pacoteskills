# Acesso e bootstrap

Use quando nao esta claro como entrar, quem pode acessar, onde consultar
credenciais ou se o canal representa a identidade que precisa ser testada.

## Registro protegido de acesso

Use o [template](../assets/templates.md). Por recurso, registre owner,
endpoint/protocolo/porta, rede/VPN/bastion, certificado ou host key esperados,
principal humano/servico, grupo e privilegio, referencia ao item do cofre,
aprovador e revisao. O registro fica na documentacao protegida do projeto,
nao nos exemplos distribuidos desta skill. Nunca escreva senha ou token.

## Escolha e validacao do canal

| Objetivo | Canal e limite |
|---|---|
| Inventario e lifecycle | API/CLI nativa; verificar ACL no endpoint |
| Configuracao Linux | SSH com host key validada, privilegio proporcional |
| Configuracao Windows | WinRM/PowerShell Remoting com transporte/autenticacao adequados |
| Recuperacao sem IP | QGA suportado ou console autenticado |
| Experiencia do colaborador | Sessao interativa do usuario real |
| Servico gerenciado | API e transacao; nao exigir acesso ao SO |

Antes de mudar: confirme fingerprint, nome, ID e ambiente. HTTP 200 com
inventario vazio pode ser ACL/escopo, nao ausencia de recursos. Em Proxmox,
token com separacao de privilegios pode ter autorizacao diferente da conta;
consulte permissoes efetivas, nao apenas o nome do role.

## Bootstrap

1. Diagnostique boot, instalador/OOBE, interface, rota e listener usando controle
   ou console quando SSH/WinRM nao existirem. Falta de acesso e pendencia,
   mas nao prova automaticamente que a rede falhou.
2. Escolha bootstrap suportado: cloud-init/Autounattend, imagem, console ou QGA.
   Cloud-init provisiona; nao e um canal generico permanente de acesso.
3. Restrinja origem, conta, privilegio e prazo. Confirme acesso antes de fechar
   o canal de recuperacao. Remocao de regra/conta temporaria exige gate humano.
4. Execute consulta inofensiva de identidade/hostname e valide logs de acesso.
5. Teste uma negativa controlada sem brute force, lockout ou credencial exposta.

WinRM autenticado nao e o token da sessao Explorer e pode ter restricoes de
delegacao/double-hop. QGA frequentemente executa com privilegio elevado;
nao usar seu resultado para provar permissao de usuario comum.

## Seguranca e aceite

Verifique origem permitida, TLS/host key, grupos e privilegios efetivos,
cofre e logs. Conta admin compartilhada limita atribuicao individual; cofre
nao elimina essa limitacao. Nao desabilite verificacao de certificado como
solucao permanente. Nao copie senha para argumento de processo ou screenshot.

PASS do acesso administrativo nao conclui a funcao do servidor. Se um
bootstrap expuser acesso ou falhar, preservar canal seguro, diagnosticar
logs e obter aprovacao para remover/reverter objetos quando necessario.

Fontes: [PowerShell Remoting](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/powershell-remoting-faq),
[Proxmox API](https://pve.proxmox.com/wiki/Proxmox_VE_API).
