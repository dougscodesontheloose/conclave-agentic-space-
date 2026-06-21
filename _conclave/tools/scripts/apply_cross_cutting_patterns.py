#!/usr/bin/env python3
"""
Conclave Skill Standardization — Phase 2: Cross-Cutting Patterns
Applies four transversal patterns to all SKILL.md files:
1. Error Handling section
2. Composability declarations (Chain-to / Composes-with)
3. Memory/Learning hooks
4. Quality Gate / Checkpoint patterns

All changes are ADDITIVE — nothing is removed.
"""

import os
import re
import sys
import json
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent.parent.parent / "skills"

# ──────────────────────────────────────────────
# TAG → COMPOSABILITY MAP
# Defines which skills chain to which, based on functional role
# ──────────────────────────────────────────────

CHAIN_MAP = {
    # Scraping skills → Research/Qualification
    "scraping": {
        "feeds_into": ["lead-qualification", "competitor-intel", "customer-discovery", "industry-scanner"],
        "fed_by": [],
    },
    # Research skills → Outreach/Content
    "research": {
        "feeds_into": ["cold-email-outreach", "linkedin-outreach", "content-asset-creator", "battlecard-generator"],
        "fed_by": ["scraping", "monitoring"],
    },
    # Lead Gen → Outreach
    "lead-generation": {
        "feeds_into": ["cold-email-outreach", "linkedin-outreach", "linkedin-message-writer", "contact-cache"],
        "fed_by": ["scraping", "signals", "research"],
    },
    # Signals → Lead Gen / Outreach
    "signals": {
        "feeds_into": ["lead-qualification", "cold-email-outreach", "linkedin-outreach", "outbound-prospecting-engine"],
        "fed_by": ["scraping", "monitoring"],
    },
    # Monitoring → Signals / Research
    "monitoring": {
        "feeds_into": ["industry-scanner", "signal-detection-pipeline", "competitor-intel"],
        "fed_by": [],
    },
    # Competitive Intel → Strategy / Outreach
    "competitive-intel": {
        "feeds_into": ["battlecard-generator", "launch-positioning-builder", "campaign-brief-generator"],
        "fed_by": ["scraping", "monitoring", "research"],
    },
    # Outreach → Contact Cache / Pipeline
    "outreach": {
        "feeds_into": ["contact-cache", "pipeline-review", "sequence-performance"],
        "fed_by": ["lead-generation", "signals", "research"],
    },
    # Content → Distribution
    "content": {
        "feeds_into": ["create-html-carousel", "create-html-slides", "linkedin-outreach"],
        "fed_by": ["research", "competitive-intel", "brand"],
    },
    # SEO → Content
    "seo": {
        "feeds_into": ["content-brief-factory", "seo-content-engine", "topical-authority-mapper"],
        "fed_by": ["site-content-catalog", "seo-domain-analyzer"],
    },
}


def read_skill(path: Path) -> str:
    """Read a SKILL.md file."""
    return path.read_text(encoding="utf-8")


def get_tags(content: str) -> list:
    """Extract tags from frontmatter."""
    match = re.search(r"^tags:\s*\[([^\]]+)\]", content, re.MULTILINE)
    if match:
        return [t.strip() for t in match.group(1).split(",")]
    return []


def get_skill_name(path: Path) -> str:
    """Get skill name from directory."""
    # Handle nested skills like lead-gen-devtools/community-signals
    parts = path.relative_to(SKILLS_DIR).parts
    if len(parts) > 2:
        return "/".join(parts[:-1])
    return parts[0]


def has_section(content: str, heading: str) -> bool:
    """Check if a section heading exists (## or ###)."""
    pattern = rf"^#{2,3}\s+{re.escape(heading)}"
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))


def has_any_error_section(content: str) -> bool:
    """Check if any error handling section exists."""
    patterns = [
        r"^#{2,3}\s+Error\s+Handling",
        r"^#{2,3}\s+Troubleshooting",
        r"^#{2,3}\s+Fallback",
        r"^#{2,3}\s+Error\s+Recovery",
    ]
    return any(re.search(p, content, re.MULTILINE | re.IGNORECASE) for p in patterns)


