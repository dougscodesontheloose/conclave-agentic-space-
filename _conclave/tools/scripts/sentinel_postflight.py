import os
import sys
import json
from datetime import datetime

CONCLAVE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
INTENTION_MATRIX = os.path.join(CONCLAVE_ROOT, "_conclave", "core", "intention_matrix.json")
BREADCRUMBS_FILE = os.path.join(CONCLAVE_ROOT, "_conclave", "runtime", "scratch", "session-breadcrumbs.jsonl")

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def emit_breadcrumb(squad_code, run_id, success):
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    session_id = datetime.now().strftime("%Y-%m-%d")
    quality = "good" if success else "miss"
    value = f"Execução do squad {squad_code} concluída (run_id: {run_id})."
    
    breadcrumb = {
        "ts": ts,
        "session_id": session_id,
        "type": "squad_work",
        "value": value,
        "squad": squad_code,
        "quality": quality
    }
    
    os.makedirs(os.path.dirname(BREADCRUMBS_FILE), exist_ok=True)
    with open(BREADCRUMBS_FILE, 'a') as f:
        f.write(json.dumps(breadcrumb) + "\n")

def run_postflight(squad_code, run_id, success):
    print(f"🛡️ Sentinel Post-Flight: Finalizando squad '{squad_code}' (Run ID: {run_id})")
    
    # 1. Incrementa usage_count e last_run no intention_matrix
    try:
        matrix = load_json(INTENTION_MATRIX)
        updated = False
        for entry in matrix:
            if entry.get("squad_id") == squad_code:
                entry["usage_count"] = entry.get("usage_count", 0) + 1
                entry["last_run"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                updated = True
                break
        
        if updated:
            with open(INTENTION_MATRIX, 'w') as f:
                json.dump(matrix, f, indent=2, ensure_ascii=False)
            print("✅ Intention Matrix atualizada com tracking de uso.")
    except Exception as e:
        print(f"⚠️ Erro ao atualizar intention matrix: {e}")

    # 2. Verifica se outputs foram gerados no diretório esperado
    output_dir = os.path.join(CONCLAVE_ROOT, "squads", squad_code, "output", run_id)
    if not os.path.exists(output_dir) or not os.listdir(output_dir):
        print(f"⚠️ Aviso: Nenhum output detectado em {output_dir}")
        success = False
    else:
        print(f"✅ Outputs verificados em {output_dir}")

    # 3. Detecta se arquivos de memória foram modificados
    memory_file = os.path.join(CONCLAVE_ROOT, "squads", squad_code, "_memory", "memories.md")
    if os.path.exists(memory_file):
        pass # Optional logic to compare timestamps

    # 4. Emite breadcrumb
    emit_breadcrumb(squad_code, run_id, success)
    print("✅ Sentinel Post-Flight concluído.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 sentinel_postflight.py <squad_code> <run_id> [success=true]")
        sys.exit(1)
    
    squad_code = sys.argv[1]
    run_id = sys.argv[2]
    success = True
    if len(sys.argv) >= 4:
        success = sys.argv[3].lower() == "true"
        
    run_postflight(squad_code, run_id, success)
