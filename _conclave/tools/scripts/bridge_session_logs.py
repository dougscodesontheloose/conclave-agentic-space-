#!/usr/bin/env python3
"""
bridge_session_logs.py — One-shot bootstrap script

Parses the existing session_logs.md (7 rich human-written sessions)
and generates corresponding machine-readable entries in session-log.jsonl,
bootstrapping the JSONL stream with historical data.

Run once: python3 _conclave/tools/scripts/bridge_session_logs.py
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SESSION_LOGS_MD = ROOT_DIR / "_conclave" / "state" / "memory" / "session_logs.md"
SESSION_LOG_JSONL = ROOT_DIR / "_conclave" / "state" / "memory" / "session-log.jsonl"


def parse_sessions(content: str) -> list[dict]:
    """
    Parse session_logs.md into structured entries.
    Each session starts with a header like:
      [🟢 SUCCESS] # Session Log: 2026-04-22
    or:
      # Session Log: 2026-04-26 (parte 1)
    """
    # Match both formats
    header_re = re.compile(
        r'^(?:\[.*?\]\s*)?#\s*Session Log:\s*(\d{4}-\d{2}-\d{2})(?:\s*\((.+?)\))?',
        re.MULTILINE
    )

    matches = list(header_re.finditer(content))
    if not matches:
        return []

    sessions = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)

        date_str = match.group(1)
        part_label = match.group(2) or ""
        section_text = content[start:end].strip()

        # Extract overview (first paragraph after ## 🏁 Session Overview)
        overview_match = re.search(
            r'##\s*🏁\s*Session Overview\s*\n+(.+?)(?=\n##|\Z)',
            section_text,
            re.DOTALL
        )
        overview = ""
        if overview_match:
            # Take first paragraph only
            overview = overview_match.group(1).strip().split("\n\n")[0].strip()

        # Extract key achievements count
        achievements = re.findall(r'###\s*\d+\.', section_text)

        # Extract quality indicator
        quality = "good"
        if "[🟢 SUCCESS]" in section_text:
            quality = "good"
        elif "[🟡 PARTIAL]" in section_text:
            quality = "partial"
        elif "[🔴 MISS]" in section_text:
            quality = "miss"

        # Extract squad mentions
        squad_mentions = set()
        for sq in re.findall(r'squad\s+\*\*(\w+)\*\*', section_text, re.IGNORECASE):
            squad_mentions.add(sq.lower())
        for sq in re.findall(r'`(\w+)`\s+squad', section_text, re.IGNORECASE):
            squad_mentions.add(sq.lower())
        # Common squad names
        for known_squad in ["sexy_content", "data_ops", "lazarus", "smart_shopper", "refract",
                            "from-html-to-carousel", "council_test", "polyglot_tutor"]:
            if known_squad in section_text.lower():
                squad_mentions.add(known_squad)

        # Extract action types
        action_types = set()
        if re.search(r'cria[çr]', section_text, re.IGNORECASE):
            action_types.add("creation")
        if re.search(r'refator|otimiz|upgrad', section_text, re.IGNORECASE):
            action_types.add("architecture")
        if re.search(r'integr|implement', section_text, re.IGNORECASE):
            action_types.add("creation")
        if re.search(r'valid|test|verif', section_text, re.IGNORECASE):
            action_types.add("action")

        try:
            ts = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%dT12:00:00Z")
        except ValueError:
            ts = f"{date_str}T12:00:00Z"

        entry = {
            "ts": ts,
            "event": "session.bridged",
            "source": "bridge_session_logs",
            "date": date_str,
            "part": part_label,
            "topic_summary": overview[:200] if overview else f"Session {date_str}",
            "squads_involved": sorted(squad_mentions),
            "achievements_count": len(achievements),
            "quality": quality,
            "types": sorted(action_types) if action_types else ["action"],
        }

        sessions.append(entry)

    return sessions


def main():
    if not SESSION_LOGS_MD.exists():
        print("session_logs.md not found. Nothing to bridge.")
        return

    with open(SESSION_LOGS_MD, "r") as f:
        content = f.read()

    sessions = parse_sessions(content)

    if not sessions:
        print("No sessions found in session_logs.md.")
        return

    # Check what's already in the JSONL to avoid duplicates
    existing_dates = set()
    if SESSION_LOG_JSONL.exists():
        with open(SESSION_LOG_JSONL, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    if data.get("source") == "bridge_session_logs":
                        existing_dates.add(data.get("date", ""))
                except json.JSONDecodeError:
                    continue

    # Append only new entries
    new_count = 0
    with open(SESSION_LOG_JSONL, "a") as f:
        for session in sessions:
            date_key = session["date"]
            if session.get("part"):
                date_key += f" ({session['part']})"

            if date_key in existing_dates:
                continue

            f.write(json.dumps(session, ensure_ascii=False) + "\n")
            new_count += 1

    print(f"Bridge complete: {new_count} sessions added to session-log.jsonl ({len(sessions)} total parsed, {len(existing_dates)} already bridged)")


if __name__ == "__main__":
    main()