def has_composability_section(content: str) -> bool:
    """Check if composability declarations exist."""
    patterns = [
        r"^#{2,3}\s+Composability",
        r"^#{2,3}\s+Related Skills",
        r"^#{2,3}\s+Downstream Skills",
        r"^#{2,3}\s+Chain",
        r"^#{2,3}\s+Composes",
        r"feeds.into\b",
        r"chains?\s+(to|from|with)\b",
    ]
    return any(re.search(p, content, re.MULTILINE | re.IGNORECASE) for p in patterns)


def has_memory_hooks(content: str) -> bool:
    """Check if memory/learning hooks exist."""
    patterns = [
        r"^#{2,3}\s+Memory",
        r"^#{2,3}\s+Learning",
        r"memories\.md",
        r"squad.*memory",
    ]
    return any(re.search(p, content, re.MULTILINE | re.IGNORECASE) for p in patterns)


def has_quality_gate(content: str) -> bool:
    """Check if quality gate / checkpoint exists."""
    patterns = [
        r"^#{2,3}\s+Quality",
        r"^#{2,3}\s+Checkpoint",
        r"^#{2,3}\s+Validation",
        r"^#{2,3}\s+Output Validation",
        r"present.*user.*confirm",
        r"checkpoint",
        r"before proceeding.*confirm",
    ]
    return any(re.search(p, content, re.MULTILINE | re.IGNORECASE) for p in patterns)


def uses_external_tools(content: str) -> bool:
    """Check if skill uses external tools/APIs."""
    patterns = [
        r"python3\s+",
        r"curl\s+",
        r"npx\s+",
        r"pip\s+install",
        r"apify",
        r"api[_\s]key",
        r"API_TOKEN",
        r"APIFY",
    ]
    return any(re.search(p, content, re.IGNORECASE) for p in patterns)


def detect_skill_type(content: str, tags: list) -> str:
    """Detect the skill type for tailored error handling."""
    if any(t in tags for t in ["scraping", "social-media"]):
        return "scraping"
    if any(t in tags for t in ["outreach", "lead-generation"]):
        return "outreach"
    if any(t in tags for t in ["research", "competitive-intel"]):
        return "research"
    if any(t in tags for t in ["content", "design"]):
        return "content"
    if any(t in tags for t in ["system", "development"]):
        return "system"
    if any(t in tags for t in ["monitoring", "signals"]):
        return "monitoring"
    if any(t in tags for t in ["seo"]):
        return "seo"
    if any(t in tags for t in ["ads"]):
        return "ads"
    return "general"


# ──────────────────────────────────────────────
# TEMPLATE GENERATORS
# ──────────────────────────────────────────────

def generate_error_handling(skill_type: str, skill_name: str) -> str:
    """Generate Error Handling section based on skill type."""

    base = """
## Error Handling

"""

    if skill_type == "scraping":
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **API rate limit / 429** | HTTP 429 or `rate_limit` in response | Wait 60s, retry with exponential backoff (max 3 retries) |
| **API key missing/invalid** | HTTP 401/403 or env var not set | Log `❌ Missing API key: [VAR_NAME]`. Stop and inform user with setup instructions |
| **Target page structure changed** | Zero results from a previously working source | Log `⚠️ 0 results from [source]`. Continue with other sources, flag in output |
| **Network timeout** | No response within configured timeout | Retry once. If still failing, skip source and note in output |
| **Empty dataset returned** | Valid API response but 0 results | Distinguish "no data exists" vs "query too narrow". Suggest query adjustments |

