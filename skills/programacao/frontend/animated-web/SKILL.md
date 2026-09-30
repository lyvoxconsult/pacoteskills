---
name: animated-web
description: Cria websites completos e responsivos com scroll-driven animations baseadas em canvas 2D. Use quando quiser transformar um vídeo MP4 em frames WebP e construir uma landing page animada, viva e cinematográfica do zero. Input esperado: descrição do site (tema, seções, cores, propósito, vídeo disponível ou não). Output gerado: script Python para extrair frames, todos os componentes Next.js (FrameSequence, hooks, seções), globals.css com design tokens, e instruções step-by-step para rodar localmente. Também use para: "quero um site igual ao do skate", "site com animação de scroll", "landing page com canvas animation", "transformar vídeo em animação web".
user-invocable: true
---

## Identidade

Você é um engenheiro front-end especialista em web cinematográfica. Você domina o processo completo de criar sites com scroll-driven animations usando `<canvas>` 2D — desde a extração de frames de um vídeo MP4 até o deploy de uma landing page Next.js responsiva, performática e visualmente impactante.

---

## Processo Completo (Step-by-Step)

### STEP 0 — Coletar Contexto

Se o input estiver vazio ou vago, faça ESTAS perguntas antes de gerar qualquer código:

1. Qual é o tema/propósito do site? (marca, portfólio, produto, evento...)
2. Você tem um vídeo MP4 disponível? Se sim, onde está?
3. Qual paleta de cores? (ex: preto + amarelo, branco + azul, etc.)
4. Quais seções quer no site? (ex: hero, sobre, serviços, depoimentos, contato)
5. Qual identidade tipográfica? (clean, rude, editorial, tech...)

Se tiver informação suficiente, pule direto para o STEP 1.

---

### STEP 1 — Script Python: Extrair Frames do MP4

Gere o arquivo `extract_frames.py` na raiz do projeto:

```python
import os
import sys
import subprocess

VIDEO_PATH = "video.mp4"          # AJUSTAR
OUTPUT_DIR = "public/frames/loop"
TARGET_FPS = 30
WEBP_QUALITY = 80

def check_and_install_opencv():
    try:
        import cv2
        return cv2
    except ImportError:
        print("OpenCV não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
        import cv2
        return cv2

def extract_frames():
    cv2 = check_and_install_opencv()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"Erro: não foi possível abrir '{VIDEO_PATH}'")
        return

    source_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / source_fps if source_fps > 0 else 0
    frame_interval = source_fps / TARGET_FPS

    print(f"Vídeo: {VIDEO_PATH}")
    print(f"FPS original: {source_fps:.2f} | Total frames: {total_frames} | Duração: {duration:.2f}s")
    print(f"Extraindo a {TARGET_FPS} FPS -> destino: {OUTPUT_DIR}")

    frame_index = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_index % frame_interval < 1:
            filename = os.path.join(OUTPUT_DIR, f"frame_{saved_count + 1:04d}.webp")
            cv2.imwrite(filename, frame, [cv2.IMWRITE_WEBP_QUALITY, WEBP_QUALITY])
            saved_count += 1
        frame_index += 1

    cap.release()
    print(f"Concluído! {saved_count} frames salvos em '{OUTPUT_DIR}'.")

if __name__ == "__main__":
    extract_frames()
```

**Instrução para o usuário:**
```bash
# 1. Coloque o vídeo na raiz como video.mp4 (ou ajuste VIDEO_PATH)
# 2. Execute:
python extract_frames.py
# Frames gerados em: public/frames/loop/frame_0001.webp ...
```

---

### STEP 2 — Setup Next.js

```bash
npx create-next-app@latest nome-do-projeto --typescript --tailwind --app --no-src-dir
cd nome-do-projeto
mkdir -p public/frames/loop
mkdir -p src/hooks src/components/ui src/components/sections
```

**`package.json`** — verificar que tem:
```json
{
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  },
  "devDependencies": {
    "typescript": "latest",
    "@types/react": "latest",
    "@types/node": "latest",
    "tailwindcss": "latest",
    "@tailwindcss/postcss": "latest",
    "autoprefixer": "latest"
  }
}
```

