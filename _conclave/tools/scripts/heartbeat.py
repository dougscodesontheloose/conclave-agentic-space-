#!/usr/bin/env python3
"""
Conclave Heartbeat (SafeGuard & Guardrails)
Ensures system integrity and security compliance at session boundaries.
"""

import os
import sys
import json
import time
from pathlib import Path
import subprocess

# Colors
G = "\033[92m"; R = "\033[91m"; Y = "\033[93m"; C = "\033[96m"; B = "\033[1m"; X = "\033[0m"

def run_integrity():
    print(f"{B}[HEARTBEAT]{X} Running Integrity Check...")
    try:
        # Run existing validation script
        result = subprocess.run([sys.executable, "_conclave/tools/scripts/validate_conclave.py"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  {G}✓{X} Core Integrity: OK")
            return True
        else:
            print(f"  {R}✗{X} Core Integrity: FAIL")
            print(result.stdout)
            return False
    except Exception as e:
        print(f"  {R}✗{X} Error running validation: {e}")
        return False

def check_vault():
    print(f"{B}[HEARTBEAT]{X} Checking SafeGuard Vault...")
    # Check if .vault directories are correctly gitignored or protected
    vaults = list(Path(".").rglob(".vault"))
    if not vaults:
        print(f"  {G}✓{X} No exposed .vault directories found.")
        return True
    
    # Check .gitignore for .vault
    gitignore = Path(".gitignore")
    if gitignore.exists():
        content = gitignore.read_text()
        if ".vault" in content:
            print(f"  {G}✓{X} .vault is protected by .gitignore")
            return True
        else:
            print(f"  {Y}⚠{X} .vault directories exist but are NOT in .gitignore!")
            return False
    return True

def scan_leaks():
    print(f"{B}[HEARTBEAT]{X} Scanning for TIER: SECRET leaks in outputs...")
    # Scan squads/*/output/ for common sensitive patterns (very basic)
    # In a real scenario, this would use a list of patterns from company.md or a vault
    secret_patterns = ["password", "secret_key", "api_key", "cpf", "rg"] # Example patterns
    leaks_found = []
    import re
    # Create regex patterns with word boundaries for short strings to prevent false positives (like 'argument' triggering 'rg')
    compiled_patterns = {p: re.compile(rf'\b{re.escape(p)}\b', re.IGNORECASE) for p in secret_patterns}
    
    output_dirs = list(Path("squads").glob("*/output"))
    for d in output_dirs:
        for f in d.rglob("*"):
            if f.is_file() and f.suffix in [".txt", ".md", ".json", ".log"]:
                try:
                    content = f.read_text(errors='ignore')
                    for p, regex in compiled_patterns.items():
                        if regex.search(content):
                            leaks_found.append(f"{f} (pattern: {p})")
                except:
                    pass
    
    if not leaks_found:
        print(f"  {G}✓{X} No obvious leaks detected in outputs.")
        return True
    else:
        print(f"  {R}✗{X} Potential leaks found:")
        for leak in leaks_found:
            print(f"    - {leak}")
        return False

def start_session():
    print(f"\n{B}=== CONCLAVE HEARTBEAT: SESSION START ==={X}")
    i_ok = run_integrity()
    v_ok = check_vault()
    
    if i_ok and v_ok:
        print(f"\n{G}STATUS: SYSTEM HEALTHY. SAFEGUARD ACTIVE.{X}\n")
    else:
        print(f"\n{R}STATUS: SECURITY ALERT. CHECK LOGS.{X}\n")

def end_session():
    print(f"\n{B}=== CONCLAVE HEARTBEAT: SESSION END ==={X}")
    l_ok = scan_leaks()
    
    # Log session end
    log_file = Path("_conclave/runtime/logs/audit.jsonl")
    log_entry = {
        "event": "session_end",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "leaks_detected": not l_ok
    }
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
        
    if l_ok:
        print(f"\n{G}STATUS: CLEAN EXIT. ALL GUARDRAILS MET.{X}\n")
    else:
        print(f"\n{Y}STATUS: WARNING. POTENTIAL DATA LEAK DETECTED.{X}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: heartbeat.py --start | --end")
        sys.exit(1)
        
    mode = sys.argv[1]
    if mode == "--start":
        start_session()
    elif mode == "--end":
        end_session()
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)
