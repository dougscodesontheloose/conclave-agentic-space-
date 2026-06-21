#!/usr/bin/env python3
"""
Carousel Renderer v4 — "Poética Racional" Edition
Design premium focado na identidade do <user_name> Moura:
- Contraste entre Engenharia (Mono) e Poesia (Serif).
- Efeito Glassmorphism e texturas de ruído.
- Layouts assimétricos e tipografia refinada.
"""

import re
import os
import sys
from pathlib import Path

OUTPUT_DIR = Path("squads/linkedin-content/output/carousel")

COLORS = {
    "bg":          "#0a0b1e",  # Night Blue
    "accent":      "#00e5ff",  # Cyan (Engineering)
    "poetic":      "#f0abfc",  # Soft Magenta (Poetry)
    "text_main":   "#f8fafc",
    "text_dim":    "#94a3b8",
    "glass_bg":    "rgba(255, 255, 255, 0.03)",
    "glass_border":"rgba(255, 255, 255, 0.1)",
}

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500&family=Lora:ital,wght@0,600;1,500&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
    --bg: {COLORS['bg']};
    --accent: {COLORS['accent']};
    --poetic: {COLORS['poetic']};
    --text: {COLORS['text_main']};
    --text-dim: {COLORS['text_dim']};
    --glass: {COLORS['glass_bg']};
    --border: {COLORS['glass_border']};
}}

body {{
    background: #000;
    font-family: 'Inter', sans-serif;
    color: var(--text);
    display: flex;
    flex-wrap: wrap;
    gap: 60px;
    padding: 60px;
    justify-content: center;
}}

.slide {{
    width: 1080px;
    height: 1080px;
    padding: 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    background: var(--bg);
    overflow: hidden;
    /* Scale for preview */
    transform: scale(0.6);
    transform-origin: top left;
    margin-bottom: -432px;
    margin-right: -432px;
    box-shadow: 0 40px 100px rgba(0,0,0,0.5);
    border: 1px solid var(--border);
}}

/* -- Background Textures -- */
.slide::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: 
        radial-gradient(circle at 10% 10%, rgba(0, 229, 255, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(240, 171, 252, 0.08) 0%, transparent 40%);
    z-index: 1;
}}

.slide::after {{
    content: "";
    position: absolute;
    inset: 0;
    opacity: 0.03;
    pointer-events: none;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3col%3e%3cg%3e%3cfilter id='noiseFilter'%3e%3cfETurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3e%3c/filter%3e%3crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3e%3c/g%3e%3c/svg%3e");
    z-index: 2;
}}

/* -- Header & Labels (Engineering side) -- */
.header {{
    position: relative;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    letter-spacing: 0.1em;
    color: var(--text-dim);
    border-left: 4px solid var(--accent);
    padding-left: 20px;
    text-transform: uppercase;
}}

.slide-number {{
    font-weight: 600;
    color: var(--accent);
}}

/* -- Content Card -- */
.content-wrapper {{
    position: relative;
    z-index: 10;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 40px;
}}

.title {{
    font-family: 'Lora', serif;
    font-size: 82px;
    line-height: 1.1;
    font-weight: 600;
    color: var(--text);
    /* Subtle glow */
    text-shadow: 0 0 30px rgba(255,255,255,0.1);
}}

.title italic, .title em {{
    font-weight: 500;
    font-style: italic;
    color: var(--poetic);
}}

.body-text {{
    font-size: 38px;
    line-height: 1.5;
    font-weight: 300;
    color: var(--text-dim);
    max-width: 850px;
    background: var(--glass);
    padding: 30px;
    border-radius: 12px;
    border: 1px solid var(--border);
    backdrop-filter: blur(10px);
}}

.body-text ul {{
    list-style: none;
    padding-top: 10px;
}}

.body-text li {{
    position: relative;
    padding-left: 40px;
    margin-bottom: 15px;
}}

.body-text li::before {{
    content: "0" counter(item);
    counter-increment: item;
    position: absolute;
    left: 0;
    color: var(--accent);
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 600;
    opacity: 0.7;
    top: 10px;
}}

/* -- Footer -- */
.footer {{
    position: relative;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    color: var(--text-dim);
}}

.signature {{
    color: var(--poetic);
    font-weight: 600;
    letter-spacing: 0.05em;
}}