---

### STEP 3 — Hook: `useScrollFrame.ts`

`src/hooks/useScrollFrame.ts`:

```typescript
import { RefObject, useEffect, useState } from 'react';

export function useScrollFrame(containerRef: RefObject<HTMLElement | null>, totalFrames: number) {
  const [currentFrame, setCurrentFrame] = useState(0);

  useEffect(() => {
    const onScroll = () => {
      const el = containerRef.current;
      if (!el) return;
      const rect = el.getBoundingClientRect();
      const scrollable = el.offsetHeight - window.innerHeight;
      const scrolled = Math.max(0, -rect.top);
      const progress = Math.min(scrolled / scrollable, 1);
      setCurrentFrame(Math.floor(progress * (totalFrames - 1)));
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener('scroll', onScroll);
  }, [containerRef, totalFrames]);

  return currentFrame;
}
```

---

### STEP 4 — Hook: `useInView.ts`

`src/hooks/useInView.ts`:

```typescript
import { RefObject, useEffect, useState } from 'react';

export function useInView(ref: RefObject<HTMLElement | null>, threshold = 0.15) {
  const [inView, setInView] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) setInView(true); },
      { threshold }
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [ref, threshold]);

  return inView;
}
```

---

### STEP 5 — Componente: `FrameSequence.tsx`

`src/components/ui/FrameSequence.tsx`:

```typescript
'use client';
import { useEffect, useRef } from 'react';
import { useScrollFrame } from '@/hooks/useScrollFrame';

interface FrameSequenceProps {
  framesPath: string;
  framePrefix?: string;
  zeroPad?: number;
  ext?: string;
  totalFrames: number;
  height?: string;
  children?: React.ReactNode;
  id?: string;
}

export default function FrameSequence({
  framesPath,
  framePrefix = 'frame_',
  zeroPad = 4,
  ext = 'webp',
  totalFrames,
  height = '300vh',
  children,
  id,
}: FrameSequenceProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const imagesRef = useRef<HTMLImageElement[]>([]);
  const isReadyRef = useRef(false);

  const currentFrame = useScrollFrame(containerRef, totalFrames);

  // Gera URL do frame com zero-padding
  const getFrameUrl = (index: number) => {
    const padded = String(index + 1).padStart(zeroPad, '0');
    return `${framesPath}/${framePrefix}${padded}.${ext}`;
  };

  // Pré-carrega frames
  useEffect(() => {
    const images: HTMLImageElement[] = Array(totalFrames).fill(null).map(() => new Image());
    imagesRef.current = images;

    const BATCH1_END = Math.min(30, totalFrames);

    // Batch 1: frames críticos (LCP)
    let loaded = 0;
    for (let i = 0; i < BATCH1_END; i++) {
      images[i].onload = () => {
        loaded++;
        if (loaded === 1) {
          syncCanvasSize();
          drawFrame(0);
        }
        if (loaded === BATCH1_END) {
          isReadyRef.current = true;
          drawFrame(currentFrame);
        }
      };
      images[i].src = getFrameUrl(i);
    }

    // Batch 2: resto dos frames (idle)
    const loadRest = () => {
      for (let i = BATCH1_END; i < totalFrames; i++) {
        images[i].src = getFrameUrl(i);
      }
    };

    if ('requestIdleCallback' in window) {
      requestIdleCallback(loadRest);
    } else {
      setTimeout(loadRest, 100);
    }
  }, [totalFrames, framesPath]);

  // Sincroniza tamanho do canvas com o container real
  const syncCanvasSize = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;
  };

  // Desenha frame com cover-fit
  const drawFrame = (frameIndex: number) => {
    const canvas = canvasRef.current;
    const img = imagesRef.current[frameIndex];
    if (!canvas || !img || !img.complete || img.naturalWidth === 0) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const imgRatio = img.naturalWidth / img.naturalHeight;
    const canvasRatio = canvas.width / canvas.height;
    let drawW = 0, drawH = 0, offsetX = 0, offsetY = 0;

    if (imgRatio > canvasRatio) {
      drawH = canvas.height;
      drawW = canvas.height * imgRatio;
      offsetX = (canvas.width - drawW) / 2;
    } else {
      drawW = canvas.width;
      drawH = canvas.width / imgRatio;
      offsetY = (canvas.height - drawH) / 2;
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, offsetX, offsetY, drawW, drawH);
  };

  // Reage ao frame atual
  useEffect(() => {
    if (!isReadyRef.current) return;
    requestAnimationFrame(() => drawFrame(currentFrame));
  }, [currentFrame]);

  // Resize handler
  useEffect(() => {
    const onResize = () => {
      syncCanvasSize();
      drawFrame(currentFrame);
    };
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, [currentFrame]);

  return (
    <section ref={containerRef} id={id} style={{ height }} className="relative w-full">
      <div className="sticky top-0 h-screen w-full overflow-hidden">
        <canvas ref={canvasRef} className="absolute inset-0 w-full h-full" />
        {/* Vignette */}
        <div className="absolute inset-0 pointer-events-none"
          style={{ background: 'linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, transparent 30%, transparent 70%, rgba(0,0,0,0.6) 100%)' }}
        />
        {children}
      </div>
    </section>
  );
}
```

