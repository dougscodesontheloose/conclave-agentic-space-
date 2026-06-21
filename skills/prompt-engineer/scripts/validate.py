#!/usr/bin/env python3
"""
Validate prompt-engineer skill directory structure and constraints.
Run: python3 scripts/validate.py
"""

import json
import os
import re
import sys
from pathlib import Path

# --- Constants ---
MAX_SKILL_LINES = 500
MAX_DESCRIPTION_CHARS = 1024
MAX_NAME_CHARS = 64
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_FILE = SKILL_DIR / "SKILL.md"
EVALS_FILE = SKILL_DIR / "evals" / "evals.json"
REFERENCES_DIR = SKILL_DIR / "references"

errors = []
warnings = []


def check_skill_exists():
    if not SKILL_FILE.exists():
        errors.append(f"SKILL.md not found at {SKILL_FILE}")
        return False
    return True


def check_line_count():
    lines = SKILL_FILE.read_text().splitlines()
    count = len(lines)
    if count > MAX_SKILL_LINES:
        errors.append(f"SKILL.md has {count} lines (max: {MAX_SKILL_LINES})")
    else:
        print(f"  ✓ Line count: {count}/{MAX_SKILL_LINES}")


def check_frontmatter():
    content = SKILL_FILE.read_text()
    if not content.startswith("---"):
        errors.append("SKILL.md missing frontmatter (must start with ---)")
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter not properly closed")
        return

    frontmatter = parts[1]

    # Check name
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip()
        if len(name) > MAX_NAME_CHARS:
            errors.append(f"name '{name}' exceeds {MAX_NAME_CHARS} chars ({len(name)})")
        if not NAME_PATTERN.match(name):
            errors.append(f"name '{name}' must be lowercase-hyphenated")
        print(f"  ✓ Name: '{name}' ({len(name)} chars)")
    else:
        errors.append("Frontmatter missing 'name' field")

    # Check description
    desc_match = re.search(
        r"^description:\s*>?\s*\n((?:\s+.+\n)*)", frontmatter, re.MULTILINE
    )
    if desc_match:
        desc = desc_match.group(1).strip()
        desc_len = len(desc)
        if desc_len > MAX_DESCRIPTION_CHARS:
            errors.append(
                f"description exceeds {MAX_DESCRIPTION_CHARS} chars ({desc_len})"
            )
        print(f"  ✓ Description: {desc_len}/{MAX_DESCRIPTION_CHARS} chars")
    else:
        # Try single-line description
        desc_match_single = re.search(
            r'^description:\s*"?([^"\n]+)"?\s*$', frontmatter, re.MULTILINE
        )
        if desc_match_single:
            desc = desc_match_single.group(1).strip()
            print(f"  ✓ Description: {len(desc)}/{MAX_DESCRIPTION_CHARS} chars")
        else:
            errors.append("Frontmatter missing 'description' field")


def check_references():
    content = SKILL_FILE.read_text()
    ref_pattern = re.compile(r"references/([^\s\)]+\.md)")
    referenced = set(ref_pattern.findall(content))

    if not REFERENCES_DIR.exists():
        if referenced:
            errors.append(
                f"references/ dir missing but SKILL.md references: {referenced}"
            )
        return

    existing = {f.name for f in REFERENCES_DIR.glob("*.md")}

    missing = referenced - existing
    orphaned = existing - referenced

    for m in missing:
        errors.append(f"Referenced file missing: references/{m}")
    for o in orphaned:
        warnings.append(f"Orphaned reference (not linked from SKILL.md): references/{o}")

    if not missing:
        print(f"  ✓ All {len(referenced)} referenced files exist")


def check_evals():
    if not EVALS_FILE.exists():
        errors.append(f"evals/evals.json not found at {EVALS_FILE}")
        return

    try:
        evals = json.loads(EVALS_FILE.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"evals.json is invalid JSON: {e}")
        return

    should_trigger = [e for e in evals if e.get("should_trigger")]
    should_not = [e for e in evals if not e.get("should_trigger")]

    print(f"  ✓ Evals: {len(should_trigger)} trigger / {len(should_not)} no-trigger")

    if len(should_trigger) < 8:
        warnings.append(
            f"Only {len(should_trigger)} should-trigger evals (recommended: 8+)"
        )
    if len(should_not) < 8:
        warnings.append(
            f"Only {len(should_not)} should-NOT-trigger evals (recommended: 8+)"
        )


def main():
    print("=" * 50)
    print("SKILL VALIDATION: prompt-engineer")
    print("=" * 50)

    if not check_skill_exists():
        print("\n❌ FATAL: SKILL.md not found. Aborting.")
        sys.exit(1)

    check_line_count()
    check_frontmatter()
    check_references()
    check_evals()

    print()
    if warnings:
        print(f"⚠  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"   - {w}")

    if errors:
        print(f"\n❌ {len(errors)} error(s):")
        for e in errors:
            print(f"   - {e}")
        sys.exit(1)
    else:
        print("✅ All checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
