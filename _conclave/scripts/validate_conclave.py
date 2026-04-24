#!/usr/bin/env python3
"""
Conclave Integrity Validator
Run from the Conclave project root: python3 _conclave/scripts/validate_conclave.py
"""

import os
import sys
import json
import re
from pathlib import Path

G = "\033[92m"; R = "\033[91m"; Y = "\033[93m"; C = "\033[96m"; B = "\033[1m"; X = "\033[0m"

# System agents that use a slim schema — exempt from full content-agent checks.
# Documented in build.prompt.md: "Safe Zone" agents and the Architect exception.
SYSTEM_AGENT_IDS = {"pietro-prompt", "arquiteto", "architect"}

class Result:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warned = 0
        self.errors = []

    def ok(self, msg):
        print(f"  {G}✓{X} {msg}")
        self.passed += 1

    def fail(self, msg):
        print(f"  {R}✗{X} {msg}")
        self.failed += 1
        self.errors.append(msg)

    def warn(self, msg):
        print(f"  {Y}⚠{X} {msg}")
        self.warned += 1

    def check(self, cond, ok_msg, fail_msg, blocking=True):
        if cond:
            self.ok(ok_msg)
        elif blocking:
            self.fail(fail_msg)
        else:
            self.warn(fail_msg)
        return cond


# ── YAML / file helpers ────────────────────────────────────────────────────────

def get_scalar(content, key):
    """Extract a top-level scalar from simple YAML."""
    m = re.search(rf'^{re.escape(key)}\s*:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else None

def get_list(content, key):
    """Extract a YAML list under `key:` (any indent level)."""
    pattern = rf'(?m)^\s*{re.escape(key)}\s*:\s*\n((?:\s+-\s*.+\n?)*)'
    m = re.search(pattern, content)
    if not m:
        return []
    return [re.sub(r'^\s*-\s*', '', l).strip().strip('"').strip("'")
            for l in m.group(1).splitlines() if l.strip().startswith('-')]

def get_nested_list(content, parent_key, child_key):
    """Extract a list nested under parent_key > child_key."""
    parent_m = re.search(rf'(?m)^{re.escape(parent_key)}\s*:\s*\n((?:[ \t]+.+\n?)*)', content)
    if not parent_m:
        return []
    block = parent_m.group(1)
    return get_list(block, child_key)

def frontmatter(content):
    """Return raw frontmatter string (between --- delimiters), or empty string."""
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    return m.group(1) if m else ""

def fm_field(content, key):
    return get_scalar(frontmatter(content), key)

def fm_list(content, key):
    return get_list(frontmatter(content), key)

def agent_folder_name(agent_path: Path) -> str:
    """Convert 'wade-web.agent.md' → 'wade-web' (strip .agent.md suffix)."""
    name = agent_path.name
    if name.endswith('.agent.md'):
        return name[:-len('.agent.md')]
    return agent_path.stem

def has_section(content, section):
    return bool(re.search(rf'^## {re.escape(section)}\b', content, re.MULTILINE))

def line_count(path):
    try:
        return len(path.read_text(encoding='utf-8', errors='ignore').splitlines())
    except Exception:
        return 0


# ── CSV parser (handles both column orderings) ────────────────────────────────

def parse_squad_csv(csv_path: Path):
    """
    Parse squad-party.csv. Handles two formats:
    Format A (original): path,name,icon,title
    Format B (newer):    id,name,title,icon,execution,path
    Returns list of (agent_display_name, agent_file_path).
    """
    try:
        content = csv_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.splitlines()
    except Exception:
        return []
    if not lines:
        return []

    agents = []
    header = lines[0].strip().lower()

    # Detect Format B by checking if the first line looks like a header
    # Format B headers usually contain 'id', 'path', 'name', or 'displayname'
    # but we must be careful not to mistake a Format A line (path starting with ./agents/...) as a header.
    is_format_b = False
    if ',' in header:
        cols = [c.strip() for c in header.split(',')]
        if any(c in ('id', 'path', 'name', 'displayname', 'display_name', 'role', 'title') for c in cols):
            is_format_b = True

    if is_format_b:
        # Format B — has a header row; find column indices
        cols = [c.strip().lower() for c in lines[0].split(',')]
        path_idx = next((i for i, c in enumerate(cols) if c == 'path'), None)
        name_idx = next((i for i, c in enumerate(cols) if c in ('name', 'displayname', 'display_name')), None)
        id_idx = next((i for i, c in enumerate(cols) if c == 'id'), None)

        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(',')]
            
            # Extract path
            rel = parts[path_idx] if path_idx is not None and path_idx < len(parts) else None
            if rel and rel.startswith('./'):
                rel = rel[2:]
            
            # Extract name with fallbacks
            name = "agent"
            if name_idx is not None and name_idx < len(parts) and parts[name_idx]:
                name = parts[name_idx]
            elif id_idx is not None and id_idx < len(parts) and parts[id_idx]:
                name = parts[id_idx]
            
            if rel:
                agents.append((name, csv_path.parent / rel))
    else:
        # Format A — no header; first column is path
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',', 3)
            if len(parts) < 2:
                continue
            rel = parts[0].strip()
            if rel.startswith('./'):
                rel = rel[2:]
            name = parts[1].strip()
            agents.append((name, csv_path.parent / rel))

    return agents