.handle {{
    opacity: 0.5;
}}

/* -- Variants -- */
.slide.capa .title {{
    font-size: 100px;
    background: linear-gradient(to right, #fff, var(--poetic));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.slide.capa .body-text {{
    background: none;
    border: none;
    padding: 0;
    backdrop-filter: none;
    font-size: 42px;
    color: var(--accent);
}}
"""

SLIDE_TEMPLATE = """
<div class="slide {capa_class}" id="slide-{idx}">
    <div class="header">
        <span>{categoria}</span>
        <span class="slide-number">{counter}</span>
    </div>
    
    <div class="content-wrapper">
        <h1 class="title">{signal_html}</h1>
        <div class="body-text" style="counter-reset: item;">
            {context_html}
        </div>
    </div>
    
    <div class="footer">
        <div class="signature">Poética Racional</div>
        <div class="handle">{detail}</div>
    </div>
</div>
"""

def parse_slides(md_text: str) -> list[dict]:
    slides = []
    # Tenta focar na seção de slides se houver várias opções
    if "## Opção 2" in md_text:
        md_part = md_text.split("## Opção 2")[1]
    else:
        md_part = md_text
        
    blocks = re.split(r'\n## Slide \d+', md_part)
    for i, block in enumerate(blocks):
        if not block.strip() or "[CATEGORIA]" not in block:
            continue
            
        slide = {}
        slide["categoria"] = (re.search(r'\*\*\[CATEGORIA\]\*\*\s*\[(.+?)\]', block) or type('obj', (object,), {'group': lambda self, x: ''})()).group(1)
        slide["counter"] = (re.search(r'\*\*\[N/TOTAL\]\*\*\s*\[(.+?)\]', block) or type('obj', (object,), {'group': lambda self, x: ''})()).group(1)
        
        signal = (re.search(r'\*\*Signal:\*\*\s*(.+?)(?=\n)', block) or type('obj', (object,), {'group': lambda self, x: ''})()).group(1).strip()
        # Formata itálicos pra poesia
        signal = signal.replace("*", "<em>").replace("</em><em>", "").replace("<em>", "<em>", 1) # Simplista
        slide["signal"] = signal
        
        context_m = re.search(r'\*\*Context:\*\*\s*([\s\S]+?)(?=\*\*Detail:|\*\*Handle:|$)', block)
        slide["context"] = context_m.group(1).strip() if context_m else ""
        
        detail_m = re.search(r'\*\*Detail:\*\*\s*(.+?)(?=\n|$)', block)
        slide["detail"] = detail_m.group(1).strip() if detail_m else "@dougpmoura"
        
        slide["is_capa"] = "01/" in slide["counter"]
        slides.append(slide)
    return slides

def build_context_html(raw: str) -> str:
    lines = [l.strip() for l in raw.split('\n') if l.strip()]
    if any(l.startswith('-') for l in lines):
        items = "".join(f"<li>{l.lstrip('- ').strip()}</li>" for l in lines if l.startswith('-'))
        return f"<ul>{items}</ul>"
    return "<br>".join(lines)

def build_all(md_path: str):
    md_text = Path(md_path).read_text(encoding='utf-8')
    slides = parse_slides(md_text)
    
    if not slides:
        print("❌ Nenhum slide encontrado no Markdown. Verifique o formato.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    html_out = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Preview: Poética Racional v4</title>
        <style>{CSS}</style>
    </head>
    <body>
    """
    
    for idx, slide in enumerate(slides, 1):
        capa_class = " capa" if slide["is_capa"] else ""
        
        html_out += SLIDE_TEMPLATE.format(
            idx=idx,
            capa_class=capa_class,
            categoria=slide["categoria"],
            counter=slide["counter"],
            signal_html=slide["signal"],
            context_html=build_context_html(slide["context"]),
            detail=slide["detail"]
        )
        
    html_out += "</body></html>"
    out_file = OUTPUT_DIR / "preview_v4_premium.html"
    out_file.write_text(html_out, encoding='utf-8')
    print(f"✨ Design Premium 'Poética Racional' gerado em {out_file}", flush=True)

if __name__ == "__main__":
    md_path = sys.argv[1] if len(sys.argv) > 1 else "squads/linkedin-content/output/post-texto-resumo.md"
    build_all(md_path)
