#!/usr/bin/env python3
"""
Conclave Skill Standardization — Phase 3: Quality Leveling
Adds missing structural sections to skills below the quality line.
All changes are ADDITIVE.

Focuses on skills score 3-7 that are functional but under-documented.
Skills score 1-2 (prompt/pointer skills) are handled separately with lighter touch.
"""

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent.parent.parent / "skills"

# ──────────────────────────────────────────────
# QUALITY CHECKS
# ──────────────────────────────────────────────

def has_pattern(content, pattern):
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))

def has_when_to_use(content):
    return has_pattern(content, r"^#{2,3}\s+(When to Use|Quando usar|Trigger|Auto.Trigger|Use Cases)")

def has_inputs(content):
    return has_pattern(content, r"^#{2,3}\s+(Input|Inputs|Prerequisites|Dependencies|Requirements)")

def has_output_format(content):
    return has_pattern(content, r"^#{2,3}\s+(Output|Output Format|Output Schema|Outputs|Deliverables)")

def has_cost(content):
    return has_pattern(content, r"^#{2,3}\s+Cost")

def has_quick_start(content):
    return has_pattern(content, r"^#{2,3}\s+(Quick Start|Getting Started|Usage)")

def get_tags(content):
    match = re.search(r"^tags:\s*\[([^\]]+)\]", content, re.MULTILINE)
    if match:
        return [t.strip() for t in match.group(1).split(",")]
    return []

