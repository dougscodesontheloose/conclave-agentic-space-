#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
import shutil
import re

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

def run_cmd(cmd, cwd=None):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error executing {cmd}: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def check_file_sizes(directory):
    print("Checking file sizes to prevent GH001 blocking...")
    # Get all tracked and untracked files respecting gitignore
    out = run_cmd("git ls-files -c -o --exclude-standard", cwd=directory)
    files = out.split('\n')
    for f in files:
        if not f:
            continue
        path = os.path.join(directory, f)
        if os.path.exists(path) and not os.path.islink(path):
            size = os.path.getsize(path)
            if size > MAX_FILE_SIZE:
                print(f"ERROR: File {path} exceeds 100MB ({size / 1024 / 1024:.2f}MB). Aborting backup.")
                sys.exit(1)
    print("✓ All files are under 100MB.")

def sanitize_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Remove mentions of names
        content = re.sub(r'\bDouglas\b', '<user_name>', content, flags=re.IGNORECASE)
        content = re.sub(r'\bDoug\b', '<user_name>', content, flags=re.IGNORECASE)
        content = re.sub(r'\bDogue\b', '<user_name>', content, flags=re.IGNORECASE)
        
        # Remove secrets (rough regexes for tokens)
        content = re.sub(r'sk-[a-zA-Z0-9]{32,}', '<api_key_removed>', content)
        content = re.sub(r'(client_secret|access_token)[\s:=]+[\'"]?[a-zA-Z0-9\-_]+[\'"]?', r'\1 = "<secret_removed>"', content, flags=re.IGNORECASE)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        pass # Ignore binary files or read errors

def fullride_backup():
    print("Starting Exodus: Fullride (Private Backup)")
    check_file_sizes(".")
    
    run_cmd("git add .")
    try:
        run_cmd("git commit -m \"chore(exodus): commit fullride de seguranca\"")
    except SystemExit:
        print("Nothing to commit or commit failed.")
        
    print("Pushing to origin main...")
    run_cmd("git push origin main")
    print("✓ Fullride backup complete.")

def opensource_backup():
    print("Starting Exodus: Open Source (Sanitized Export)")
    export_dir = "_export_opensource"
    
    if os.path.exists(export_dir):
        shutil.rmtree(export_dir)
    os.makedirs(export_dir)
    
    print("Copying core structure...")
    # Basic directories to copy
    dirs_to_copy = ["_conclave", "squads", "skills"]
    for d in dirs_to_copy:
        if os.path.exists(d):
            shutil.copytree(
                d, 
                os.path.join(export_dir, d), 
                dirs_exist_ok=True,
                ignore=shutil.ignore_patterns('browser_profile', '*.sock', 'Singleton*', 'scratch', 'runtime')
            )
            
    # Copy essential files
    files_to_copy = ["AGENTS.md", "CLAUDE.md", "README.md", "TUTORIAL.md"]
    for f in files_to_copy:
        if os.path.exists(f):
            shutil.copy2(f, export_dir)

    print("Sanitizing contents and removing private squads...")
    private_squads = ["cliff_palace", "corner-office", "lazarus", "dream_catcher"]
    for p_squad in private_squads:
        sq_path = os.path.join(export_dir, "squads", p_squad)
        if os.path.exists(sq_path):
            shutil.rmtree(sq_path)

    # Walk through export dir and sanitize
    for root, dirs, files in os.walk(export_dir):
        # Empty memory logs
        if "_memory" in root or "logs" in root:
            for file in files:
                if file.endswith(".md") or file.endswith(".jsonl") or file.endswith(".json"):
                    with open(os.path.join(root, file), 'w') as f:
                        if file.endswith(".json"):
                            f.write("{}")
                        elif file.endswith(".jsonl"):
                            f.write("")
                        else:
                            f.write("<!-- User memory cleared -->\n")
            continue
            
        for file in files:
            # We don't want any .bak files leaking
            if ".bak-" in file:
                os.remove(os.path.join(root, file))
                continue
            
            filepath = os.path.join(root, file)
            if file.endswith(".md") or file.endswith(".json") or file.endswith(".yaml") or file.endswith(".py") or file.endswith(".sh"):
                sanitize_file(filepath)

    print("✓ Open Source sanitization complete.")
    print(f"Cleaned repository is available at: {export_dir}/")
    print("To push to public github, cd into the folder, init git, add a public remote, and push.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exodus Protocol Engine")
    parser.add_argument("--mode", choices=["fullride", "opensource"], required=True, help="Mode of export")
    args = parser.parse_args()

    if args.mode == "fullride":
        fullride_backup()
    elif args.mode == "opensource":
        opensource_backup()
