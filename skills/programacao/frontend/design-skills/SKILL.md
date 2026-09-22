# 🎨 Design Skills — Design Systems e Tokens

Esta skill especifica os guias conceituais e os padrões operacionais para a criação e manutenção de consistência visual premium.

---

## 🎨 Framework de Cores e Tokens de Design

1. **Uso Avançado do Espaço de Cores HSL:**
   - HSL (*Hue, Saturation, Lightness*) é a ferramenta definitiva para gerar variações harmônicas e dinâmicas nas interfaces.
   - Defina as cores principais do sistema utilizando variáveis CSS na tag `:root`:
     ```css
     :root {
       --primary-h: 220;
       --primary-s: 90%;
       --primary-l: 56%;
       
       --primary: hsl(var(--primary-h), var(--primary-s), var(--primary-l));
       --primary-hover: hsl(var(--primary-h), var(--primary-s), calc(var(--primary-l) - 8%));
       --primary-light: hsl(var(--primary-h), var(--primary-s), 95%);
       
       --bg-main: hsl(0, 0%, 100%);
       --bg-card: hsl(220, 15%, 97%);
       --text-main: hsl(220, 20%, 15%);
     }
     ```
   - O uso de HSL torna as alterações de temas de interfaces extremamente fáceis de implementar e manter de forma global.

2. **Tipografia Premium:**
   - Mantenha uma escala tipográfica lógica e consistente nas interfaces (ex: proporções baseadas em *Golden Ratio* ou escalas modulares de `1.25rem`, `1.5rem`, `2rem`).
   - Use fontes de alto apelo visual (como **Outfit**, **Plus Jakarta Sans** ou **Inter**) importadas do Google Fonts para elevar a percepção de valor do produto.

3. **Espaçamento e Grid (Bento Grid):**
   - Adote escalas de espaçamento fixas e proporcionais baseadas em 8px (ex: `8px`, `16px`, `24px`, `32px`, `48px`).
   - Utilize a estrutura de **Bento Grids** (layouts assimétricos compostos por cards auto-suficientes com bordas arredondadas e sombras suaves) para interfaces limpas e organizadas.
