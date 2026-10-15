# Antlia: aprendizado, nao arquitetura modelo

Estudo de caso sanitizado de laboratorio virtualizado com firewall, AD,
File Server, banco, app, clientes Windows, observabilidade e NAS simulado.
Sem IPs, contas pessoais, credenciais, VMIDs reais ou logs brutos.

| Observacao historica | Regra reutilizavel |
|---|---|
| Relatorios declararam concluido antes de teste interno suficiente | Separar control plane, guest e funcao |
| Explorer passou a mostrar drives | Prova de experiencia visual daquele usuario; ACL continua exigindo testes |
| API retornou sucesso sem inventario visivel | Verificar ACL/escopo por endpoint |
| Coleta Epoch registrou offset de cerca de quatro horas | Nao reinterpretar como timezone; preservar metodo e incerteza |
| Survey posterior mostrou peers proximos e fonte free-running em hosts | Proximidade temporal nao comprova fonte confiavel |
| Restore de VM e boot tiveram sucesso | Nao extrapolar para aplicacao recuperada |
| Arquivo de dump copiado teve hash igual | Prova de copia, nao restore SQL |
| NAS virtual compartilhou host/pool | Integracao nao garante independencia de desastre |
| Testes negativos usaram excecao/timeout como deny | Classificar causa e usar controles positivos |

Esses fatos nao afirmam que as falhas persistem hoje. Relato posterior de
correcao precisa de evidencia correspondente para sustentar nova conclusao.
Uma captura de painel nao prova politicas, retention, alertas ou restore.

Nao reproduzir numero de VMs, VLANs, nomes de OUs, contas, software ou horarios
como arquitetura ideal. Extraia processo: descobrir, entender, executar com
gates, testar identidade/protocolo, documentar e reauditar.
