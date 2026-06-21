#!/usr/bin/env python3
"""
breadcrumb.py — Conclave Observer Protocol (COP)

Passive breadcrumb tracker for Conclave sessions. Drops lightweight signals
during any work session (not just formal /conclave run), and harvests them
into the existing memory streams at session end.

Usage:
  python3 breadcrumb.py drop --type {type} --value "{text}" [--squad "{name}"] [--quality "{quality}"]
  python3 breadcrumb.py harvest
  python3 breadcrumb.py status

Signal types: action, creation, squad_work, architecture, feedback, session_start, session_end
Quality:      pending, good, partial, miss
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict

# ── paths ────────────────────────────────────────────────────────────────────

ROOT_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SCRATCH_DIR = ROOT_DIR / "_conclave" / "runtime" / "scratch"
BREADCRUMBS_FILE = SCRATCH_DIR / "session-breadcrumbs.jsonl"
BREADCRUMBS_ARCHIVE = SCRATCH_DIR / "session-breadcrumbs-archive.jsonl"

MEMORY_DIR = ROOT_DIR / "_conclave" / "state" / "memory"
SESSION_LOG = MEMORY_DIR / "session-log.jsonl"
SQUADS_DIR = ROOT_DIR / "squads"

# Colors
G = "\033[92m"; R = "\033[91m"; Y = "\033[93m"; C = "\033[96m"; B = "\033[1m"; X = "\033[0m"

VALID_TYPES = {"action", "creation", "squad_work", "architecture", "feedback", "session_start", "session_end"}
VALID_QUALITIES = {"pending", "good", "partial", "miss"}


# ── drop ─────────────────────────────────────────────────────────────────────

def drop(signal_type: str, value: str, squad: str = "none", quality: str = "pending"):
    """Append a single breadcrumb to the session file."""
    if signal_type not in VALID_TYPES:
        print(f"{R}Error:{X} Invalid type '{signal_type}'. Valid: {', '.join(sorted(VALID_TYPES))}")
        sys.exit(1)

    if quality not in VALID_QUALITIES:
        print(f"{R}Error:{X} Invalid quality '{quality}'. Valid: {', '.join(sorted(VALID_QUALITIES))}")
        sys.exit(1)

    # Enforce 80-char max on value
    value = value[:80].strip()

    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

    entry = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "session_id": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "type": signal_type,
        "value": value,
        "squad": squad if squad else "none",
        "quality": quality,
    }

    with open(BREADCRUMBS_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── harvest ──────────────────────────────────────────────────────────────────

def harvest():
    """
    Process accumulated breadcrumbs and feed them into the existing
    Conclave memory streams (squad-signals, implicit-signals, session-log).
    """
    if not BREADCRUMBS_FILE.exists() or BREADCRUMBS_FILE.stat().st_size == 0:
        print(f"{G}No breadcrumbs to harvest.{X}")
        return

    # Read all breadcrumbs
    breadcrumbs = []
    with open(BREADCRUMBS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                breadcrumbs.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not breadcrumbs:
        print(f"{G}No valid breadcrumbs found.{X}")
        return

    # Filter out session_start/session_end markers (they're structural, not data)
    work_crumbs = [b for b in breadcrumbs if b.get("type") not in ("session_start", "session_end")]

    if not work_crumbs:
        print(f"{G}No work breadcrumbs to harvest (only session markers).{X}")
        _archive_breadcrumbs(breadcrumbs)
        return

    # ── Group by squad ──
    squad_crumbs = defaultdict(list)
    global_crumbs = []

    for b in work_crumbs:
        squad = b.get("squad", "none")
        if squad and squad != "none":
            squad_crumbs[squad].append(b)
        else:
            global_crumbs.append(b)

    stats = {"squads_fed": 0, "signals_emitted": 0, "session_entries": 0}

    # ── Feed squad-level streams ──
    for squad_name, crumbs in squad_crumbs.items():
        squad_memory_dir = SQUADS_DIR / squad_name / "_memory"
        if not squad_memory_dir.exists():
            squad_memory_dir.mkdir(parents=True, exist_ok=True)

        # Determine overall quality for this squad's session work
        qualities = [c.get("quality", "pending") for c in crumbs]
        confirmed_qualities = [q for q in qualities if q != "pending"]

        if confirmed_qualities:
            # Use the most common confirmed quality
            quality_counts = defaultdict(int)
            for q in confirmed_qualities:
                quality_counts[q] += 1
            session_quality = max(quality_counts, key=quality_counts.get)
        else:
            # All pending — can't emit a quality signal yet
            session_quality = None

        # Emit squad-signal if quality is confirmed
        if session_quality:
            squad_signals_file = squad_memory_dir / "squad-signals.jsonl"

            # Try to read domain from squad.yaml
            domain = _get_squad_domain(squad_name)

            signal = {
                "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "squad": squad_name,
                "run_id": f"session-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
                "domain": domain,
                "delivered": session_quality in ("good", "partial"),
                "quality": session_quality,
                "source": "cop_harvest",
            }

            with open(squad_signals_file, "a") as f:
                f.write(json.dumps(signal, ensure_ascii=False) + "\n")

            stats["signals_emitted"] += 1

        # Extract implicit signals from the work crumbs
        implicit_signals = _extract_implicit_signals(squad_name, crumbs, session_quality)
        if implicit_signals:
            implicit_file = squad_memory_dir / "implicit-signals.jsonl"
            with open(implicit_file, "a") as f:
                for sig in implicit_signals:
                    f.write(json.dumps(sig, ensure_ascii=False) + "\n")
            stats["signals_emitted"] += len(implicit_signals)

        stats["squads_fed"] += 1

    # ── Feed global session-log ──
    all_crumbs = work_crumbs
    session_topics = [c["value"] for c in all_crumbs if c.get("value")]
    if session_topics:
        # Build a session summary
        topic_summary = "; ".join(session_topics[:5])  # Max 5 topics
        if len(session_topics) > 5:
            topic_summary += f" (+{len(session_topics) - 5} more)"

        # Determine squads involved
        squads_involved = list(squad_crumbs.keys())

        session_entry = {
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event": "session.harvested",
            "source": "cop_harvest",
            "breadcrumbs_total": len(work_crumbs),
            "squads_involved": squads_involved,
            "topic_summary": topic_summary[:200],
            "types": list(set(c.get("type", "") for c in work_crumbs)),
        }

        MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        with open(SESSION_LOG, "a") as f:
            f.write(json.dumps(session_entry, ensure_ascii=False) + "\n")

        stats["session_entries"] += 1

    # ── Archive processed breadcrumbs ──
    _archive_breadcrumbs(breadcrumbs)

    # ── Check D6 threshold ──
    d6_msg = _check_d6_threshold()

    # ── Report ──
    print(f"{G}Harvest complete:{X}")
    print(f"  Breadcrumbs processed: {len(work_crumbs)}")
    print(f"  Squads fed: {stats['squads_fed']}")
    print(f"  Signals emitted: {stats['signals_emitted']}")
    print(f"  Session log entries: {stats['session_entries']}")
    if d6_msg:
        print(f"\n  {d6_msg}")


def _get_squad_domain(squad_name: str) -> str:
    """Read the domain field from a squad's squad.yaml."""
    squad_yaml = SQUADS_DIR / squad_name / "squad.yaml"
    if not squad_yaml.exists():
        return ""
    try:
        with open(squad_yaml, "r") as f:
            for line in f:
                if line.strip().startswith("domain:"):
                    return line.split(":", 1)[1].strip().strip('"').strip("'")
    except Exception:
        pass
    return ""