# ── CHECK GROUPS ───────────────────────────────────────────────────────────────

def check_core(root, r):
    print(f"\n{B}{C}── CORE RUNTIME ──────────────────────────────────────{X}")

    required = [
        "_conclave/core/architect.agent.yaml",
        "_conclave/core/prompts/discovery.prompt.md",
        "_conclave/core/prompts/design.prompt.md",
        "_conclave/core/prompts/build.prompt.md",
        "_conclave/core/skill/SKILL.md",
        "_conclave/core/runner.pipeline.md",
        "_conclave/core/skills.engine.md",
        "_conclave/core/security.policy.md",
        "_conclave/core/router.agent.md",
        "_conclave/core/intention_matrix.json",
        "_conclave/core/best-practices/_catalog.yaml",
        "_conclave/_memory/company.md",
        "_conclave/_memory/preferences.md",
    ]
    for rel in required:
        p = root / rel
        r.check(p.exists(), rel, f"MISSING: {rel}")

    # best-practices catalog consistency
    catalog = root / "_conclave/core/best-practices/_catalog.yaml"
    if catalog.exists():
        content = catalog.read_text(encoding='utf-8', errors='ignore')
        bp_files = re.findall(r'file:\s*["\']?(\S+\.md)["\']?', content)
        for fname in bp_files:
            p = root / "_conclave/core/best-practices" / fname
            r.check(p.exists(), f"best-practices/{fname}", f"MISSING best-practice: {fname}")

    for script in ["reindex_squads.py", "validate_conclave.py"]:
        p = root / "_conclave/scripts" / script
        r.check(p.exists(), f"scripts/{script}", f"MISSING script: {script}")

    matrix = root / "_conclave/core/intention_matrix.json"
    if matrix.exists():
        try:
            json.loads(matrix.read_text())
            r.ok("intention_matrix.json is valid JSON")
        except json.JSONDecodeError as e:
            r.fail(f"intention_matrix.json invalid JSON: {e}")


