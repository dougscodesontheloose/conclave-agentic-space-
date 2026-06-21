import os
import sys
import json
import yaml

CONCLAVE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SQUADS_DIR = os.path.join(CONCLAVE_ROOT, "squads")
AGENTS_DIR = os.path.join(CONCLAVE_ROOT, "_conclave", "agents")
SKILLS_DIR = os.path.join(CONCLAVE_ROOT, "_conclave", "skills")
INTENTION_MATRIX = os.path.join(CONCLAVE_ROOT, "_conclave", "core", "intention_matrix.json")

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def auto_repair_intention_matrix(squad_code):
    print(f"🔧 Sentinel Auto-Repair: Removendo stub quebrado '{squad_code}' do intention_matrix...")
    try:
        matrix = load_json(INTENTION_MATRIX)
        new_matrix = [entry for entry in matrix if entry.get("squad_id") != squad_code]
        if len(matrix) != len(new_matrix):
            with open(INTENTION_MATRIX, 'w') as f:
                json.dump(new_matrix, f, indent=2, ensure_ascii=False)
            print("🔧 Reparo concluído.")
    except Exception as e:
        print(f"⚠️ Erro ao tentar reparar intention_matrix: {e}")

def run_preflight(squad_code):
    print(f"🛡️ Sentinel Pre-Flight Check: Iniciando validação para squad '{squad_code}'")
    squad_dir = os.path.join(SQUADS_DIR, squad_code)
    squad_yaml_path = os.path.join(squad_dir, "squad.yaml")

    # 1. Validar que o squad alvo existe e tem squad.yaml válido
    if not os.path.exists(squad_dir):
        print(f"❌ Erro: Diretório do squad '{squad_code}' não existe.")
        auto_repair_intention_matrix(squad_code)
        sys.exit(1)

    if not os.path.exists(squad_yaml_path):
        print(f"❌ Erro: squad.yaml não encontrado em '{squad_dir}'.")
        auto_repair_intention_matrix(squad_code)
        sys.exit(1)

    try:
        squad_data = load_yaml(squad_yaml_path)
    except Exception as e:
        print(f"❌ Erro: squad.yaml inválido para '{squad_code}': {e}")
        sys.exit(1)

    # Verifica se é um redirecionamento
    if "redirect_to" in squad_data:
        print(f"ℹ️ Squad '{squad_code}' é um redirecionamento para '{squad_data['redirect_to']}'.")
        return

    # 2. Verifica que todos os agentes referenciados têm .agent.md
    party_csv_path = os.path.join(squad_dir, "squad-party.csv")
    if os.path.exists(party_csv_path):
        with open(party_csv_path, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]: # skip header
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    agent_path_rel = parts[3]
                    agent_path_abs = os.path.normpath(os.path.join(squad_dir, agent_path_rel))
                    if not os.path.exists(agent_path_abs):
                        print(f"❌ Erro: Agente referenciado '{agent_path_rel}' não encontrado em {agent_path_abs}.")
                        sys.exit(1)
    else:
        print(f"⚠️ Aviso: squad-party.csv não encontrado para '{squad_code}'.")

    # 3. Checa se skills declarados estão instalados
    skills = squad_data.get("skills", [])
    if skills:
        for skill in skills:
            if skill in ["web_search", "web_fetch"]:
                continue
            skill_path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
            if not os.path.exists(skill_path):
                print(f"❌ Erro: Skill '{skill}' referenciada não está instalada ({skill_path}).")
                sys.exit(1)

    # 4. Valida que paths referenciados em data existem
    data_paths = squad_data.get("data", [])
    if data_paths:
        for data_rel_path in data_paths:
            data_path_abs = os.path.normpath(os.path.join(squad_dir, data_rel_path))
            if not os.path.exists(data_path_abs):
                print(f"⚠️ Aviso: Path referenciado '{data_rel_path}' não encontrado em {data_path_abs}.")

    print("✅ Sentinel Pre-Flight: Checks passaram. Sistema pronto para execução.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 sentinel_preflight.py <squad_code>")
        sys.exit(1)
    run_preflight(sys.argv[1])