**Principle:** Never fail silently. Every error must produce a visible log line and a note in the final output.
"""

    elif skill_type == "outreach":
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **Contact not found** | Empty result from people search | Log `⚠️ No contacts found for [company]`. Skip to next company, note gap in output |
| **Enrichment failed** | API error or missing fields | Use partial data. Mark enrichment_status as `partial` in output |
| **Duplicate contact detected** | Match on LinkedIn URL or email in contact-cache | Skip duplicate, log `ℹ️ Skipped duplicate: [name]` |
| **Template rendering failed** | Missing personalization variables | Fall back to generic template. Flag `⚠️ Low personalization` in output |
| **Outreach tool connection failed** | API error from outreach platform | Export to CSV as fallback. Inform user of manual upload path |

**Principle:** Partial success is better than total failure. Always produce an output, even if degraded.
"""

    elif skill_type == "research":
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **Primary source unavailable** | HTTP error or empty response | Fall back to WebSearch as secondary source. Note `⚠️ Primary source unavailable` |
| **Insufficient data for analysis** | Fewer than minimum data points required | Lower confidence level of findings. Mark as `low-confidence` in output |
| **Conflicting data across sources** | Contradictory information found | Report both versions with sources. Let user resolve the conflict |
| **Rate limiting on research queries** | Throttled responses | Space queries with 2-3s delays. Reduce parallel requests |
| **Stale data detected** | Dates older than threshold (varies by use case) | Flag `⚠️ Data may be stale (from [date])`. Suggest re-running with fresh sources |

**Principle:** Always cite sources. When data is uncertain, say so explicitly rather than presenting low-confidence findings as facts.
"""

    elif skill_type == "content":
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **External API unavailable** (Gamma, v0) | HTTP error or timeout | Fall back to self-hosted HTML generation. Log `ℹ️ Using HTML fallback` |
| **Font loading failed** | Timeout on font CDN | Use system font stack as fallback. Note in output |
| **Screenshot generation failed** | Playwright/browser error | Provide HTML files and manual screenshot instructions |
| **Content exceeds format limits** | Text overflow or slide count exceeded | Split into multiple units. Warn user about content volume |
| **Brand config missing** | No brand JSON found | Use neutral default palette. Ask user for brand details |

**Principle:** Always produce a deliverable, even if lower fidelity than ideal.
"""

    elif skill_type == "system":
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **Dependency not installed** | ImportError or command not found | Log exact install command needed. Do not attempt auto-install without user consent |
| **Permission denied** | OS permission error | Log the specific path and required permission. Suggest fix command |
| **Configuration missing** | Required config file not found | Provide template with defaults. Ask user to fill required fields |
| **Disk space insufficient** | Write failure or quota error | Run cleanup suggestions. Warn before large operations |

**Principle:** System skills must be self-diagnosing. Every failure should include the exact fix command.
"""

    elif skill_type == "monitoring":
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **Source temporarily unavailable** | HTTP error or timeout on monitored source | Skip source for this scan cycle. Note in output `⚠️ [source] unavailable` |
| **No new signals detected** | Valid scan but 0 new items | Report clean scan explicitly: "No new signals detected (sources: X scanned)". Don't fail silently |
| **Keyword config outdated** | Consistently 0 matches across multiple scans | Suggest keyword review. Log `ℹ️ Consider updating keywords — 0 matches in last N scans` |
| **API credits exhausted** | Credit limit or quota error | Switch to free alternatives where available. Log remaining credit status |
| **Duplicate signals from prior scan** | Match against previous scan results | Deduplicate. Only surface genuinely new items |

**Principle:** Monitoring skills must clearly distinguish "nothing happened" from "scan failed". Both are valid but mean different things.
"""

    else:  # general / ads / seo
        return base + """| Failure Mode | Detection | Recovery |
|---|---|---|
| **API/tool unavailable** | HTTP error, timeout, or command failure | Log the specific error. Attempt retry once. If still failing, skip and note in output |
| **Insufficient input data** | Missing required fields or empty dataset | Prompt user for missing data. Do not proceed with assumptions on critical fields |
| **Unexpected data format** | Parse error or schema mismatch | Log the raw response snippet. Attempt best-effort parsing. Flag `⚠️ Data format unexpected` |
| **Rate limiting** | HTTP 429 or throttle signal | Implement exponential backoff (1s → 2s → 4s). Max 3 retries |
| **Partial results** | Some sources succeed, others fail | Deliver partial results with clear indication of which sources failed and why |

**Principle:** Every execution must produce either a result or a clear, actionable error message. Silent failures are unacceptable.
"""


