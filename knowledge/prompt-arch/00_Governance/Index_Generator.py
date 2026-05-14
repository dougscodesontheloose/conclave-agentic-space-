import os
import json
import re

def generate_index(base_path="."):
    index = {
        "agents": [],
        "frameworks": [],
        "prompts": [],
        "use_cases": [],
        "skills": []
    }
    
    mapping = {
        "01_Agents": "agents",
        "02_Frameworks": "frameworks",
        "03_Library/Prompts": "prompts",
        "04_Use_Cases": "use_cases",
        "05_Skills": "skills"
    }
    
    for folder, key in mapping.items():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            continue
            
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read(500) # Lê os primeiros 500 caracteres para resumo
                    # Tenta pegar o primeiro título H1 ou H2 como descrição
                    title_match = re.search(r'^#+ (.+)$', content, re.M)
                    title = title_match.group(1) if title_match else file.replace(".md", "")
                    
                    index[key].append({
                        "name": title,
                        "file": file,
                        "path": file_path,
                        "snippet": content[:200].replace("\n", " ") + "..."
                    })
    
    with open("00_Governance/library_index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4, ensure_ascii=False)
    
    return f"Index generated with {sum(len(v) for v in index.values())} entries."

if __name__ == "__main__":
    result = generate_index()
    print(result)