def check_agent(agent_path: Path, r: Result, agent_name: str):
    content = agent_path.read_text(encoding='utf-8', errors='ignore')
    agent_id = fm_field(content, 'id') or ""
    folder = agent_folder_name(agent_path)
    is_system = folder in SYSTEM_AGENT_IDS or any(s in agent_id for s in SYSTEM_AGENT_IDS)

    tasks = fm_list(content, 'tasks')
    has_tasks = len(tasks) > 0

    if is_system:
        # System agents (Pietro, Arquiteto) — only check basic structure
        r.check(has_section(content, "Persona") or "## Identidade" in content or "# " in content,
                f"{agent_name}: has body content (system agent)",
                f"{agent_name}: appears empty or missing content (system agent)")
        # System agents skip name validation and full section checks
        if has_tasks:
            _check_task_files(agent_path, tasks, r, agent_name)
        return

    if has_tasks:
        min_lines = 80
        required_sections = ["Persona", "Principles", "Voice Guidance", "Anti-Patterns", "Quality Criteria", "Integration"]
        forbidden = ["Operational Framework", "Output Examples"]
        for s in forbidden:
            if has_section(content, s):
                r.warn(f"{agent_name}: has '## {s}' but also has tasks: (should move to task files)")
    else:
        min_lines = 100
        required_sections = ["Persona", "Principles", "Operational Framework", "Voice Guidance",
                              "Output Examples", "Anti-Patterns", "Quality Criteria", "Integration"]

    for section in required_sections:
        r.check(has_section(content, section),
                f"{agent_name}: ## {section}",
                f"{agent_name}: MISSING ## {section}")

    for sub in ["### Role", "### Identity", "### Communication Style"]:
        r.check(sub in content, f"{agent_name}: {sub}", f"{agent_name}: MISSING {sub}")

    r.check(line_count(agent_path) >= min_lines,
            f"{agent_name}: ≥{min_lines} lines ({line_count(agent_path)})",
            f"{agent_name}: too short ({line_count(agent_path)} < {min_lines} lines)", blocking=False)

    name = fm_field(content, 'name')
    if name:
        r.check(len(name.split()) >= 2,
                f"{agent_name}: name '{name}' has 2 words",
                f"{agent_name}: name '{name}' missing LastName (must be 2 words)")

    if has_tasks:
        _check_task_files(agent_path, tasks, r, agent_name)


def _check_task_files(agent_path: Path, tasks: list, r: Result, agent_name: str):
    folder = agent_folder_name(agent_path)
    tasks_dir = agent_path.parent / folder
    for task_rel in tasks:
        task_path = tasks_dir / task_rel
        r.check(task_path.exists(),
                f"{agent_name}/{task_rel}",
                f"{agent_name}: MISSING task file: {task_rel}")
        if task_path.exists():
            _check_task_content(task_path, r, f"{agent_name}/{task_rel}")


def _check_task_content(task_path: Path, r: Result, label: str):
    content = task_path.read_text(encoding='utf-8', errors='ignore')
    r.check(bool(re.match(r'^---\n', content)), f"{label}: frontmatter", f"{label}: MISSING frontmatter")

    for field in ['task', 'order']:
        r.check(bool(fm_field(content, field)), f"{label}: frontmatter.{field}", f"{label}: MISSING frontmatter.{field}")

    for section in ["Process", "Output Format", "Output Example", "Quality Criteria", "Veto Conditions"]:
        r.check(has_section(content, section), f"{label}: ## {section}", f"{label}: MISSING ## {section}")

    r.check(line_count(task_path) >= 50,
            f"{label}: ≥50 lines ({line_count(task_path)})",
            f"{label}: too short ({line_count(task_path)} < 50 lines)", blocking=False)


def check_step(step_path: Path, r: Result, label: str):
    content = step_path.read_text(encoding='utf-8', errors='ignore')

    fm = frontmatter(content)
    if re.search(r'type:\s*checkpoint', fm):
        r.ok(f"{label}: checkpoint (section checks skipped)")
        return

    for section in ["Context Loading", "Instructions", "Output Format", "Veto Conditions", "Quality Criteria"]:
        r.check(has_section(content, section), f"{label}: ## {section}", f"{label}: MISSING ## {section}")

    r.check(has_section(content, "Output Example"),
            f"{label}: ## Output Example",
            f"{label}: MISSING ## Output Example", blocking=False)

    r.check(line_count(step_path) >= 60,
            f"{label}: ≥60 lines ({line_count(step_path)})",
            f"{label}: too short ({line_count(step_path)} < 60 lines)", blocking=False)


