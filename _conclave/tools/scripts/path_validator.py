#!/usr/bin/env python3
import sys
import os

# Authorized Zone boundary
AUTHORIZED_ZONE = "/Users/douglasdepaulamoura/Documents/Bancada"

def validate_path(target_path):
    resolved_path = os.path.abspath(target_path)
    
    if not resolved_path.startswith(AUTHORIZED_ZONE):
        print(f"VETO: Path '{target_path}' resolves to '{resolved_path}' which escapes the authorized zone '{AUTHORIZED_ZONE}'.")
        sys.exit(1)
    
    print("OK")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 path_validator.py <target_path>", file=sys.stderr)
        sys.exit(1)
    
    validate_path(sys.argv[1])