def generate_composability(tags: list, skill_name: str) -> str:
    """Generate Composability section based on tags."""
    feeds_into = set()
    fed_by = set()

    for tag in tags:
        if tag in CHAIN_MAP:
            feeds_into.update(CHAIN_MAP[tag]["feeds_into"])
            fed_by.update(CHAIN_MAP[tag]["fed_by"])

    # Remove self-references
    feeds_into.discard(skill_name)
    fed_by.discard(skill_name)

    if not feeds_into and not fed_by:
        return ""

    section = "\n## Composability\n\n"

    if fed_by:
        section += "**Receives data from:**\n"
        for source in sorted(fed_by):
            section += f"- Skills tagged `{source}` (e.g., data collection and enrichment)\n"

    if feeds_into:
        section += "\n**Feeds into:**\n"
        for target in sorted(feeds_into):
            section += f"- `{target}`\n"

    section += """
**Integration pattern:** This skill can be called standalone or as part of a pipeline. When chaining, pass the output path as input to the downstream skill.
"""
    return section


def generate_memory_hooks(skill_name: str) -> str:
    """Generate Memory/Learning hooks section."""
    return f"""
## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: {skill_name} — [finding]` | `[OPERACIONAL]: {skill_name} — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: {skill_name} — [param] works better as [value]` | `[OPERACIONAL]: {skill_name} — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: {skill_name} — [insight]` | `[ESTRATÉGICO]: {skill_name} — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry
"""


def generate_quality_gate(skill_type: str) -> str:
    """Generate Quality Gate section."""

    base = """
## Quality Gate

Before delivering the final output, verify:

"""

    if skill_type in ("scraping", "monitoring"):
        return base + """- [ ] **Data completeness:** At least 1 source returned results. If all sources failed, the output must explain why
- [ ] **No silent failures:** Every source that was attempted has a status (success/partial/failed) in the output
- [ ] **Deduplication applied:** No duplicate entries in the final dataset
- [ ] **Output format valid:** CSV/JSON is well-formed and parseable
- [ ] **User checkpoint:** Present summary to user before proceeding to downstream skills

**If any check fails:** Stop, report the failure, and ask the user how to proceed.
"""

    elif skill_type in ("outreach", "lead-generation"):
        return base + """- [ ] **Lead quality:** All leads have at minimum: name, company, and one contact method (email or LinkedIn URL)
- [ ] **Personalization check:** At least 1 personalized element per message beyond [First Name]
- [ ] **Duplicate check:** Cross-reference against contact-cache to avoid re-contacting
- [ ] **Volume sanity:** If generating >50 contacts, present a sample of 5 for user approval before proceeding
- [ ] **User checkpoint:** Present the lead list and draft messages for review before any outreach execution

**If any check fails:** Flag the specific leads/messages that failed and ask user to review.
"""

    elif skill_type in ("research", "competitive-intel", "seo"):
        return base + """- [ ] **Source diversity:** Findings are supported by at least 2 independent sources
- [ ] **Recency check:** Key data points are from the last 12 months (or explicitly flagged as older)
- [ ] **Confidence labeling:** Every finding has a confidence level (high/medium/low)
- [ ] **Actionability:** Report includes at least 1 concrete next step or recommendation
- [ ] **User checkpoint:** Present key findings summary before generating the full report

**If any check fails:** Note the gap explicitly in the output rather than omitting it.
"""

    elif skill_type in ("content", "design"):
        return base + """- [ ] **Brand consistency:** Colors, fonts, and tone match the brand config (or defaults)
- [ ] **Format compliance:** Output meets platform specs (e.g., 1080×1080 for LinkedIn carousel)
- [ ] **Content density:** No slide/section exceeds readability limits
- [ ] **Link integrity:** All URLs in the output are valid and accessible
- [ ] **User checkpoint:** Present preview to user for approval before final export

**If any check fails:** Generate a corrected version and present both options to the user.
"""

    else:
        return base + """- [ ] **Output completeness:** All required fields/sections are populated
- [ ] **No silent failures:** Every step that was attempted has a status in the output
- [ ] **Format valid:** Output matches the documented schema
- [ ] **User checkpoint:** Present results summary to user before finalizing

**If any check fails:** Report the specific gap and ask user how to proceed.
"""


