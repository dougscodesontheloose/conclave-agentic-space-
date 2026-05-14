#!/usr/bin/env python3
"""
Conclave Skill Standardization — Phase 4: 5★ Upgrade
Applies missing substantive elements:
1. `type:` in frontmatter
2. `**Core principle:**` after H1
3. `## Prerequisites`
4. `## Phase 0: Intake`
"""

import os
import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent.parent.parent / "skills"

CORE_PRINCIPLES = {
    "scraping": "Dados brutos são passivos; inteligência é o que você recorta do ruído.",
    "outreach": "A verdadeira personalização prova que você fez o dever de casa antes de pedir o tempo do prospect.",
    "lead-generation": "Qualificar cedo custa pouco; desqualificar tarde custa o deal.",
    "monitoring": "Sinais só têm valor se a janela de oportunidade ainda estiver aberta.",
    "research": "Não procure dados que confirmem sua tese; procure assimetrias que o mercado ignora.",
    "competitive-intel": "Movimentos do concorrente são sinais; sua resposta é estratégia.",
    "content": "Atenção não se aluga com volume, se conquista com densidade.",
    "seo": "A intenção do usuário dita a arquitetura; o algoritmo apenas lê o mapa.",
    "system": "Sistemas resilientes assumem a falha como padrão e a recuperação como regra.",
    "ads": "Você não compra cliques, você compra a atenção fracionada do seu melhor cliente.",
    "general": "A precisão da resposta é diretamente proporcional à clareza da intenção."
}

def get_tags(content: str) -> list:
    match = re.search(r"^tags:\s*\[([^\]]+)\]", content, re.MULTILINE)
    if match:
        return [t.strip() for t in match.group(1).split(",")]
    return []

def detect_category(tags: list) -> str:
    categories = ["scraping", "outreach", "lead-generation", "monitoring", "research", "competitive-intel", "content", "seo", "system", "ads"]
    for t in tags:
        if t in categories:
            return t
    if any(t in ["social-media", "design"] for t in tags): return "content"
    if any(t in ["signals"] for t in tags): return "monitoring"
    if any(t in ["development", "orchestration", "automation"] for t in tags): return "system"
    return "general"

def generate_prerequisites(category: str, content: str) -> str:
    section = "\n## Prerequisites\n\n### Environment Variables\n\n```env\n"
    if "apify" in content.lower():
        section += "APIFY_API_TOKEN=required_for_scraping\n"
    elif "firecrawl" in content.lower():
        section += "FIRECRAWL_API_KEY=required_for_extraction\n"
    elif category == "outreach":
        section += "# EX: RESEND_API_KEY=your_token_here\n"
    else:
        section += "# Nenhuma variável obrigatória estrita\n"
    section += "```\n\n### Dependencies\n\n"
    if "python" in content.lower() or "bash" in content.lower():
        section += "Requer ambiente de execução padrão do Conclave.\n"
    else:
        section += "Nenhuma. Pure reasoning skill.\n"
    return section

def generate_phase0(category: str) -> str:
    section = "\n## Phase 0: Intake\n\nPerguntas obrigatórias antes da execução:\n\n"
    if category == "scraping":
        section += "1. **Alvo** — Qual a URL ou fonte específica?\n2. **Foco** — Que tipo de dados são mais críticos?\n3. **Formato** — JSON, CSV ou Markdown?\n"
    elif category in ("outreach", "lead-generation"):
        section += "1. **ICP** — Qual o perfil ideal exato que estamos buscando?\n2. **Contexto** — Qual a dor que nossa abordagem resolve?\n3. **Volume** — Limite de leads/mensagens por lote?\n"
    elif category in ("research", "competitive-intel"):
        section += "1. **Entidade alvo** — Empresa, pessoa ou tendência?\n2. **Profundidade** — Visão geral (quick) ou análise profunda (deep)?\n3. **Objetivo** — O que esta pesquisa deve destravar no seu projeto?\n"
    elif category == "content":
        section += "1. **Audiência** — Para quem estamos escrevendo/criando?\n2. **Tom de Voz** — Qual a diretriz de marca a ser usada?\n3. **Canal** — Onde isso será publicado?\n"
    elif category == "system":
        section += "1. **Escopo** — Quais arquivos ou diretórios serão afetados?\n2. **Objetivo** — Qual o estado final desejado?\n3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?\n"
    else:
        section += "1. **Contexto** — Qual a situação atual?\n2. **Objetivo** — O que define o sucesso desta execução?\n3. **Restrições** — O que não devemos fazer?\n"
    return section

