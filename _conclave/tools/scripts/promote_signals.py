#!/usr/bin/env python3
"""
promote_signals.py - Promotes frequent implicit signals to explicit squad memory.
Reads squads/*/_memory/implicit-signals.jsonl. If any signal appears >= 5 times,
it is appended to memories.md under ## [SYSTEM_PROMOTED] Mapped Patterns,
and the processed signals are removed from the jsonl file.
"""

import os
import json
from collections import defaultdict

def main():
    conclave_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    squads_dir = os.path.join(conclave_dir, "..", "squads")
    
    if not os.path.isdir(squads_dir):
        return

    PROMOTION_THRESHOLD = 5

    for squad in os.listdir(squads_dir):
        squad_path = os.path.join(squads_dir, squad)
        if not os.path.isdir(squad_path):
            continue
            
        memory_dir = os.path.join(squad_path, "_memory")
        signals_file = os.path.join(memory_dir, "implicit-signals.jsonl")
        memories_file = os.path.join(memory_dir, "memories.md")
        
        if not os.path.isfile(signals_file):
            continue
            
        # Count signals
        signal_counts = defaultdict(int)
        all_signals = []
        
        with open(signals_file, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    data = json.loads(line)
                    # Extract a meaningful string to track
                    # Adjust based on the actual schema used by the runner
                    signal_text = data.get("value") or data.get("signal") or data.get("content") or data.get("pattern") or ""
                    signal_type = data.get("signal_type", "unknown")
                    
                    if signal_text:
                        key = f"[{signal_type.upper()}] {signal_text}"
                        signal_counts[key] += 1
                    
                    all_signals.append(data)
                except json.JSONDecodeError:
                    continue
                    
        # Identify promoted
        promoted = []
        for key, count in signal_counts.items():
            if count >= PROMOTION_THRESHOLD:
                promoted.append(key)
                
        if not promoted:
            continue
            
        # Write to memories.md
        if os.path.isfile(memories_file):
            with open(memories_file, "r") as f:
                content = f.read()
                
            promoted_text = "\n".join([f"- {p}" for p in promoted]) + "\n"
            
            # Check if section exists
            section_header = "## [SYSTEM_PROMOTED] Mapped Patterns"
            if section_header in content:
                content = content.replace(section_header, section_header + "\n" + promoted_text)
            else:
                content += f"\n{section_header}\n{promoted_text}"
                
            with open(memories_file, "w") as f:
                f.write(content)
                
        # Clean up jsonl by removing promoted signals
        remaining_signals = []
        for data in all_signals:
            signal_text = data.get("signal") or data.get("content") or data.get("pattern") or ""
            signal_type = data.get("signal_type", "unknown")
            key = f"[{signal_type.upper()}] {signal_text}"
            
            if key not in promoted:
                remaining_signals.append(data)
                
        with open(signals_file, "w") as f:
            for data in remaining_signals:
                f.write(json.dumps(data) + "\n")

if __name__ == "__main__":
    main()
