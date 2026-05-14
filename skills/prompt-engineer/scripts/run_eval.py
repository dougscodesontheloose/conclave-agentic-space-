#!/usr/bin/env python3
"""
Run evaluation queries against the prompt-engineer skill.
Outputs a test plan with expected trigger/no-trigger status.

Usage: python3 scripts/run_eval.py [--split train|validation|all]
"""

import argparse
import json
import sys
from pathlib import Path

EVALS_FILE = Path(__file__).resolve().parent.parent / "evals" / "evals.json"


def load_evals(split: str) -> list:
    if not EVALS_FILE.exists():
        print(f"❌ evals.json not found at {EVALS_FILE}")
        sys.exit(1)

    with open(EVALS_FILE) as f:
        evals = json.load(f)

    if split != "all":
        evals = [e for e in evals if e.get("split") == split]

    return evals


def print_eval_plan(evals: list, split: str):
    trigger = [e for e in evals if e["should_trigger"]]
    no_trigger = [e for e in evals if not e["should_trigger"]]

    print(f"\n{'='*60}")
    print(f"EVAL PLAN — Split: {split.upper()}")
    print(f"{'='*60}")

    print(f"\n🟢 SHOULD TRIGGER ({len(trigger)} queries):")
    print("-" * 60)
    for i, e in enumerate(trigger, 1):
        print(f"  {i:2d}. \"{e['query']}\"")
        print(f"      Notes: {e.get('notes', 'N/A')}")

    print(f"\n🔴 SHOULD NOT TRIGGER ({len(no_trigger)} queries):")
    print("-" * 60)
    for i, e in enumerate(no_trigger, 1):
        print(f"  {i:2d}. \"{e['query']}\"")
        print(f"      Notes: {e.get('notes', 'N/A')}")

    print(f"\n{'='*60}")
    print(f"Total: {len(evals)} queries ({len(trigger)} trigger / {len(no_trigger)} no-trigger)")
    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(description="Run prompt-engineer skill evals")
    parser.add_argument(
        "--split",
        choices=["train", "validation", "all"],
        default="all",
        help="Which eval split to run (default: all)",
    )
    args = parser.parse_args()

    evals = load_evals(args.split)
    if not evals:
        print(f"No evals found for split '{args.split}'")
        sys.exit(1)

    print_eval_plan(evals, args.split)


if __name__ == "__main__":
    main()
