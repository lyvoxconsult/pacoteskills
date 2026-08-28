# Infra And Containers

## Baseline recomendado

| Ferramenta | Papel | Prioridade | Observado na maquina auditada |
| --- | --- | --- | --- |
| Docker | containers, ambientes reproduziveis e servicos auxiliares | alta | sim |

## Complementares importantes

| Ferramenta | Papel | Prioridade | Observado na maquina auditada |
| --- | --- | --- | --- |
| Docker Compose | orquestracao local de multiplos servicos | alta | nao auditado separadamente |
| dev containers | padronizacao de ambiente por projeto | media | nao auditado aqui |
| virtualizacao leve | isolamento adicional quando necessario | media | nao auditado aqui |

## Estado observado

- Docker: `29.6.1`

## Notas

- Docker entra como item de alta relevancia porque reduz diferencas entre hosts e facilita subir bancos, filas, proxies e stacks auxiliares.
- Esta documentacao nao fixa uma distribuicao ou interface grafica especifica. O foco e a capacidade funcional de executar containers.
