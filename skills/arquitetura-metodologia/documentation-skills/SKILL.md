# 📝 Documentation Skills — Escrita Técnica e Segundo Cérebro

Esta skill fornece as metodologias recomendadas para manter a documentação de arquitetura de sistemas e o Segundo Cérebro do Obsidian extremamente organizados e úteis.

---

## ⚖️ Filosofia da Documentação Enxuta (Lean Documentation)

1. **Evite Poluição:**
   - As notas e documentos técnicos devem focar no **Porquê** (decisões, arquitetura, dependências e escopo estratégico) e não no **Como** (detalhes exaustivos de linhas de código que mudam frequentemente).
   - Não cole blocos extensos de código-fonte nas notas do Obsidian. A IA pode analisar o código-fonte do repositório Git diretamente.

2. **Registro de Decisões Técnicas (Architecture Decision Records):**
   - Utilize a estrutura de ADRs (Architecture Decision Records) contida em `Decisões Técnicas.md` de cada projeto para registrar de forma rápida e clara todas as refatorações relevantes.
   - Um histórico de decisões limpo reduz o tempo de onboarding de novos desenvolvedores e contextualiza IAs rapidamente em manutenções futuras.

---

## 🤖 Simbiose de Agentes com o Obsidian

- **Consulta Preventiva:** Sempre ordene aos agentes de desenvolvimento ler a visão geral do projeto no Obsidian antes de iniciar modificações no código-fonte.
- **Log Pós-Tarefa:** Ao final de sprints com entregas bem-sucedidas, delegue a escrita das alterações na nota do Obsidian correspondente de forma automatizada pelo agente.
- **Segurança Absoluta:** O cofre local do Obsidian reside de forma isolada e não é exposto a repositórios públicos. No entanto, siga a boa prática de evitar versionar credenciais confidenciais de banco ou chaves reais de produção nas notas de visão geral de projeto.