---

### STEP 6 — Design Tokens: `globals.css`

Adapte as cores ao tema do projeto. Exemplo base:

```css
@import "tailwindcss";

:root {
  /* Ajuste para o tema do projeto */
  --color-black:    #0A0A0A;
  --color-primary:  #F5E642;   /* cor de destaque */
  --color-white:    #F0EDE6;
  --color-surface:  #2A2A2A;
  --color-accent1:  #C0440A;
  --color-accent2:  #7BBFDC;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { background: var(--color-black); color: var(--color-white); }

/* Grain texture */
.grain::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity: 0.035;
  z-index: 9999;
  pointer-events: none;
}

/* Photo fade nas bordas */
.photo-fade { position: relative; }
.photo-fade::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    linear-gradient(to bottom, var(--color-black) 0%, transparent 18%, transparent 82%, var(--color-black) 100%),
    linear-gradient(to right, var(--color-black) 0%, transparent 18%, transparent 82%, var(--color-black) 100%);
  pointer-events: none;
}

/* Scroll hint bounce */
@keyframes scrollBounce {
  0%, 100% { transform: translateY(0); opacity: 0.5; }
  50%       { transform: translateY(6px); opacity: 1; }
}
.scroll-bounce { animation: scrollBounce 1.6s ease-in-out infinite; }

/* Scrollbar */
::-webkit-scrollbar { width: 2px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(245,230,66,0.2); border-radius: 1px; }
```

---

### STEP 7 — Overlays de Texto no Hero

Padrão de fade in/out por progresso de scroll (0–100):

```typescript
function getOpacity(progress: number, start: number, end: number, fade = 5): number {
  if (progress < start - fade || progress > end + fade) return 0;
  if (progress >= start && progress <= end) return 1;
  if (progress < start) return (progress - (start - fade)) / fade;
  return 1 - (progress - end) / fade;
}

// Uso:
const progressPct = (currentFrame / (totalFrames - 1)) * 100;
const opacity1 = getOpacity(progressPct, 10, 40);  // aparece de 10% a 40%
const opacity2 = getOpacity(progressPct, 50, 85);  // aparece de 50% a 85%
```

---

### STEP 8 — NavBar Responsiva

Pattern pronto (adapte cores e links):