def _extract_implicit_signals(squad_name: str, crumbs: list, quality: str | None) -> list:
    """
    Extract implicit signals from breadcrumbs.
    Maps breadcrumb types to signal_type categories.
    """
    signals = []
    domain = _get_squad_domain(squad_name)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Deduplicate by value to avoid redundant signals
    seen_values = set()

    for crumb in crumbs:
        value = crumb.get("value", "").strip()
        if not value or value in seen_values:
            continue
        seen_values.add(value)

        crumb_type = crumb.get("type", "action")

        # Map breadcrumb type to implicit signal type
        if crumb_type == "creation":
            signal_type = "format"
        elif crumb_type == "architecture":
            signal_type = "topic"
        elif crumb_type == "feedback":
            signal_type = "tone"
        else:
            signal_type = "topic"

        signals.append({
            "ts": ts,
            "squad": squad_name,
            "run_id": f"session-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
            "domain": domain,
            "quality": quality or "pending",
            "signal_type": signal_type,
            "value": value[:80],
            "source": "cop_breadcrumb",
        })

        # Cap at 5 signals per squad per harvest
        if len(signals) >= 5:
            break

    return signals


def _archive_breadcrumbs(breadcrumbs: list):
    """Move processed breadcrumbs to archive and clear the active file."""
    with open(BREADCRUMBS_ARCHIVE, "a") as f:
        for b in breadcrumbs:
            f.write(json.dumps(b, ensure_ascii=False) + "\n")

    # Clear active file
    with open(BREADCRUMBS_FILE, "w") as f:
        pass  # Truncate


