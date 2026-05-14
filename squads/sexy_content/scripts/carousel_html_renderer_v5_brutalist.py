#!/usr/bin/env python3
"""
Carousel Renderer v5 — "Brutalismo Transparente" Edition
Design baseado na identidade "Poética Racional":
- Estética inspirada em Nothing Phone, Teenage Engineering e Posters da NASA.
- Fundo clear com grid milimetrado (blueprint).
- Tipografia em alto contraste: Inter (Grosseira/Objetiva) + JetBrains Mono (Código).
- Elementos orgânicos simulados através do espaço vazio e assimetria radical.
"""

import re
import os
import sys
from pathlib import Path

OUTPUT_DIR = Path("squads/linkedin-content/output/carousel")

THEMES = {
    "brutalist": {
        "bg": "#f4f4f5", "grid": "#e4e4e7", "accent": "#FF6B00", "text_main": "#09090b", "text_dim": "#71717a"
    },
    "mint": {
        "bg": "#f0fdf4", "grid": "#dcfce7", "accent": "#059669", "text_main": "#064e3b", "text_dim": "#34d399"
    },
    "deep_sea": {
        "bg": "#f0f9ff", "grid": "#e0f2fe", "accent": "#0284c7", "text_main": "#0c4a6e", "text_dim": "#38bdf8"
    },
    "cyber": {
        "bg": "#fafafa", "grid": "#f4f4f5", "accent": "#8b5cf6", "text_main": "#2e1065", "text_dim": "#a78bfa"
    }
}

# Configuração padrão (selecionada via argumento ou automática)
SELECTED_THEME = "brutalist"
if len(sys.argv) > 2 and sys.argv[2] in THEMES:
    SELECTED_THEME = sys.argv[2]

theme = THEMES[SELECTED_THEME]

COLORS = {
    "bg":          theme["bg"],
    "grid":        theme["grid"],
    "surface":     "rgba(255, 255, 255, 0.7)", 
    "accent":      theme["accent"],
    "text_main":   theme["text_main"],
    "text_dim":    theme["text_dim"],
    "border":      theme["text_main"], # Borda segue o texto principal
}

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&family=Inter:wght@400;600;800&family=Lora:ital,wght@1,500&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
    --bg: {COLORS['bg']};
    --grid: {COLORS['grid']};
    --surface: {COLORS['surface']};
    --accent: {COLORS['accent']};
    --text: {COLORS['text_main']};
    --text-dim: {COLORS['text_dim']};
    --border: {COLORS['border']};
}}

body {{
    background: #e5e5e5;
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
    padding: 60px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    background-color: var(--bg);
    overflow: hidden;
    /* Scale for preview */
    transform: scale(0.6);
    transform-origin: top left;
    margin-bottom: -432px;
    margin-right: -432px;
    box-shadow: 20px 20px 0px rgba(0,0,0,0.1);
    border: 2px solid var(--border);
}}

/* -- Engineering Grid Pattern -- */
.slide::before {{
    content: "";
    position: absolute;
    inset: 0;
    pointer-events: none;
    background-image: 
        linear-gradient(to right, var(--grid) 1px, transparent 1px),
        linear-gradient(to bottom, var(--grid) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: 1;
}}

/* -- Blueprint Corner Marks -- */
.slide::after {{
    content: "+";
    position: absolute;
    top: 40px;
    right: 40px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 24px;
    color: var(--border);
    z-index: 5;
}}

.content-layer {{
    position: relative;
    z-index: 10;
    height: 100%;
    display: flex;
    flex-direction: column;
}}

/* -- Header & Labels (Engineering Metadados) -- */
.header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    letter-spacing: 0.05em;
    color: var(--text-dim);
    text-transform: uppercase;
    font-weight: 600;
}}

.metadata-box {{
    border: 2px solid var(--border);
    background: var(--surface);
    backdrop-filter: blur(12px);
    padding: 10px 16px;
    display: flex;
    flex-direction: column;
    gap: 4px;
}}

.metadata-box span.val {{
    color: var(--border);
    font-size: 20px;
}}

.accent-tag {{
    background: var(--accent);
    color: #fff;
    padding: 4px 12px;
    font-size: 14px;
}}

