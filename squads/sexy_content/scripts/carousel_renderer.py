#!/usr/bin/env python3
"""
Carousel Renderer — Retro-Futurismo Funcional
Converte post-final.md em PNGs 1080x1080 prontos para LinkedIn.
Dependência: pip install playwright && playwright install chromium
"""

import asyncio
import re
import json
import os
import sys
from pathlib import Path

OUTPUT_DIR = Path("squads/linkedin-content/output/carousel")

# ─── VISUAL IDENTITY TOKENS ────────────────────────────────────────
COLORS = {
    "bg":      "#141716",
    "surface": "#1C201D",
    "border":  "#2A2E2B",
    "amber":   "#C8A951",
    "white":   "#F0EDE6",
    "slate":   "#8B9E92",
    "dim":     "#5A6B60",
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

/* ── Label Row ─────────────────────────── */
.label-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 1px solid {COLORS['border']};
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: {COLORS['slate']};
}}

/* ── Content Area ──────────────────────── */
.content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 28px;
    padding: 32px 0;
}}

/* ── Signal ────────────────────────────── */
.signal {{
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 58px;
    line-height: 1.1;
    color: {COLORS['amber']};
    letter-spacing: -0.02em;
}}

/* Signal variant: long text (headline mode) */
.signal.headline {{
    font-size: 40px;
    color: {COLORS['white']};
}}

/* ── Context ────────────────────────────── */
.context {{
    font-family: 'Inter', sans-serif;
    font-weight: 300;
    font-size: 24px;
    line-height: 1.55;
    color: {COLORS['white']};
    max-width: 820px;
}}

/* context list items */
.context ul {{
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
}}
.context ul li::before {{
    content: '→ ';
    color: {COLORS['amber']};
    font-family: 'JetBrains Mono', monospace;
    font-size: 18px;
    margin-right: 4px;
}}

/* ── Detail Row ─────────────────────────── */
.detail-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 20px;
    border-top: 1px solid {COLORS['border']};
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: {COLORS['dim']};
}}

/* ── Capa (slide 1) variant ─────────────── */
.slide.capa .signal {{
    font-size: 52px;
    color: {COLORS['white']};
}}
.slide.capa .context {{
    font-size: 22px;
    color: {COLORS['slate']};
}}

/* ── Highlight amber on numbers ─────────── */
.amber {{ color: {COLORS['amber']}; }}
"""

SLIDE_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>{css}</style>
</head>
<body>
<div class="slide{capa_class}">
    <div class="label-row">
        <span>{categoria}</span>
        <span>{counter}</span>
    </div>
    <div class="content">
        <div class="{signal_class}">{signal_html}</div>
        <div class="context">{context_html}</div>
    </div>
    <div class="detail-row">
        <span>{detail}</span>
    </div>
</div>
</body>
</html>"""


# ─── PARSER ────────────────────────────────────────────────────────
def parse_slides(md_text: str) -> list[dict]:
    """
    Extrai blocos de slides do markdown no formato:
    ## Slide N — Título
    **[CATEGORIA]** [VALOR]
    **[N/TOTAL]** [VALOR]
    **Signal:** TEXTO
    **Context:** TEXTO
    **Detail:** TEXTO (opcional)
    """
    slides = []
    # Localizar somente a seção do carrossel (Opção 2 se houver)
    if "## Opção 2" in md_text:
        md_text = md_text.split("## Opção 2")[1]
    elif "## Opção 1" in md_text:
        md_text = md_text.split("## Opção 1")[1]

    blocks = re.split(r'\n## Slide \d+', md_text)
    for i, block in enumerate(blocks):
        if not block.strip():
            continue
        slide = {}

        cat_m = re.search(r'\*\*\[CATEGORIA\]\*\*\s*\[(.+?)\]', block)
        slide["categoria"] = cat_m.group(1) if cat_m else ""

        counter_m = re.search(r'\*\*\[N/TOTAL\]\*\*\s*\[(.+?)\]', block)
        slide["counter"] = counter_m.group(1) if counter_m else ""

        signal_m = re.search(r'\*\*Signal:\*\*\s*(.+?)(?=\n)', block)
        slide["signal"] = signal_m.group(1).strip() if signal_m else ""

        # Context: captura até o próximo campo bold ou fim
        context_m = re.search(r'\*\*Context:\*\*\s*([\s\S]+?)(?=\*\*Detail:|\*\*Handle:|$)', block)
        slide["context"] = context_m.group(1).strip() if context_m else ""

        detail_m = re.search(r'\*\*Detail:\*\*\s*(.+?)(?=\n|$)', block)
        slide["detail"] = detail_m.group(1).strip() if detail_m else ""

        slide["is_capa"] = (i == 1)  # primeiro bloco real
        slides.append(slide)

    return slides


def build_context_html(raw: str) -> str:
    """Converte markdown simples para HTML de contexto."""
    lines = [l.strip() for l in raw.split('\n') if l.strip()]
    # Se tem lista de bullets (- item)
    if any(l.startswith('-') for l in lines):
        items = "".join(
            f"<li>{l.lstrip('- ').strip()}</li>"
            for l in lines if l.startswith('-')
        )
        return f"<ul>{items}</ul>"
    return "<br>".join(lines)


def build_html(slide: dict, css: str) -> str:
    signal_text = slide["signal"]
    # Signal longo → headline mode
    signal_class = "signal headline" if len(signal_text) > 60 else "signal"
    capa_class = " capa" if slide["is_capa"] else ""

    return SLIDE_TEMPLATE.format(
        css=css,
        capa_class=capa_class,
        categoria=slide["categoria"],
        counter=slide["counter"],
        signal_class=signal_class,
        signal_html=signal_text,
        context_html=build_context_html(slide["context"]),
        detail=slide["detail"] or "&nbsp;",
    )


# ─── RENDERER ──────────────────────────────────────────────────────
async def render_slides(md_path: str):
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("❌ Playwright não encontrado. Instalando...", flush=True)
        os.system("pip install playwright --quiet && playwright install chromium --quiet")
        from playwright.async_api import async_playwright

    md_text = Path(md_path).read_text(encoding='utf-8')
    slides = parse_slides(md_text)

    if not slides:
        print("❌ Nenhum slide encontrado no arquivo. Verifique o formato.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})

        for idx, slide in enumerate(slides, 1):
            html = build_html(slide, CSS)
            await page.set_content(html, wait_until="networkidle")
            filename = f"slide-{idx:02d}.png"
            filepath = OUTPUT_DIR / filename
            await page.screenshot(path=str(filepath), full_page=False)
            manifest.append({"slide": idx, "file": str(filepath), "signal": slide["signal"]})
            print(f"✅ {filename} exportado", flush=True)

        await browser.close()

    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"\n🎛️ Carrossel completo: {len(slides)} slides em {OUTPUT_DIR}/", flush=True)
    print(f"📋 Manifest salvo em {manifest_path}", flush=True)


if __name__ == "__main__":
    md_path = sys.argv[1] if len(sys.argv) > 1 else "squads/linkedin-content/output/post-final.md"
    asyncio.run(render_slides(md_path))