def _check_d6_threshold() -> str | None:
    """
    Check if enough cross-squad data has accumulated to trigger
    User Model Inference (D6). Returns a message if threshold met.
    """
    total_signals = 0

    if not SQUADS_DIR.exists():
        return None

    for squad_dir in SQUADS_DIR.iterdir():
        if not squad_dir.is_dir():
            continue
        signals_file = squad_dir / "_memory" / "squad-signals.jsonl"
        if signals_file.exists():
            with open(signals_file, "r") as f:
                total_signals += sum(1 for line in f if line.strip())

    if total_signals > 0 and total_signals % 3 == 0:
        return f"🌊 D6 threshold atingido ({total_signals} signals cross-squad). Execute /conclave tide para atualizar o user-model."

    return None


# ── status ───────────────────────────────────────────────────────────────────

def status():
    """Show current breadcrumb status."""
    print(f"\n{B}=== CONCLAVE OBSERVER PROTOCOL (COP) — STATUS ==={X}")

    # Active breadcrumbs
    if BREADCRUMBS_FILE.exists() and BREADCRUMBS_FILE.stat().st_size > 0:
        with open(BREADCRUMBS_FILE, "r") as f:
            lines = [l for l in f if l.strip()]
        print(f"  Active breadcrumbs: {len(lines)}")

        # Show types breakdown
        types = defaultdict(int)
        for line in lines:
            try:
                data = json.loads(line)
                types[data.get("type", "unknown")] += 1
            except Exception:
                pass
        for t, count in sorted(types.items()):
            print(f"    {t}: {count}")
    else:
        print(f"  Active breadcrumbs: 0")

    # Archive stats
    if BREADCRUMBS_ARCHIVE.exists() and BREADCRUMBS_ARCHIVE.stat().st_size > 0:
        with open(BREADCRUMBS_ARCHIVE, "r") as f:
            archive_lines = sum(1 for l in f if l.strip())
        print(f"  Archived breadcrumbs: {archive_lines}")
    else:
        print(f"  Archived breadcrumbs: 0")

    # Squad signal coverage
    print(f"\n  {B}Squad signal coverage:{X}")
    if SQUADS_DIR.exists():
        for squad_dir in sorted(SQUADS_DIR.iterdir()):
            if not squad_dir.is_dir():
                continue
            name = squad_dir.name
            signals = squad_dir / "_memory" / "squad-signals.jsonl"
            implicit = squad_dir / "_memory" / "implicit-signals.jsonl"

            sig_count = 0
            imp_count = 0
            if signals.exists():
                with open(signals, "r") as f:
                    sig_count = sum(1 for l in f if l.strip())
            if implicit.exists():
                with open(implicit, "r") as f:
                    imp_count = sum(1 for l in f if l.strip())

            status_icon = f"{G}✓{X}" if sig_count > 0 else f"{Y}○{X}"
            print(f"    {status_icon} {name}: {sig_count} signals, {imp_count} implicit")

    print()


# ── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conclave Observer Protocol — Breadcrumb Tracker")
    sub = parser.add_subparsers(dest="action")

    # drop
    p_drop = sub.add_parser("drop", help="Drop a breadcrumb")
    p_drop.add_argument("--type", required=True, help=f"Signal type: {', '.join(sorted(VALID_TYPES))}")
    p_drop.add_argument("--value", required=True, help="Description (max 80 chars)")
    p_drop.add_argument("--squad", default="none", help="Squad name or 'none'")
    p_drop.add_argument("--quality", default="pending", help=f"Quality: {', '.join(sorted(VALID_QUALITIES))}")

    # harvest
    sub.add_parser("harvest", help="Harvest breadcrumbs into memory streams")

    # status
    sub.add_parser("status", help="Show breadcrumb status")

    args = parser.parse_args()
    if not args.action:
        parser.print_help()
        sys.exit(0)

    if args.action == "drop":
        drop(
            signal_type=args.type,
            value=args.value,
            squad=args.squad,
            quality=args.quality,
        )
    elif args.action == "harvest":
        harvest()
    elif args.action == "status":
        status()
