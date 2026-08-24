---
title: "Ferramentas Globais Condicionais"
status: active
updated_at: 2026-08-14
---

# Ferramentas Globais Condicionais

Estas ferramentas fazem parte do workspace de todos os projetos novos. Elas são obrigatórias quando o gatilho se aplica e dispensadas para perguntas rápidas, edição de imagem e tarefas claramente irrelevantes.

| Ferramenta | Uso padrão | Instalação/forma de uso |
|---|---|---|
| Graphify | Grafo local para arquitetura, pesquisa de base e alterações multi-arquivo | `graphify`; skill global instalada. |
| Headroom | Compressão reversível de contexto para RAG, logs e saídas extensas | `headroom`; validar com `headroom doctor` antes de proxy/MCP. |
| Outlines | Saída estruturada de LLM orientada por schema dentro da aplicação | Adicionar `outlines` apenas ao ambiente do projeto que gera respostas estruturadas. |
| Codeburn | Auditoria local de tokens, custo, orçamento e desperdício | `codeburn status`, `overview`, `report`, `optimize` e `doctor` por padrão somente leitura. |

## Segurança

- Não ativar proxy, wrapper, hook, sincronização, compartilhamento ou alteração persistente automaticamente.
- Não adicionar Outlines a projetos sem geração de LLM estruturada.
- Não enviar documentos, PDFs, imagens, vídeos ou segredos a backend externo pelo Graphify sem configuração e autorização adequadas.
