---
name: manim-video-creator
description: >
  Crie vídeos animados estilo 3Blue1Brown com Manim Community Edition. Explicações de conceitos,
  derivações matemáticas, visualizações de algoritmos, data stories e diagramas de arquitetura.
type: tool_orchestration
tags: [creative, content, visualization]
---

# Manim Video Creator

Crie vídeos explicativos animados estilo 3Blue1Brown usando Manim Community Edition.

**Core principle:** Isto é cinema educacional. Cada frame ensina. Cada animação revela estrutura.

## When to Use

- "Crie uma animação explicando [conceito]"
- "Vídeo estilo 3Blue1Brown sobre [tópico]"
- "Visualize este algoritmo"
- "Animação de derivação matemática"

**Auto-trigger:** Quando o usuário pede animação técnica/educacional.

## Prerequisites

### Dependencies

```bash
pip install manim    # Manim CE v0.20+
# LaTeX: brew install --cask mactex  (macOS)
# ffmpeg: brew install ffmpeg
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Conceito/tópico** | Yes | O que animar |
| **Modo** | No | concept/equation/algorithm/data/architecture |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Audiência** — Para quem estamos escrevendo/criando?
2. **Tom de Voz** — Qual a diretriz de marca a ser usada?
3. **Canal** — Onde isso será publicado?

## Phase 1: Planejar (plan.md)

Antes de qualquer código, definir: narrative arc, scene list, paleta de cores, timing.

**Geometria antes de álgebra.** Mostre a forma primeiro, equação depois.

## Phase 2: Código (script.py)

Uma classe por scene. Cada scene independentemente renderizável.

```python
from manim import *

BG = "#1C1C1C"
PRIMARY = "#58C4DD"
MONO = "Menlo"

class Scene1_Introduction(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("Title", font_size=48, color=PRIMARY, font=MONO)
        self.play(Write(title), run_time=1.5)
        self.wait(1.0)
```

### Paletas

| Palette | BG | Primary | Secondary | Accent |
|---|---|---|---|---|
| Classic 3B1B | `#1C1C1C` | `#58C4DD` | `#83C167` | `#FFFF00` |
| Warm | `#2D2B55` | `#FF6B6B` | `#FFD93D` | `#6BCB77` |
| Neon | `#0A0A0A` | `#00F5FF` | `#FF00FF` | `#39FF14` |

### Timing

| Contexto | run_time | wait() |
|---|---|---|
| Título | 1.5s | 1.0s |
| Equação-chave | 2.0s | 2.0s |
| "Aha moment" | 2.5s | 3.0s |

## Phase 3: Render

```bash
manim -ql script.py Scene1  # draft (480p)
manim -qh script.py Scene1  # production (1080p)
```

## Phase 4: Stitch

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Vídeo** | MP4 | `media/videos/` |
| **Stills** | PNG | Para preview |

## Cost

| Component | Cost |
|---|---|
| Manim | Free |
| Rendering | CPU local |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **LaTeX não instalado** | MathTex falha | Instalar texlive/mactex |
| **Kerning quebrado** | Fontes proporcionais | Usar fonte monospace |

## Composability

**Receives data from:**
- `arxiv-paper-scanner` — papers para explicar em vídeo

**Feeds into:**
- Content pipelines de marketing
- Documentação visual

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Patterns** | `[OPERACIONAL]: manim-video-creator — [insight]` | `Sempre usar font monospace` |

## Quality Gate

- [ ] **Subtitles em toda animação**
- [ ] **Paleta consistente entre scenes**
- [ ] **Breathing room (wait) após reveals**
- [ ] **Font size mínimo 18**

**If any check fails:** Ajustar script e re-render.
