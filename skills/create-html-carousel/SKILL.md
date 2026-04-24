---
name: create-html-carousel
description: >
  Generates production-ready HTML carousels for LinkedIn (1080x1080px per slide).
  Implements the user's visual design system — visual packages (Transparência Anatômica,
  Arquitetura da Tensão, Telemetria & Cockpit, Brutalista Tecnológico, Soft Minimal Anthropic)
  with intentional palette crossings. Output is a single self-contained HTML file with all slides.
description_pt-BR: >
  Gera carrosséis HTML prontos para LinkedIn (1080x1080px por slide).
  Implementa o the user's visual design system — pacotes visuais com cruzamentos
  intencionais de paleta. Output: único arquivo HTML auto-contido com todos os slides.
type: prompt
version: "1.0.0"
categories: [design, content, linkedin, carousel]
---

# Create HTML Carousel

## When to Use

Use this skill whenever an agent needs to generate a LinkedIn carousel as a self-contained
HTML file. This is the rendering engine for Flynn Design — it provides the HTML/CSS patterns,
font loading, and slide structure. The agent reads visual specifications (package + palette),
applies them to the roteiro textual, and writes the output to `output/carousel.html`.

---

## HTML Structure

Every carousel is a single HTML file. All slides are `div.slide` elements inside a
`div.carousel` wrapper. Each slide is exactly 1080×1080px.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1080">
  <title>Carousel — [Squad Name]</title>
  <style>
    /* ── Reset ──────────────────────────── */
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #111; }

    /* ── Font Loading ────────────────────── */
    @import url('https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,700,400&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');
    @import url('https://api.fontshare.com/v2/css?f[]=clash-display@700,600&display=swap');

    /* ── Carousel container ──────────────── */
    .carousel {
      width: 1080px;
      font-family: 'Cabinet Grotesk', sans-serif;
    }

    /* ── Base slide ──────────────────────── */
    .slide {
      width: 1080px;
      height: 1080px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* ── Metadata (always present) ───────── */
    .meta {
      font-family: 'Space Mono', monospace;
      font-size: 14px;
      letter-spacing: 0.08em;
      opacity: 0.5;
    }

    /* Package-specific CSS added below */
  </style>
</head>
<body>
  <div class="carousel">
    <!-- Slide 01 -->
    <div class="slide" id="slide-01">
      [slide content]
    </div>
    <!-- Slide 02 -->
    <div class="slide" id="slide-02">
      [slide content]
    </div>
    <!-- ... -->
  </div>
</body>
</html>
```

---

## Visual Package CSS Templates

Add the chosen package's CSS to the `<style>` block. One package per carousel.

### Transparência Anatômica

Blueprints, translucent layers, internal structure as aesthetic element.

```css
.slide.anatomica {
  background: var(--bg, #0A0A12);
  color: var(--fg, #E8E8F0);
}
.slide.anatomica::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,212,255,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,255,0.04) 1px, transparent 1px);
  background-size: 54px 54px;
  pointer-events: none;
}
.slide.anatomica .headline {
  font-family: 'Cabinet Grotesk', sans-serif;
  font-weight: 800;
  font-size: 72px;
  line-height: 1.05;
  letter-spacing: -0.02em;
}
.slide.anatomica .meta {
  color: var(--accent, #00D4FF);
}
```

### Arquitetura da Tensão

Asymmetric composition, elements anchored to edges, deliberate visual tension.

```css
.slide.tensao {
  background: var(--bg, #F5F0E8);
  color: var(--fg, #1A1A1A);
  padding: 64px;
}
.slide.tensao .headline {
  font-family: 'Cabinet Grotesk', sans-serif;
  font-weight: 800;
  font-size: 80px;
  line-height: 1.0;
  letter-spacing: -0.03em;
  max-width: 75%;
}
.slide.tensao .anchor-bottom {
  position: absolute;
  bottom: 64px;
  left: 64px;
  right: 64px;
}
.slide.tensao .rule {
  width: 120px;
  height: 4px;
  background: var(--accent, #FF3D00);
  margin-bottom: 32px;
}
```

### Telemetria & Cockpit

Data panel aesthetics, cockpit displays, clinical precision.

```css
.slide.cockpit {
  background: var(--bg, #060810);
  color: var(--fg, #C8D8E8);
  border: 1px solid rgba(0,212,255,0.15);
  padding: 60px;
}
.slide.cockpit .data-label {
  font-family: 'Space Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent, #00D4FF);
  margin-bottom: 8px;
}
.slide.cockpit .stat {
  font-family: 'Cabinet Grotesk', sans-serif;
  font-weight: 800;
  font-size: 120px;
  line-height: 1;
  color: var(--accent, #00D4FF);
}
.slide.cockpit .headline {
  font-weight: 700;
  font-size: 48px;
  line-height: 1.15;
}
.slide.cockpit .divider {
  width: 100%;
  height: 1px;
  background: rgba(0,212,255,0.2);
  margin: 32px 0;
}
```

### Brutalista Tecnológico

Dominant typography, extreme contrast, minimal elements.

```css
.slide.brutalista {
  background: var(--bg, #0F0F0F);
  color: var(--fg, #F0F0F0);
  padding: 72px;
  justify-content: flex-end;
}
.slide.brutalista .headline {
  font-family: 'Clash Display', 'Cabinet Grotesk', sans-serif;
  font-weight: 700;
  font-size: 88px;
  line-height: 0.95;
  letter-spacing: -0.04em;
  text-transform: uppercase;
}
.slide.brutalista .tag {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent, #FF3D00);
  margin-bottom: 24px;
}
```

### Soft Minimal Anthropic

Massive negative space, neutral palette, subtle warmth — reflection and philosophy.

```css
.slide.minimal {
  background: var(--bg, #FAFAF8);
  color: var(--fg, #2A2A2A);
  padding: 96px;
  justify-content: center;
  align-items: flex-start;
}
.slide.minimal .headline {
  font-family: 'Cabinet Grotesk', sans-serif;
  font-weight: 400;
  font-size: 52px;
  line-height: 1.3;
  letter-spacing: -0.01em;
  max-width: 80%;
}
.slide.minimal .meta {
  position: absolute;
  bottom: 96px;
  right: 96px;
  color: #AAAAAA;
}
```

---

## Color Palette Variables

Apply the chosen palette as CSS custom properties on `.carousel`. One palette per carousel.

```css
/* Cockpit Dark */
.carousel.palette-cockpit { --bg: #0A0A12; --fg: #E8E8F0; --accent: #00D4FF; }

/* Oceânica & Coral */
.carousel.palette-oceanica { --bg: #0D1B2A; --fg: #E8F4F0; --accent: #FF6B6B; }

/* Red Energy */
.carousel.palette-red { --bg: #0F0F0F; --fg: #F5F5F5; --accent: #FF3D00; }

/* Biocenose */
.carousel.palette-biocenose { --bg: #1A2318; --fg: #E8F0E4; --accent: #7EC8A0; }

/* Brutalista */
.carousel.palette-brutalista { --bg: #F5F0E8; --fg: #1A1A1A; --accent: #FF3D00; }

/* Neutral Warm */
.carousel.palette-neutral { --bg: #FAFAF8; --fg: #2A2A2A; --accent: #8A8A8A; }
```

---

## Slide Metadata Pattern (MANDATORY on all slides)

Every slide MUST have a metadata element with the slide number in Space Mono.
Position varies by package — always in a corner, always subtle.

```html
<!-- Standard metadata element -->
<span class="meta">0N / TT</span>
<!-- Where N = slide number, TT = total slides -->
<!-- Example: "03 / 08" -->
```

Position by package:
- Transparência Anatômica → top-right, `position: absolute; top: 48px; right: 48px;`
- Arquitetura da Tensão → bottom-right, `position: absolute; bottom: 64px; right: 64px;`
- Telemetria & Cockpit → top-right inside divider, part of the data layout
- Brutalista → top-left, `position: absolute; top: 72px; left: 72px;`
- Soft Minimal → bottom-right, `position: absolute; bottom: 96px; right: 96px;`

---

## Typography Rules

| Purpose | Font | Weight | Size range |
|---|---|---|---|
| Main headline | Cabinet Grotesk | 800 | 52–88px |
| Subheadline / body | Cabinet Grotesk | 400–700 | 24–40px |
| Stats / large numbers | Cabinet Grotesk | 800 | 80–140px |
| Metadata / labels | Space Mono | 400–700 | 11–16px |
| Optional serif accent | Lora or Playfair Display | 400 | 32–48px |

**Prohibited fonts:** Inter, Roboto, Arial, Helvetica, Open Sans, Lato, Montserrat.

---

## Slide Length Rule

**Maximum 40 words per slide.** Count words before rendering. If over the limit:
1. Split into two slides
2. Or cut — concision is a design decision, not a loss

---

## Output Instructions

1. Generate the complete HTML file content
2. Write to `squads/{code}/output/carousel.html` using the Write tool
3. Report: number of slides, visual package applied, palette used, and the cruzamento rationale

Flynn Design announces:
```
Flynn Design — output:
— Arquivo: output/carousel.html
— Slides: N slides (1080×1080px)
— Pacote: [name]
— Paleta: [name] ([--accent hex])
— Cruzamento: [1-line rationale]
```

---

## Font Fallback

If CDN fonts fail to load (offline environment), use these fallbacks:
- Cabinet Grotesk → `system-ui, -apple-system, 'Segoe UI', sans-serif`
- Space Mono → `'Courier New', Courier, monospace`
- Clash Display → `Impact, 'Arial Narrow', sans-serif`

Always include fallbacks in the font-family declaration.
