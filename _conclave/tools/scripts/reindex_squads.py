import os
import json

EXTRA_INTENTS_BY_SQUAD = {
    "polyglot_tutor": [
        "idioma",
        "idiomas",
        "language",
        "languages",
        "aprender idioma",
        "estudar idioma",
        "poliglota",
        "polyglot",
        "polyglot_tutor",
        "poliglopter",
        "inglês",
        "ingles",
        "english",
        "id like some tea",
        "i'd like some tea",
        "espanhol",
        "spanish",
        "hablando",
        "hablando demais",
        "italiano",
        "italian",
        "ci vediamo dopo",
        "francês",
        "frances",
        "french",
        "cé la vie",
        "ce la vie",
        "c'est la vie",
        "japonês",
        "japones",
        "japanese",
        "gozaimasu",
        "grego",
        "greek",
        "grego moderno",
        "omega",
    ],
}

EXTRA_CONTEXT_TRIGGERS_BY_SQUAD = {
    "polyglot_tutor": [
        "ambientes/projetos/Id like some tea",
        "ambientes/projetos/Hablando demais!",
        "ambientes/projetos/ci vediamo dopo",
        "ambientes/projetos/Cé la vie",
        "ambientes/projetos/gozaimasu",
        "ambientes/projetos/Omega",
    ],
}

def parse_simple_yaml(content):
    data = {}
    for line in content.splitlines():
        if ':' in line and not line.strip().startswith('#'):
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data

def reindex():
    squads_dir = 'squads'
    matrix_file = '_conclave/core/intention_matrix.json'
    
    existing_data = {}
    if os.path.exists(matrix_file):
        with open(matrix_file, 'r') as f:
            try:
                data = json.load(f)
                for entry in data:
                    existing_data[entry['squad_id']] = {
                        'usage_count': entry.get('usage_count', 0),
                        'last_run': entry.get('last_run', None)
                    }
            except:
                pass

    new_matrix = []
    
    if not os.path.exists(squads_dir):
        return

    for squad_code in os.listdir(squads_dir):
        squad_path = os.path.join(squads_dir, squad_code)
        if not os.path.isdir(squad_path):
            continue
            
        yaml_path = os.path.join(squad_path, 'squad.yaml')
        if not os.path.exists(yaml_path):
            continue
            
        with open(yaml_path, 'r') as f:
            try:
                config = parse_simple_yaml(f.read())
                
                description = config.get('description', '')
                display_name = config.get('name', squad_code)
                
                intents = []
                if "linkedin" in description.lower(): intents.append("linkedin")
                if "post" in description.lower(): intents.append("post")
                if "carrossel" in description.lower() or "carousel" in description.lower(): intents.append("carrossel")
                if "código" in description.lower() or "engineering" in description.lower(): intents.append("código")
                if "pwa" in description.lower(): intents.append("pwa")
                intents.extend(EXTRA_INTENTS_BY_SQUAD.get(squad_code, []))
                
                entry = {
                    "squad_id": squad_code,
                    "displayName": display_name,
                    "description": description,
                    "intents": list(set(intents)), 
                    "context_triggers": EXTRA_CONTEXT_TRIGGERS_BY_SQUAD.get(squad_code, []),
                    "usage_count": existing_data.get(squad_code, {}).get('usage_count', 0),
                    "last_run": existing_data.get(squad_code, {}).get('last_run', None)
                }
                new_matrix.append(entry)
            except Exception as e:
                print(f"Error parsing {yaml_path}: {e}")

    with open(matrix_file, 'w') as f:
        json.dump(new_matrix, f, indent=2, ensure_ascii=False)
    print(f"Successfully reindexed {len(new_matrix)} squads.")

if __name__ == "__main__":
    reindex()