def get_skill_name(content):
    match = re.search(r"^name:\s*(.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else "unknown"

def get_description(content):
    # Try single-line description
    match = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
    if match:
        desc = match.group(1).strip()
        if not desc.startswith(">"):
            return desc
    # Try multiline description
    match = re.search(r"^description:\s*>\s*\n((?:\s+.+\n)+)", content, re.MULTILINE)
    if match:
        return " ".join(line.strip() for line in match.group(1).strip().splitlines())
    return ""

def detect_skill_category(tags):
    """Map tags to a functional category for contextual section generation."""
    if any(t in tags for t in ["scraping"]):
        return "scraping"
    if any(t in tags for t in ["outreach"]):
        return "outreach"
    if any(t in tags for t in ["lead-generation"]):
        return "lead-gen"
    if any(t in tags for t in ["monitoring", "signals"]):
        return "monitoring"
    if any(t in tags for t in ["competitive-intel", "research"]):
        return "research"
    if any(t in tags for t in ["content", "design"]):
        return "content"
    if any(t in tags for t in ["seo"]):
        return "seo"
    if any(t in tags for t in ["system", "development"]):
        return "system"
    return "general"

def is_pointer_skill(content):
    """Skills that are mainly pointers to other files or pure prompts."""
    lines = [l for l in content.splitlines() if l.strip() and not l.startswith("---") and not l.startswith("#")]
    # If the actual content (non-frontmatter, non-heading) is very short
    body_lines = []
    in_frontmatter = False
    for line in content.splitlines():
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue
        if not in_frontmatter and line.strip():
            body_lines.append(line)
    return len(body_lines) < 15


# ──────────────────────────────────────────────
# SECTION GENERATORS
# ──────────────────────────────────────────────

def generate_when_to_use(name, desc, category):
    section = f"\n## When to Use\n\n"
    
    if category == "scraping":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Collect data from external sources for downstream analysis\n"
        section += f"- Feed data into research, qualification, or monitoring pipelines\n"
        section += f"- Build datasets for competitive intelligence or lead generation\n"
    elif category == "outreach":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Engage prospects with personalized messaging\n"
        section += f"- Execute a multi-touch outreach sequence\n"
        section += f"- Convert qualified leads into conversations\n"
    elif category == "lead-gen":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Identify and qualify potential leads\n"
        section += f"- Build prospect lists from signal sources\n"
        section += f"- Enrich contact data for outreach\n"
    elif category == "monitoring":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Track changes in external sources over time\n"
        section += f"- Detect signals that indicate buying intent or market shifts\n"
        section += f"- Generate periodic intelligence reports\n"
    elif category == "research":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Deep-dive into a company, market, or competitive landscape\n"
        section += f"- Produce structured analysis for strategic decisions\n"
        section += f"- Support other skills with contextual intelligence\n"
    elif category == "content":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Create or transform content assets\n"
        section += f"- Generate visual or written deliverables\n"
        section += f"- Support marketing or sales with ready-to-use materials\n"
    elif category == "system":
        section += f"Use `{name}` when you need to:\n"
        section += f"- Maintain system health and operational quality\n"
        section += f"- Apply development best practices\n"
        section += f"- Support the infrastructure that other skills depend on\n"
    else:
        section += f"Use `{name}` when the task requires its specific capabilities as described above.\n"
    
    section += f"\n**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.\n"
    return section


def generate_inputs(name, content, category):
    section = "\n## Inputs\n\n"
    
    has_api = has_pattern(content, r"api.key|API_TOKEN|APIFY|env.var")
    has_csv = has_pattern(content, r"\.csv|CSV")
    has_url = has_pattern(content, r"--url|url.*input|target.*url")
    
    section += "| Input | Required | Description |\n"
    section += "|---|---|---|\n"
    
    if category == "scraping":
        if has_url:
            section += "| **Target URL(s)** | Yes | URL(s) to scrape |\n"
        section += "| **Keywords/Query** | Varies | Search terms or filters |\n"
        if has_api:
            section += "| **API credentials** | Yes | API key (set via environment variable) |\n"
        section += "| **Output format** | No | `json` (default) or `csv` |\n"
    elif category in ("lead-gen", "outreach"):
        section += "| **Lead list / Company target** | Yes | CSV, pasted list, or upstream skill output |\n"
        section += "| **ICP criteria** | Recommended | Qualification parameters for filtering |\n"
        if has_api:
            section += "| **API credentials** | Yes | API key (set via environment variable) |\n"
    elif category == "monitoring":
        section += "| **Configuration** | Yes | Keywords, sources, and monitoring parameters |\n"
        section += "| **Lookback period** | No | Days to scan (default: 1 for daily, 7 for weekly) |\n"
        if has_api:
            section += "| **API credentials** | Yes | API key (set via environment variable) |\n"
    elif category == "research":
        section += "| **Company/Topic** | Yes | The subject of research |\n"
        section += "| **Company context** | Recommended | `company.md` for strategic alignment |\n"
        section += "| **Depth level** | No | Quick scan vs. deep dive |\n"
    elif category == "content":
        section += "| **Content brief / Data** | Yes | Structured data or brief to generate from |\n"
        section += "| **Brand config** | Recommended | Colors, fonts, tone (from visual-brand-extractor) |\n"
        section += "| **Output format** | No | HTML, PNG, PDF, or Markdown |\n"
    elif category == "system":
        section += "| **Target scope** | Varies | Files, directories, or codebase to operate on |\n"
        section += "| **Configuration** | No | Settings or preferences for the operation |\n"
    else:
        section += "| **Primary input** | Yes | As described in the skill instructions |\n"
        section += "| **Configuration** | No | Optional parameters for customization |\n"
    
    return section


def generate_output_format(name, category):
    section = "\n## Output Format\n\n"
    
    if category == "scraping":
        section += "| Output | Format | Location |\n"
        section += "|---|---|---|\n"
        section += "| **Raw data** | JSON or CSV | Current working directory or specified path |\n"
        section += "| **Summary** | Markdown table | Displayed to user in terminal |\n"
        section += "| **Error log** | Inline notes | Included in output when sources fail |\n"
    elif category in ("lead-gen", "outreach"):
        section += "| Output | Format | Location |\n"
        section += "|---|---|---|\n"
        section += "| **Lead list** | CSV | `{name}-{YYYY-MM-DD}.csv` |\n"
        section += "| **Summary report** | Markdown | Displayed to user |\n"
        section += "| **Qualification verdicts** | Inline | Included per lead in CSV |\n"
    elif category == "monitoring":
        section += "| Output | Format | Location |\n"
        section += "|---|---|---|\n"
        section += "| **Intelligence briefing** | Markdown | `{name}-scan-{YYYY-MM-DD}.md` |\n"
        section += "| **Signal alerts** | Structured list | Included in briefing |\n"
        section += "| **Scan statistics** | Summary table | End of briefing |\n"
    elif category == "research":
        section += "| Output | Format | Location |\n"
        section += "|---|---|---|\n"
        section += "| **Analysis report** | Markdown | Current working directory |\n"
        section += "| **Key findings** | Structured sections | Within report |\n"
        section += "| **Recommendations** | Actionable list | End of report |\n"
    elif category == "content":
        section += "| Output | Format | Location |\n"
        section += "|---|---|---|\n"
        section += "| **Content asset** | HTML / PNG / Markdown | Current working directory |\n"
        section += "| **Preview** | Browser or inline | Presented for user approval |\n"
    elif category == "system":
        section += "| Output | Format | Location |\n"
        section += "|---|---|---|\n"
        section += "| **Status report** | Markdown or terminal | Displayed to user |\n"
        section += "| **Changes applied** | Log | Inline in response |\n"
    else:
        section += "Output is delivered in the format most appropriate to the task, typically Markdown or CSV.\n"
    
    return section


def generate_cost(name, content):
    """Generate Cost section based on detected tools."""
    section = "\n## Cost\n\n"
    
    has_apify = has_pattern(content, r"apify|APIFY")
    has_free_api = has_pattern(content, r"free.*api|no.*api.*key|algolia|CDX")
    is_pure_reasoning = not has_pattern(content, r"python3|bash|curl|npx|script")
    
    if is_pure_reasoning:
        section += "Free. Pure reasoning skill — no external API calls or credits required.\n"
    elif has_free_api:
        section += "Free. Uses public APIs that do not require paid credentials.\n"
    elif has_apify:
        section += "| Component | Cost |\n"
        section += "|---|---|\n"
        section += "| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |\n"
        section += "| Apify free tier | $5/month included |\n"
        section += "| LLM reasoning | Free (included in agent session) |\n"
    else:
        section += "| Component | Cost |\n"
        section += "|---|---|\n"
        section += "| External API calls | Varies by provider (check API documentation) |\n"
        section += "| LLM reasoning | Free (included in agent session) |\n"
    
    return section


# ──────────────────────────────────────────────
# MAIN PROCESSOR
# ──────────────────────────────────────────────

def compute_score(content):
    lines = len(content.splitlines())
    sections = len(re.findall(r'^#{2,3}\s+', content, re.MULTILINE))
    
    score = 0
    score += min(3, lines // 50)
    score += min(2, sections // 4)
    score += 1 if has_pattern(content, r'phase\s+\d|step\s+\d|### step|## step') else 0
    score += 1 if has_pattern(content, r'## output|### output|output.format') else 0
    score += 1 if has_pattern(content, r'## input|### input|## prerequisites|## dependencies') else 0
    score += 1 if re.findall(r'\|.*\|.*\|', content) else 0
    score += 1 if re.findall(r'```', content) or has_pattern(content, r'## cli|### cli') else 0
    
    return score


def process_skill(skill_path, dry_run=False):
    content = skill_path.read_text(encoding="utf-8")
    tags = get_tags(content)
    name = get_skill_name(content)
    desc = get_description(content)
    category = detect_skill_category(tags)
    score = compute_score(content)
    
    parts = skill_path.relative_to(SKILLS_DIR).parts
    dir_name = '/'.join(parts[:-1]) if len(parts) > 2 else parts[0]
    
    # Skip skills already at quality line
    if score >= 8:
        return {"skill": dir_name, "score": score, "action": "skip (already at quality)", "added": []}
    
    # Pointer/prompt skills get lighter treatment
    if is_pointer_skill(content):
        additions = []
        if not has_when_to_use(content):
            additions.append(generate_when_to_use(name, desc, category))
        
        if additions and not dry_run:
            # Insert before Memory & Learning section (which exists from Phase 2)
            insert_point = content.find("\n## Memory & Learning")
            if insert_point == -1:
                insert_point = content.find("\n## Quality Gate")
            if insert_point == -1:
                new_content = content.rstrip() + "\n" + "\n".join(additions) + "\n"
            else:
                new_content = content[:insert_point] + "\n".join(additions) + content[insert_point:]
            skill_path.write_text(new_content, encoding="utf-8")
        
        return {"skill": dir_name, "score": score, "action": "pointer (light)", "added": [a.split("\n")[1].strip() for a in additions]}
    
    # Full functional skills get all missing sections
    additions = []
    
    if not has_when_to_use(content):
        additions.append(generate_when_to_use(name, desc, category))
    
    if not has_inputs(content):
        additions.append(generate_inputs(name, content, category))
    
    if not has_output_format(content):
        additions.append(generate_output_format(name, category))
    
    if not has_cost(content):
        additions.append(generate_cost(name, content))
    
    if additions and not dry_run:
        # Insert before Error Handling section (which exists from Phase 2)
        insert_point = content.find("\n## Error Handling")
        if insert_point == -1:
            insert_point = content.find("\n## Composability")
        if insert_point == -1:
            insert_point = content.find("\n## Memory & Learning")
        if insert_point == -1:
            new_content = content.rstrip() + "\n" + "\n".join(additions) + "\n"
        else:
            new_content = content[:insert_point] + "\n".join(additions) + content[insert_point:]
        skill_path.write_text(new_content, encoding="utf-8")
    
    added_names = [a.split("\n")[1].strip() for a in additions] if additions else []
    return {"skill": dir_name, "score": score, "action": "leveled", "added": added_names}


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN — no files will be modified\n")
    
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    skill_files = [f for f in skill_files if "node_modules" not in str(f)]
    
    stats = {
        "total": len(skill_files),
        "leveled": 0,
        "pointer_light": 0,
        "skipped": 0,
        "when_to_use": 0,
        "inputs": 0,
        "output_format": 0,
        "cost": 0,
    }
    
    for skill_path in skill_files:
        result = process_skill(skill_path, dry_run=dry_run)
        
        if result["action"] == "skip (already at quality)":
            stats["skipped"] += 1
            if verbose:
                print(f"  ⏭️  {result['skill']} (score {result['score']})")
        elif result["action"] == "pointer (light)":
            stats["pointer_light"] += 1
            if verbose:
                added = ", ".join(result["added"]) if result["added"] else "none"
                print(f"  📌 {result['skill']} (score {result['score']}): +{added}")
        else:
            stats["leveled"] += 1
            for section_name in result["added"]:
                if "When" in section_name:
                    stats["when_to_use"] += 1
                elif "Input" in section_name:
                    stats["inputs"] += 1
                elif "Output" in section_name:
                    stats["output_format"] += 1
                elif "Cost" in section_name:
                    stats["cost"] += 1
            if verbose:
                added = ", ".join(result["added"]) if result["added"] else "none"
                print(f"  ✅ {result['skill']} (score {result['score']}): +{added}")
    
    print(f"\n{'='*60}")
    print(f"PHASE 3 SUMMARY {'(DRY RUN)' if dry_run else ''}")
    print(f"{'='*60}")
    print(f"Total skills:              {stats['total']}")
    print(f"Skills leveled (full):     {stats['leveled']}")
    print(f"Pointer skills (light):    {stats['pointer_light']}")
    print(f"Skipped (already good):    {stats['skipped']}")
    print(f"")
    print(f"Sections added:")
    print(f"  When to Use:             {stats['when_to_use']}")
    print(f"  Inputs:                  {stats['inputs']}")
    print(f"  Output Format:           {stats['output_format']}")
    print(f"  Cost:                    {stats['cost']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