def process_file(path: Path, dry_run: bool):
    content = path.read_text(encoding="utf-8")
    
    # Skip non-standard MCPs or overly short prompt pointers
    if "type: mcp" in content or len(content.splitlines()) < 15:
        return []
        
    tags = get_tags(content)
    category = detect_category(tags)
    
    changes_made = []
    
    # 1. Add type if missing
    if not re.search(r"^type:\s+", content, re.MULTILINE):
        content = re.sub(r"^(---.*?)\n(---)$", r"\1\ntype: playbook\n\2", content, count=1, flags=re.DOTALL)
        changes_made.append("type")
        
    # 2. Add Core principle
    if "Core principle:" not in content and "**Core" not in content:
        principle = CORE_PRINCIPLES.get(category, CORE_PRINCIPLES["general"])
        # Insert after the first H1
        content = re.sub(r"^(#\s+.*?)$", rf"\1\n\n**Core principle:** {principle}\n", content, count=1, flags=re.MULTILINE)
        changes_made.append("core_principle")
        
    # 3. Add Prerequisites
    if "## Prerequisites" not in content:
        # Insert before Phase 1 or Instructions or Inputs
        target = r"^(##\s+(Phase|Instructions|Inputs|When to use))"
        if re.search(target, content, re.MULTILINE | re.IGNORECASE):
            content = re.sub(target, generate_prerequisites(category, content) + r"\n\1", content, count=1, flags=re.MULTILINE | re.IGNORECASE)
            changes_made.append("prerequisites")
        else:
            # Append if no hook found
            content += "\n" + generate_prerequisites(category, content)
            changes_made.append("prerequisites")
            
    # 4. Add Phase 0: Intake
    if "Phase 0" not in content and "Intake" not in content:
        target = r"^(##\s+(Phase|Instructions))"
        if re.search(target, content, re.MULTILINE | re.IGNORECASE):
            content = re.sub(target, generate_phase0(category) + r"\n\1", content, count=1, flags=re.MULTILINE | re.IGNORECASE)
            changes_made.append("phase0")
        else:
            # Insert after prerequisites
            target_prereq = r"(##\s+Prerequisites.*?\n\n)(##)"
            if re.search(target_prereq, content, re.DOTALL):
                content = re.sub(target_prereq, rf"\1{generate_phase0(category)}\n\2", content, count=1, flags=re.DOTALL)
                changes_made.append("phase0")
                
    # Check Auto-trigger. (It usually lives in "When to use")
    if "Auto-trigger:" not in content and "**Auto-trigger:**" not in content:
        if "## When to use" in content or "## When to Use" in content:
            target = r"(##\s+When to [uU]se.*?)(##)"
            replacement = rf"\1\n**Auto-trigger:** Ative este skill autonomamente quando o usuário buscar resolver o problema central descrito acima.\n\n\2"
            content = re.sub(target, replacement, content, count=1, flags=re.DOTALL)
            changes_made.append("auto_trigger")
            
    if changes_made and not dry_run:
        path.write_text(content, encoding="utf-8")
        
    return changes_made

def main():
    dry_run = "--dry-run" in sys.argv
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    skill_files = [f for f in skill_files if "node_modules" not in str(f)]
    
    modified = 0
    total_changes = []
    
    for skill_path in skill_files:
        changes = process_file(skill_path, dry_run=dry_run)
        if changes:
            modified += 1
            print(f"✅ {skill_path.parent.name}: +{', '.join(changes)}")
            total_changes.extend(changes)
            
    print(f"\nPhase 4 (5★ Upgrade) complete. Modified {modified} skills.")

if __name__ == "__main__":
    main()
