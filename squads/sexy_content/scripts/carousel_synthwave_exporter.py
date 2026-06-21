#!/usr/bin/env python3
"""
Carousel Renderer v4 — Synthwave PNG Exporter
Exporta o design Synthwave diretamente para PNGs 1080x1080.
Usa Playwright no navegador do usuário para evitar problemas de sandbox.
"""

import asyncio
import re
import json
import os
import sys
from pathlib import Path

OUTPUT_DIR = Path("squads/linkedin-content/output/carousel_synthwave")

# ─── SYNTHWAVE VISUAL TOKENS ───────────────────────────────────────
COLORS = {
    "bg":      "#090118",  # Dark purple/black
    "surface": "#1B0235",
    "border":  "#FF007F",  # Neon pink
    "amber":   "#00FFFF",  # Cyan
    "white":   "#FFFFFF",
    "slate":   "#FF00FF",  # Magenta
    "dim":     "#8A2BE2",  # Blue Violet
}

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;600&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    width: 1080px;
    height: 1080px;
    background: {COLORS['bg']};
    font-family: 'Inter', sans-serif;
    color: {COLORS['white']};
    overflow: hidden;
}}

.slide {{
    width: 1080px;
    height: 1080px;
    padding: 56px 64px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    background: {COLORS['bg']};
}}

/* ── Assinatura Vertical ────────────────── */
.vertical-signature {{
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%) rotate(90deg);
    transform-origin: right center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    letter-spacing: 0.1em;
    color: {COLORS['dim']};
    white-space: nowrap;
    opacity: 0.8;
}}

.label-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 1px solid {COLORS['border']};
    font-family: 'JetBrains Mono', monospace;
    font-size: 26px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: {COLORS['slate']};
    text-shadow: 0 0 5px {COLORS['slate']};
}}

.content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 32px;
    padding: 40px 0;
}}

.signal {{
    font-weight: 600;
    font-size: 80px;
    line-height: 1.1;
    color: {COLORS['amber']};
    letter-spacing: -0.02em;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}}

.signal.headline {{
    font-size: 64px;
    color: {COLORS['white']};
    text-shadow: none;
}}

.context {{
    font-weight: 300;
    font-size: 42px;
    line-height: 1.55;
    color: {COLORS['white']};
    max-width: 900px;
}}

.context ul {{
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 20px;
}}

.context ul li::before {{
    content: '→ ';
    color: {COLORS['border']};
    font-family: 'JetBrains Mono', monospace;
    font-size: 32px;
    margin-right: 12px;
}}

.detail-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 20px;
    border-top: 1px solid {COLORS['border']};
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: {COLORS['dim']};
}}

.slide.capa .signal {{
    font-size: 72px;
    color: {COLORS['white']};
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}}
.slide.capa .context {{
    font-size: 36px;
    color: {COLORS['amber']};
}}
"""

SLIDE_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>{css}</style>
</head>
<body>
<div class="slide{capa_class}">
    <div class="vertical-signature">LINKEDIN.COM/IN/DOUGPMOURA</div>
    <div class="label-row">
        <span>{categoria}</span>
        <span>{counter}</span>
    </div>
    <div class="content">
        <div class="{signal_class}">{signal_html}</div>
        <div class="context">{context_html}</div>
    </div>
    <div class="detail-row">
        <span>DICAS DO <user_name></span>
        <span style="opacity: 0.8;">{detail}</span>
    </div>
</div>
</body>
</html>"""

def parse_slides(md_text: str) -> list[dict]:
    slides = []
    if "## Opção 2" in md_text:
        md_text = md_text.split("## Opção 2")[1]
    
    blocks = re.split(r'\n## Slide \d+', md_text)
    for i, block in enumerate(blocks):
        if not block.strip():
            continue
        slide = {}
        slide["categoria"] = (re.search(r'\*\*\[CATEGORIA\]\*\*\s*\[(.+?)\]', block) or type('obj', (object,), {'group': lambda self, x: ''})()).group(1)
        slide["counter"] = (re.search(r'\*\*\[N/TOTAL\]\*\*\s*\[(.+?)\]', block) or type('obj', (object,), {'group': lambda self, x: ''})()).group(1)
        slide["signal"] = (re.search(r'\*\*Signal:\*\*\s*(.+?)(?=\n)', block) or type('obj', (object,), {'group': lambda self, x: ''})()).group(1).strip()
        context_m = re.search(r'\*\*Context:\*\*\s*([\s\S]+?)(?=\*\*Detail:|\*\*Handle:|$)', block)
        slide["context"] = context_m.group(1).strip() if context_m else ""
        detail_m = re.search(r'\*\*Detail:\*\*\s*(.+?)(?=\n|$)', block)
        slide["detail"] = detail_m.group(1).strip() if detail_m else ""
        slide["is_capa"] = (i == 1)
        slides.append(slide)
    return slides

def build_context_html(raw: str) -> str:
    lines = [l.strip() for l in raw.split('\n') if l.strip()]
    if any(l.startswith('-') for l in lines):
        items = "".join(f"<li>{l.lstrip('- ').strip()}</li>" for l in lines if l.startswith('-'))
        return f"<ul>{items}</ul>"
    return "<br>".join(lines)

async def render_slides(md_path: str):
    from playwright.async_api import async_playwright
    md_text = Path(md_path).read_text(encoding='utf-8')
    slides = parse_slides(md_text)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})
        for idx, slide in enumerate(slides, 1):
            sc_class = "signal headline" if len(slide["signal"]) > 60 else "signal"
            capa_class = " capa" if slide["is_capa"] else ""
            html = SLIDE_TEMPLATE.format(css=CSS, capa_class=capa_class, categoria=slide["categoria"], counter=slide["counter"], signal_class=sc_class, signal_html=slide["signal"], context_html=build_context_html(slide["context"]), detail=slide["detail"] or "")
            await page.set_content(html, wait_until="networkidle")
            filename = f"synthwave-slide-{idx:02d}.png"
            await page.screenshot(path=str(OUTPUT_DIR / filename))
            print(f"✅ {filename} exportado", flush=True)
        await browser.close()
    print(f"\n🎨 Synthwave PNGs prontos em {OUTPUT_DIR}/", flush=True)

if __name__ == "__main__":
    md_path = sys.argv[1] if len(sys.argv) > 1 else "squads/linkedin-content/output/post-final.md"
    asyncio.run(render_slides(md_path))
