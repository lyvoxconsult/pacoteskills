# Configuracao interna Linux/Windows

Use para comprovar o SO e sua funcao, alem de hardware e status hypervisor.
Entradas: versao esperada, baseline, funcao, identidade da coleta e requisitos.

## Matriz interna

| Camada | Linux | Windows |
|---|---|---|
| Identidade/versao | hostnamectl, os-release | Get-ComputerInfo, hostname |
| Rede/DNS/rotas | ip, resolvectl/dig | Get-NetIPConfiguration, Get-NetRoute, Resolve-DnsName |
| Tempo | timedatectl, cliente NTP instalado | w32tm /query /status e /source |
| Discos/mounts | lsblk, findmnt, df | Get-Disk, Get-Volume, Get-Partition |
| Servicos/processos | systemctl, ps | Get-Service, Get-Process |
| Portas | ss -lntup | Get-NetTCPConnection, Get-NetUDPEndpoint |
| Logs | journalctl e logs nativos | Get-WinEvent com filtro e limite |
| Firewall/usuarios | nft/iptables conforme produto, id/getent | Get-NetFirewallProfile/Rule, grupos locais/AD |

Nao executar todas as ferramentas indiscriminadamente. Confirme disponibilidade
e privilegio; ss sem privilegio pode omitir processo, nao listener. Get-WindowsFeature
e ferramenta de Windows Server, nao requisito de Windows Client.

## Procedimento

1. Verifique instalacao concluida, boot no disco, drivers/VirtIO/QGA quando
   aplicaveis, hostname, IP/CIDR/gateway/DNS, timezone e fonte temporal.
2. Compare discos, arquivosystems, mounts, espaco e servicos com arquitetura;
   ativo no meta-servico nao implica instancia do banco saudavel.
3. Compare listeners com servicos esperados e origem autorizada. Porta
   desnecessaria precisa de analise de dependencias antes de fechar/remover.
4. Verifique updates, firewall, usuarios/grupos, privilegios, autenticacao,
   contas de servico e hardening proporcional. Patch/reboot precisa de janela,
   compatibilidade e validacao posterior, nao major upgrade por conveniencia.
5. Teste dependencia, logging e backup; aplique teste especifico da funcao.

## Interpretacao e recuperacao

Ausencia de SSH/WinRM: distinguir listener, firewall, autenticacao, DNS e SO
incompleto antes de bootstrap. Active nao comprova configuracao correta;
servico escutando em todas as interfaces exige confronto com fluxo autorizado.
Nao desativar Defender/firewall ou elevar todo usuario para reparar sintomas.

Em edicoes manuais, preservar configuracao, validar parser nativo quando
disponivel, aplicar escopo minimo e confirmar persistencia. Remocao de conta,
pacote, arquivo ou regra exige aprovacao humana; nao cleanup automatico.
PASS identifica criterio testado, nao uma etiqueta global de VM saudavel.

Fontes: [systemd manuals](https://www.freedesktop.org/software/systemd/man/latest/),
[Windows PowerShell modules](https://learn.microsoft.com/en-us/powershell/module/).
