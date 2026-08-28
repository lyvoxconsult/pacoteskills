# Foundations

## Categorias

- `Baseline recomendado`: deve existir na maioria das máquinas de desenvolvimento.
- `Complementar importante`: agrega produtividade ou cobertura técnica, mas pode ser opcional.
- `Observado na máquina auditada`: ferramenta detectada no host usado durante a auditoria.

## Princípios

1. Documentar o que é útil para desenvolvimento real, não qualquer binário presente.
2. Evitar acoplamento com sistema operacional específico.
3. Registrar estado observado sem promovê-lo automaticamente a padrão global.
4. Preferir ferramentas com instalação simples, comunidade madura e baixo risco operacional.
5. Tratar o repositório como catálogo e referência de setup, não como depósito de executáveis.

## Critério de inclusão

Uma ferramenta ou framework entra neste catálogo quando atende pelo menos um destes pontos:

- é pré-requisito frequente para skills, MCPs ou automações;
- reduz atrito de setup em novas máquinas;
- sustenta desenvolvimento, teste, build, containerização ou depuração;
- aparece de forma recorrente nos fluxos de trabalho do agente.

## Estado observado

Os arquivos deste diretório podem citar o estado de uma máquina auditada. Esse dado serve como evidência local, não como verdade global permanente.
