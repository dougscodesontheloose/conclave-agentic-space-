"""
ingest_staging.py — Manage staging memory files for Conclave ingestion
"""

import os
import sys
import shutil
import hashlib
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
STAGING_DIR = os.path.join(ROOT_DIR, "knowledge", "memory-lane", "staging")
ARCHIVE_DIR = os.path.join(STAGING_DIR, "archive")

def get_file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def list_staging_files():
    if not os.path.exists(STAGING_DIR):
        print(f"Error: Staging directory not found at {STAGING_DIR}")
        return []
    
    files = []
    for item in os.listdir(STAGING_DIR):
        item_path = os.path.join(STAGING_DIR, item)
        if os.path.isfile(item_path):
            if item in ["README.md", ".gitkeep", ".DS_Store"]:
                continue
            files.append(item_path)
    return files

def status():
    files = list_staging_files()
    if not files:
        print("[staging] No pending files in staging area.")
        return
    
    print(f"[staging] Found {len(files)} pending file(s) for ingestion:")
    for f in files:
        rel = os.path.relpath(f, ROOT_DIR)
        size = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M:%S')
        print(f"  - {rel} ({size} bytes, modified: {mtime})")

def archive_file(filepath):
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
        
    filename = os.path.basename(filepath)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_name = f"{ts}_{filename}"
    dest_path = os.path.join(ARCHIVE_DIR, dest_name)
    
    shutil.move(filepath, dest_path)
    print(f"[staging] Archived: {os.path.basename(filepath)} -> staging/archive/{dest_name}")

def archive_all():
    files = list_staging_files()
    if not files:
        print("[staging] Nothing to archive.")
        return
    for f in files:
        archive_file(f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 _conclave/tools/scripts/ingest_staging.py status")
        print("  python3 _conclave/tools/scripts/ingest_staging.py archive <file_path>")
        print("  python3 _conclave/tools/scripts/ingest_staging.py archive-all")
        sys.exit(0)
        
    cmd = sys.argv[1]
    if cmd == "status":
        status()
    elif cmd == "archive" and len(sys.argv) > 2:
        target = sys.argv[2]
        if not os.path.isabs(target):
            target = os.path.join(ROOT_DIR, target)
        if os.path.exists(target):
            archive_file(target)
        else:
            print(f"Error: File not found: {target}")
    elif cmd == "archive-all":
        archive_all()
    else:
        print(f"Unknown command: {cmd}")
