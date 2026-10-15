# Rede, pfSense, DNS e tempo

Use para conectividade, segmentacao, NAT, resolucao, firewall e timestamps.
Entradas: topologia, interfaces/MACs, bridges/VLANs, IP/CIDR, rotas, matriz de
fluxos, versao do produto, acesso administrativo e canal de recuperacao.

## Diagnostico por camadas

1. Verifique link, MAC e interface correta, bridge/trunk/tag e CIDR. VM ligada
   nao prova que o guest usa a NIC/VLAN/IP previstos.
2. Verifique rota de ida e volta, gateway, NAT e MTU quando houver perda parcial.
   Use ip addr/route e Get-NetIPConfiguration/Get-NetRoute nos sistemas corretos.
3. Separe DNS de acesso por IP: dig/Resolve-DnsName para o resolver escolhido,
   registros A/PTR/SRV quando aplicaveis e forwarders. Nao trocar DNS do membro
   AD por publico apenas para fazer internet funcionar.
4. Confirme listener e saude no destino, controle positivo pela origem autorizada
   e teste negativo pela origem proibida. nc/Test-NetConnection nao substituem
   transacao autenticada do protocolo.
5. Correlacione log/captura/state com fluxo unico e horario. Timeout sozinho
   e INCONCLUSIVO; recusa TCP tambem pode vir de servico ausente ou REJECT.

## pfSense

Verifique boot pelo disco, WAN, LAN/trunk, VLANs, IPs, gateways e default route,
NAT, aliases, regras ordenadas/floating, DHCP, Resolver/Forwarder, NTP,
administracao e logging. Inspecione persistencia e configuracao efetivamente
carregada, nao apenas config.xml salvo. O backup config.xml e sensivel.

Use GUI/console/SSH/API efetivamente suportados na versao. Antes de editar
config.xml, preserve copia protegida, valide sintaxe e conheca mecanismo nativo
de aplicar/recarregar. Nao prescrever pfctl -f de arquivo temporario como
substituto universal da configuracao gerenciada pelo produto.

Mudanca de regra pode deixar states antigos influenciando o teste. Inspecione
states e, se necessario, solicite aprovacao para remocao direcionada.
Reset global quebra conexoes e pode cortar a gestao; nao executar por rotina.
Aviso de crash exige logs/diagnostico antes de ser descartado.

## Firewalls em camadas

Compare origem, destino, porta, protocolo, direcao, acao e identidade onde
suportada em pfSense, Proxmox, firewall do SO e autorizacao da aplicacao.
Default deny e menor privilegio sao objetivos; nao aceitar ANY/ANY permanente
para contornar instalacao. Regra temporaria exige prazo e aprovacao de remocao.
Inclua IPv6 na analise ou documente claramente seu escopo, sem presumir que
bloqueio IPv4 cobre outro caminho.

## Tempo

Colete epoch, fonte, estado de sync e tempo de ida/volta. Compare com referencia
confiavel e estime incerteza; coletas sequenciais nao sao simultaneas. Tolerancia
vem do workload/politica, nao de limite universal de dois segundos. Em AD,
verifique PDC emulator e hierarquia configurada; free-running nao prova NTP.
Timezone altera apresentacao, nao explica offset de epoch por si so.

Aceite: fluxos permitidos funcionam no protocolo; negativas tem causa
corroborada; administracao preservada; DNS e tempo validados com fonte.
Reverter mudanca exige plano e gate humano quando remover/sobrescrever dados.

Fontes: [pfSense states](https://docs.netgate.com/pfsense/en/latest/monitoring/status/firewall-states.html),
[NTPv4](https://www.rfc-editor.org/info/rfc5905/),
[Windows Time](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings).
