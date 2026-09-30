# 🎬 animated-web skill

> Skill para agentes de IA que transforma vídeos MP4 em landing pages cinematográficas com scroll-driven animations em canvas 2D.

Essa skill foi criada durante o desenvolvimento deste projeto e está disponível aqui para quem quiser usar no próprio agente de IA.

---

## O que ela faz

Quando ativada, a skill guia o agente pelo processo completo de criar uma landing page animada:

- 🎥 Gera o script Python para extrair frames do MP4 em `.webp` otimizados
- ⚙️ Monta a estrutura do projeto Next.js com pastas e dependências
- 🪝 Cria os hooks `useScrollFrame` e `useInView`
- 🖼️ Implementa o componente `FrameSequence` (canvas 2D com cover-fit e pré-carregamento em batches)
- 🎨 Configura os design tokens no `globals.css` (grain, photo-fade, scrollbar)
- 📖 Entrega NavBar, overlays de texto animados e seções com entrada suave
- ✅ Valida tudo com um checklist de qualidade antes da entrega

---

## Como instalar no seu agente

### Claude Code / Antigravity

```bash
# Windows
git clone https://github.com/gfrabelo/airpods-pro "%USERPROFILE%\.claude\skills\animated-web" --no-local

# Ou copie manualmente o SKILL.md para:
# C:\Users\SEU_USUARIO\.claude\skills\animated-web\SKILL.md
```

```bash
# macOS / Linux
mkdir -p ~/.claude/skills/animated-web
curl -o ~/.claude/skills/animated-web/SKILL.md \
  https://raw.githubusercontent.com/gfrabelo/airpods-pro/main/skills/animated-web/SKILL.md
```

### Outros agentes (Cursor, Windsurf, Copilot...)

Copie o conteúdo do `SKILL.md` para a pasta de regras/prompts do seu editor.

---

## Como usar

Depois de instalada, descreva o que quer criar:

```
Quero um site com animação de scroll igual ao do Apple AirPods Pro.
Tenho um vídeo MP4 disponível.
```

```
Cria uma landing page cinematográfica para minha marca.
Tema: academia de MMA. Paleta: preto + vermelho. Fonte: urbana.
```

O agente vai conduzir todo o processo — da extração dos frames até o site rodando.

---

## Combinação recomendada

Esta skill foi usada em conjunto com a **UI UX Pro Max** para gerar o design system do projeto:

> 🔗 [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

---

## Arquivo principal

→ [`SKILL.md`](./SKILL.md) — instruções completas para o agente de IA