```typescript
'use client';
import { useEffect, useState } from 'react';

export default function NavBar() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const links = ['#sobre', '#servicos', '#galeria', '#contato'];

  return (
    <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
      scrolled ? 'bg-black/90 backdrop-blur-md border-b border-white/10' : 'bg-transparent'
    }`}>
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <a href="#" className="font-mono text-sm tracking-widest text-[--color-primary]">
          LOGO
        </a>
        {/* Desktop */}
        <div className="hidden md:flex gap-8">
          {links.map(l => (
            <a key={l} href={l} className="text-sm tracking-wider text-white/70 hover:text-white transition-colors">
              {l.replace('#', '').toUpperCase()}
            </a>
          ))}
        </div>
        {/* Mobile toggle */}
        <button className="md:hidden flex flex-col gap-1.5 w-6" onClick={() => setMenuOpen(!menuOpen)}>
          <span className={`block h-px bg-white transition-all ${menuOpen ? 'rotate-45 translate-y-2' : ''}`} />
          <span className={`block h-px bg-white transition-all ${menuOpen ? 'opacity-0' : ''}`} />
          <span className={`block h-px bg-white transition-all ${menuOpen ? '-rotate-45 -translate-y-2' : ''}`} />
        </button>
      </div>
      {/* Mobile menu */}
      {menuOpen && (
        <div className="md:hidden bg-black/95 px-6 py-4 flex flex-col gap-4">
          {links.map(l => (
            <a key={l} href={l} onClick={() => setMenuOpen(false)}
              className="text-sm tracking-wider text-white/70 hover:text-white">
              {l.replace('#', '').toUpperCase()}
            </a>
          ))}
        </div>
      )}
    </nav>
  );
}
```

---

### STEP 9 — Seções Adicionais (Pattern Base)

Qualquer seção com animação de entrada usa `useInView`:

```typescript
'use client';
import { useRef } from 'react';
import { useInView } from '@/hooks/useInView';

export default function NomeDaSection() {
  const ref = useRef<HTMLElement>(null);
  const inView = useInView(ref);

  return (
    <section ref={ref} id="nome" className="py-32 px-6 max-w-5xl mx-auto">
      <div className={`transition-all duration-700 ${inView ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'}`}>
        {/* Conteúdo da seção */}
      </div>
    </section>
  );
}
```

---

### STEP 10 — Orquestração na `page.tsx`

```typescript
import NavBar from '@/components/ui/NavBar';
import FrameSequence from '@/components/ui/FrameSequence';
import HeroOverlays from '@/components/sections/HeroOverlays';
// ... outras seções

export default function Home() {
  return (
    <main className="grain bg-[--color-black]">
      <NavBar />
      <FrameSequence
        framesPath="/frames/loop"
        totalFrames={63}      // Ajustar conforme extract_frames
        height="300vh"
        id="hero"
      >
        <HeroOverlays />
      </FrameSequence>
      {/* Demais seções */}
    </main>
  );
}
```

---

## Checklist de Qualidade

Antes de entregar o código ao usuário, verifique:

- [ ] `extract_frames.py` tem `VIDEO_PATH` e `OUTPUT_DIR` corretos
- [ ] `totalFrames` em `FrameSequence` bate com o número real de frames gerados
- [ ] `height` do FrameSequence é proporcional ao número de frames (regra: `totalFrames * 5`vh como ponto de partida)
- [ ] Paleta de cores aplicada nos CSS custom properties
- [ ] NavBar tem links corretos apontando para os IDs das seções
- [ ] Cada seção tem um `id` correspondente
- [ ] Fontes importadas no `layout.tsx`

---

## Fontes Recomendadas por Estilo

| Estilo | Display | Body | Label |
|--------|---------|------|-------|
| Raw/Urbano | Bebas Neue, Anton | Space Grotesk | Space Mono |
| Luxury | Playfair Display | Cormorant | DM Mono |
| Tech/Startup | Inter, Geist | Inter | JetBrains Mono |
| Editorial | DM Serif Display | Source Serif 4 | IBM Plex Mono |

---

## Edge Cases

- **Sem vídeo MP4:** Ofereça usar uma sequência de imagens estáticas como frames, ou crie uma animação CSS pura como fallback
- **Muitos frames (>120):** Reduza `WEBP_QUALITY` para 70 e limite `TARGET_FPS` a 20
- **Vídeo muito longo (>10s):** Oriente a recortar apenas o trecho relevante com ffmpeg antes de extrair
- **Site sem tema definido:** Peça uma referência visual ou 3 palavras que descrevem o feeling desejado
- **Sem Next.js:** O `FrameSequence` funciona em HTML puro com JS vanilla — oferecer versão alternativa se solicitado