def process_skill(skill_path: Path, dry_run: bool = False) -> dict:
    """Process a single SKILL.md file, adding missing cross-cutting patterns."""
    content = read_skill(skill_path)
    skill_name = get_skill_name(skill_path)
    tags = get_tags(content)
    skill_type = detect_skill_type(content, tags)
    uses_tools = uses_external_tools(content)

    changes = {
        "skill": skill_name,
        "tags": tags,
        "type": skill_type,
        "added": [],
        "skipped": [],
    }

    additions = []

    # 1. Error Handling
    if has_any_error_section(content):
        changes["skipped"].append("error_handling (already exists)")
    elif uses_tools or skill_type in ("scraping", "outreach", "monitoring"):
        section = generate_error_handling(skill_type, skill_name)
        additions.append(section)
        changes["added"].append("error_handling")
    else:
        changes["skipped"].append("error_handling (no external tools)")

    # 2. Composability
    if has_composability_section(content):
        changes["skipped"].append("composability (already exists)")
    else:
        section = generate_composability(tags, skill_name)
        if section:
            additions.append(section)
            changes["added"].append("composability")
        else:
            changes["skipped"].append("composability (no chain mappings)")

    # 3. Memory Hooks
    if has_memory_hooks(content):
        changes["skipped"].append("memory_hooks (already exists)")
    else:
        section = generate_memory_hooks(skill_name)
        additions.append(section)
        changes["added"].append("memory_hooks")

    # 4. Quality Gate
    if has_quality_gate(content):
        changes["skipped"].append("quality_gate (already exists)")
    else:
        section = generate_quality_gate(skill_type)
        additions.append(section)
        changes["added"].append("quality_gate")

    if additions and not dry_run:
        # Append all sections at the end of the file
        new_content = content.rstrip() + "\n" + "\n".join(additions) + "\n"
        skill_path.write_text(new_content, encoding="utf-8")

    return changes


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    if dry_run:
        print("🔍 DRY RUN — no files will be modified\n")

    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    # Exclude node_modules
    skill_files = [f for f in skill_files if "node_modules" not in str(f)]

    stats = {
        "total": len(skill_files),
        "error_handling_added": 0,
        "composability_added": 0,
        "memory_hooks_added": 0,
        "quality_gate_added": 0,
        "skills_modified": 0,
    }

    results = []

    for skill_path in skill_files:
        changes = process_skill(skill_path, dry_run=dry_run)
        results.append(changes)

        if changes["added"]:
            stats["skills_modified"] += 1
            for item in changes["added"]:
                stats[f"{item}_added"] += 1

        if verbose:
            status = "✅" if changes["added"] else "⏭️"
            added_str = ", ".join(changes["added"]) if changes["added"] else "none"
            print(f"  {status} {changes['skill']}: +{added_str}")

    # Print summary
    print(f"\n{'='*60}")
    print(f"PHASE 2 SUMMARY {'(DRY RUN)' if dry_run else ''}")
    print(f"{'='*60}")
    print(f"Total skills processed:    {stats['total']}")
    print(f"Skills modified:           {stats['skills_modified']}")
    print(f"Error Handling added:      {stats['error_handling_added']}")
    print(f"Composability added:       {stats['composability_added']}")
    print(f"Memory Hooks added:        {stats['memory_hooks_added']}")
    print(f"Quality Gates added:       {stats['quality_gate_added']}")
    print(f"{'='*60}")

    # Write results JSON for review
    output_path = Path(__file__).parent / "phase2_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nDetailed results: {output_path}")


if __name__ == "__main__":
    main()
