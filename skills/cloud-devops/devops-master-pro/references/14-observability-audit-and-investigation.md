# Observabilidade, auditoria e investigacao

Use para logs/metrics/traces, SIEM, SLOs e cobertura investigavel. Entradas:
fontes, eventos requeridos, principals, retencao, volume, privacidade e consultas.

## Cobertura mensuravel

Mapeie autenticacao, administracao, processos conforme politica, mudancas
de grupo/GPO/ACL, SMB/SACL, banco, app, firewall e backup por fonte. Diga
quais operacoes nao sao cobertas. Nao prometer logar literalmente tudo que
acontece numa VM sem limites tecnicos, custo e privacidade.

1. Inspecione fonte/agente/coletor, buffers/filas, drops, parser, armazenamento,
   indices ou arquivos, ACL, tempo, retencao e espaco.
2. Gere evento benigno com marcador unico e identidade definida, sem senha.
   A geracao nao deve criar/remover objetos sem permissao/gate correspondente.
3. Procure no destino, valide origem, principal, timestamp, campos e latencia.
   Conteudo copiado manualmente nao comprova caminho automatico de coleta.
4. Teste consulta de investigacao e alerta aplicavel ate destinatario autorizado.
   Servico SIEM ativo ou syslog presente nao prova deteccao/correlacao.
5. Verifique confianca temporal, controle de acesso e protecao contra alteracao.
   Hash sidecar nao prova emissor ou nao repudio. Imutabilidade precisa de
   mecanismo/retencao verificados, nao atributo descritivo.

## Investigacao

Registre janela UTC e timezone exibido, identidade/origem, recurso, operacao,
resultado e correlacao. Valide lacunas e atrasos antes de concluir que ausencia
de evento significa ausencia de acao. Consultas devem ser reproduziveis,
filtradas e limitadas para evitar exportacao de dados desnecessarios.

Preserve raw evidence em local protegido fora do Git; resumo sanitizado referencia
artefato. Coleta forense deve preservar origem, hashes, custodia e alteracoes da
propria coleta, sem afirmar certificacao juridica a partir desta skill.

## SLO e capacidade

Escolha SLIs de usuario (sucesso/latencia) e objetivo/janela; infraestrutura
CPU baixa nao prova confiabilidade. Alertas devem ter owner, severidade,
runbook e teste de entrega. Evite cardinalidade explosiva e dados pessoais
em labels/traces. Retencao ou TTL com exclusao requer aprovacao humana especifica.

Aceite: marcador recebido e consultavel, alerta entregue quando previsto,
cobertura e lacunas documentadas, storage/tempo/ACL verificados. Nao instalar
stack adicional quando uma solucao existente cumpre requisito.

Fontes: [OpenTelemetry](https://opentelemetry.io/docs/),
[Prometheus practices](https://prometheus.io/docs/practices/),
[Windows audit policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings).
