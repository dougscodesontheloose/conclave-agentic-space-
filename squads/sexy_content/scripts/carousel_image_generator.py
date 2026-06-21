import re
import os
import sys
from pathlib import Path

# Pasta de saída
OUTPUT_DIR = Path("squads/linkedin-content/output/carousel")

COLORS = {{
    "bg":      "{bg}",
    "surface": "{surface}",
    "border":  "{border}",
    "amber":   "{amber}",
    "white":   "{white}",
    "slate":   "{slate}",
    "dim":     "{dim}",
}}

# CSS ajustado para exportação individual
CSS = """
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;600&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    background: #000;
    font-family: 'Inter', sans-serif;
    color: {COLORS['white']};
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
    margin: 0;
    overflow: hidden;
}}

/* Assinatura Vertical */
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

SLIDE_TEMPLATE = """
<div class="slide {capa_class}" id="slide-{idx}">
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
"""

# Resto do script de parser e PDF/Image render (independente de Playwright por ora)
# ... adaptando para gerar um HTML por slide para você dar print individual se o automático falhar