/* -- Content Card -- */
.content-wrapper {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 40px;
    margin-left: 40px; /* Assimetria brutalista */
    padding-right: 40px;
}}

/* O famoso "gear" / Forma preta forte do lado esquerdo (como no poster SWE) */
.brutalist-block {{
    position: absolute;
    left: -40px;
    top: 30%;
    width: 60px;
    height: 300px;
    background: var(--border);
    z-index: 5;
}}

.title {{
    font-family: 'Inter', sans-serif;
    font-size: 85px;
    line-height: 1.05;
    font-weight: 800;
    color: var(--text);
    letter-spacing: -0.03em;
    max-width: 900px;
}}

.title italic, .title em {{
    font-family: 'Lora', serif;
    font-weight: 500;
    font-style: italic;
    color: var(--text);
}}

.body-text {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 32px;
    line-height: 1.5;
    font-weight: 400;
    color: var(--text);
    max-width: 800px;
    background: var(--surface);
    padding: 30px;
    border-left: 6px solid var(--accent);
    backdrop-filter: blur(5px);
}}

.body-text ul {{
    list-style: none;
}}

.body-text li {{
    position: relative;
    padding-left: 30px;
    margin-bottom: 20px;
}}

.body-text li::before {{
    content: ">> ";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-weight: 800;
}}

/* -- Footer -- */
.footer {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    color: var(--border);
    font-weight: 600;
}}

.barcode {{
    font-family: 'Libre Barcode 39', monospace; /* Fonte fake p/ barcode ou simulação com pipes */
    font-weight: normal;
    font-size: 18px;
    letter-spacing: 2px;
    opacity: 0.8;
}}

/* -- Variants -- */
.slide.capa {{
    background: var(--border); /* Preto Total */
    color: #fff;
    border-color: var(--bg);
}}

.slide.capa::before {{
    background-image: 
        linear-gradient(to right, rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255,255,255,0.05) 1px, transparent 1px);
}}

.slide.capa .brutalist-block {{
    display: none;
}}

.slide.capa .title {{
    color: #fff;
    font-size: 110px;
    margin-left: 0;
    margin-bottom: 60px;
}}

.slide.capa .body-text {{
    background: transparent;
    border-left: none;
    color: var(--accent);
    font-family: 'Inter', sans-serif;
    font-weight: 800;
    font-size: 40px;
    padding: 0;
    max-width: 750px;
    line-height: 1.3;
}}

.slide.capa .metadata-box {{
    background: transparent;
    border-color: rgba(255,255,255,0.2);
    color: #fff;
}}

.slide.capa .metadata-box span.val {{
    color: #fff;
}}

.slide.capa .footer {{
    color: rgba(255,255,255,0.5);
}}

.slide.capa .handle {{
    display: none;
}}
"""

SLIDE_TEMPLATE = """
<div class="slide {capa_class}" id="slide-{idx}">
    <div class="content-layer">
        <div class="header">
            <div class="metadata-box">
                <span>SECT.</span>
                <span class="val">{categoria}</span>
            </div>
            <div class="metadata-box">
                <span>PAGE</span>
                <span class="val">{counter}</span>
            </div>
        </div>
        
        <div class="content-wrapper">
            <div class="brutalist-block"></div>
            <h1 class="title">{signal_html}</h1>
            <div class="body-text">
                {context_html}
            </div>
        </div>
        
        <div class="footer">
            <div class="brand">SYS.DOUGLAS</div>
            <div class="barcode">|| | | | || | | || | | </div>
            <div class="handle">{detail}</div>
        </div>
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
    return "<br><br>".join(lines)

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
        <title>Preview: Brutalismo Transparente v5</title>
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
            counter=slide["counter"].replace("/", " / "),
            signal_html=slide["signal"],
            context_html=build_context_html(slide["context"]),
            detail=slide["detail"]
        )
        
    html_out += "</body></html>"
    out_file = OUTPUT_DIR / f"preview_v5_{SELECTED_THEME}.html"
    out_file.write_text(html_out, encoding='utf-8')
    print(f"✨ Tema '{SELECTED_THEME}' gerado em {out_file}", flush=True)

if __name__ == "__main__":
    md_path = sys.argv[1] if len(sys.argv) > 1 else "squads/linkedin-content/output/post-texto-resumo.md"
    build_all(md_path)
