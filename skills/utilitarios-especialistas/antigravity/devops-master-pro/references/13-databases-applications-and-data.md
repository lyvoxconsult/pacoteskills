# Bancos, aplicacoes e dados

Use para listener, grants, storage, dependencia APP/DB e restauracao SQL.
Entradas: produto/versao, papel, dados, acesso, principals e criterio funcional.

## Banco

1. Verifique filesystem/mounts/espaco, disco SO/DATA/WAL conforme requisito,
   service/instance, versao e configuracao efetiva. Discos virtuais separados
   no mesmo pool nao sao falhas fisicas independentes.
2. Para PostgreSQL, examine databases/roles/grants, listen_addresses,
   postgresql.conf/pg_hba carregados, logs e TLS quando exigido. Verificar
   regra no arquivo nao prova que o processo a carregou.
3. Use consulta autenticada local e do APP, com identidade correta. Cliente
   proibido deve falhar por causa corroborada, nao servidor desligado.
4. Valide log do teste, backup, retencao e restauracao no nivel contratado.
   Meta-servico postgresql active nao prova instancia aceita SQL.

## Aplicacao

Confirme processo, unidade/entrypoint persistente, pacotes/config, listeners,
DNS/NTP, autenticacao/autorizacao, DB e logs. Script que faz SELECT nao
necessariamente implementa a aplicacao/middleware requerido.
E2E deve passar pelo caminho que o usuario usa: cliente -> app -> DB ->
resultado e persistencia. Evite transacao destrutiva em dados de negocio.
Inserir probes e depois remove-los requer escopo humano aprovado de cleanup.

## Backup/restore de dados

Escolha logico, fisico, WAL/PITR conforme workload. Dump copiado e hash igual
validam arquivo, nao restauracao. Em ambiente isolado autorizado, restaure
objetos/dados, roles/tablespaces/extensoes necessarios e execute queries e
transacao de aplicacao. Restauracao que sobrescreve dados exige gate humano.
PITR exige cadeia/WAL e timeline adequados, nao apenas pasta chamada WAL.

## Limites e aceite

Resultado funcional, grants/negativas, persistencia e log precisam de prova.
Tuning usa medicao e baseline, nao aumento indiscriminado de conexoes/memoria.
Logs SQL podem expor dados e credenciais: minimizar e proteger.
Nao marcar TLS PASS por porta ou parametro sem validar conexao/certificado.
Rollback de schema/dados precisa de estrategia especifica; apagar/recriar
banco para corrigir declaracao nao e permitido sem aprovacao humana.

Fontes: [PostgreSQL authentication](https://www.postgresql.org/docs/current/client-authentication.html),
[backup](https://www.postgresql.org/docs/current/backup.html),
[pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html).
