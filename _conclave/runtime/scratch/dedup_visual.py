import os
import hashlib

def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

root_dir = "/Users/douglasdepaulamoura/Documents/Bancada/Conclave/references/visual-style"
new_files = [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f)) and f != ".DS_Store"]

hashes = {}
# Index existing files
for root, dirs, files in os.walk(root_dir):
    if root == root_dir:
        continue # Skip root files for indexing
    for f in files:
        if f.startswith("."): continue
        path = os.path.join(root, f)
        h = get_hash(path)
        hashes[h] = path

duplicates = []
to_move = []

for f in new_files:
    path = os.path.join(root_dir, f)
    h = get_hash(path)
    if h in hashes:
        duplicates.append((path, hashes[h]))
    else:
        to_move.append(path)

print(f"Found {len(duplicates)} duplicates.")
for d in duplicates:
    print(f"DUP: {d[0]} == {d[1]}")
    os.remove(d[0])

print(f"Ready to move {len(to_move)} files to Design de Estilos.")
for f in to_move:
    target = os.path.join(root_dir, "Design de Estilos", os.path.basename(f))
    # Rename if collision
    if os.path.exists(target):
        base, ext = os.path.splitext(target)
        target = f"{base}_alt{ext}"
    os.rename(f, target)