def check_squad(squad_dir: Path, skills_dir: Path, r: Result):
    name = squad_dir.name
    print(f"\n{B}{C}── SQUAD: {name} ─────────────────────────────────────{X}")

    yaml_path = squad_dir / "squad.yaml"
    if not r.check(yaml_path.exists(), "squad.yaml exists", f"{name}: MISSING squad.yaml"):
        return

    content = yaml_path.read_text(encoding='utf-8', errors='ignore')
    for field in ["name", "code", "description", "icon"]:
        r.check(bool(get_scalar(content, field)), f"squad.yaml: {field}", f"{name}: MISSING squad.yaml field '{field}'")

    csv_path = squad_dir / "squad-party.csv"
    if not r.check(csv_path.exists(), "squad-party.csv exists", f"{name}: MISSING squad-party.csv"):
        return

    agents = parse_squad_csv(csv_path)
    if not agents:
        r.warn(f"{name}: squad-party.csv has no parseable agents")
    for agent_name, agent_path in agents:
        rel = agent_path.relative_to(squad_dir) if agent_path.is_relative_to(squad_dir) else agent_path
        r.check(agent_path.exists(), f"agent: {rel}", f"{name}: MISSING agent file: {rel}")
        if agent_path.exists():
            check_agent(agent_path, r, agent_name)

    # pipeline steps
    steps_dir = squad_dir / "pipeline" / "steps"
    pipeline_steps = get_nested_list(content, "pipeline", "steps") or get_list(content, "steps")

    if not pipeline_steps:
        r.warn(f"{name}: could not parse pipeline.steps from squad.yaml")
    else:
        r.ok(f"pipeline: {len(pipeline_steps)} steps declared")
        first = pipeline_steps[0]
        r.check(first.startswith("step-00"),
                f"pipeline starts with step-00-* ('{first}')",
                f"{name}: first step is '{first}', expected step-00-* (Safe Zone squads exempt)", blocking=False)
        for step_file in pipeline_steps:
            step_path = steps_dir / step_file
            r.check(step_path.exists(), f"step: {step_file}", f"{name}: MISSING step file: {step_file}")
            if step_path.exists():
                check_step(step_path, r, f"{name}/{step_file}")

    for df in get_list(content, "data"):
        p = squad_dir / df
        r.check(p.exists(), f"data: {df}", f"{name}: MISSING data file: {df}")

    for skill in get_list(content, "skills"):
        if skill in ("web_search", "web_fetch"):
            r.ok(f"skill: {skill} (native)")
            continue
        r.check((skills_dir / skill).exists(),
                f"skill: {skill} installed",
                f"{name}: skill '{skill}' listed but NOT installed in skills/", blocking=False)

    memories = squad_dir / "_memory" / "memories.md"
    r.check(memories.exists(), "_memory/memories.md exists",
            f"{name}: MISSING _memory/memories.md", blocking=False)


# ── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    root = Path.cwd()
    if not (root / "_conclave").exists():
        print(f"{R}ERROR:{X} Run from the Conclave project root (directory containing _conclave/).")
        sys.exit(1)

    print(f"\n{B}Conclave Integrity Validator{X}")
    print(f"Root: {root}\n")

    r = Result()
    check_core(root, r)

    squads_dir = root / "squads"
    skills_dir = root / "skills"
    if squads_dir.exists():
        squads = sorted(d for d in squads_dir.iterdir() if d.is_dir())
        for squad_dir in squads:
            check_squad(squad_dir, skills_dir, r)
    else:
        r.fail("squads/ directory not found")

    print(f"\n{B}{'─'*54}{X}")
    print(f"{B}RESULT:{X}  {G}{r.passed} passed{X}  |  {R}{r.failed} failed{X}  |  {Y}{r.warned} warnings{X}")
    print(f"{'─'*54}")

    if r.errors:
        print(f"\n{R}Blocking failures:{X}")
        for e in r.errors:
            print(f"  {R}✗{X} {e}")

    if r.failed > 0:
        print(f"\n{R}Status: FAIL — fix blocking issues before updating core files.{X}\n")
        sys.exit(1)
    else:
        print(f"\n{G}Status: PASS — system is intact.{X}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
