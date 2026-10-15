# Arquitetura e descoberta

Use para brownfield, desenho, migracao ou comparacao entre documentado e real.

## Entradas e fronteiras

Identifique ambiente, owner, workloads, usuarios, dados, dependencias,
restricoes de acesso, orcamento, janela e objetivos de disponibilidade,
latencia, capacidade, RPO/RTO e compliance. Se nao definidos, declare
hipoteses; consulte humano quando mudarem arquitetura ou risco relevante.
Autoridade de leitura nao autoriza provisionamento ou migracao.

## Procedimento

1. Leia inventario, IaC, playbooks, diagramas, contratos e incidentes relevantes.
   Liste fontes consultadas, datas e lacunas; nao diga leitura integral quando
   houve apenas inventario de arquivos.
2. Colete inventario de controle e de funcao: host, VM, SO, servico, rede,
   identidade, dados, telemetria e recuperacao. Vincule identificadores estaveis.
3. Desenhe fluxos reais com origem, destino, protocolo, identidade e dependencia.
   Separe plano de gestao, trafego de usuario, dados e destino de backup.
4. Mapeie dominios de falha: mesmo disco, host, rack, site, conta cloud, provedor,
   credencial administrativa, DNS/identidade e supply chain compartilhados.
5. Compare alternativas com capacidade medida, custo total, operabilidade,
   resiliencia e prazo. Nao adicionar Kubernetes, multi-cloud, HA ou cluster
   de tres nos sem necessidade e justificativa.
6. Registre decisao e matriz requisito/real/status/acao/dependencia/risco/teste.
   Ordene execucao pela dependencia real; DNS/NTP podem depender de identidade,
   e recuperar identidade pode exigir acesso local independente.

## Interpretacao e aceite

Um diagrama coerente prova entendimento, nao conectividade. Dimensionamento
usa picos e crescimento, nao apenas tamanho nominal de disco/RAM.
Aceite arquitetural exige requisitos rastreaveis e tradeoffs reconhecidos;
aceite operacional exige testes internos e de ponta a ponta por funcao.

## Limites e recuperacao

Planeje migracao por etapas com rollback viavel, coexistencia e gatilhos de
interrupcao. Nao formatar para alinhar codigo a uma arquitetura idealizada.
Exclusoes e substituicoes exigem aprovacao humana conforme referencia 16.
Documente incerteza, dependencia externa e risco aceito sem converter em PASS.

Fontes adicionais: cloud-architect, hybrid-cloud-architect e network-engineer
do catalogo local, resolvidos conforme [roteamento](skill-routing.md).
