import os
import sys
import json
import yaml
from datetime import datetime, timedelta

CONCLAVE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SQUADS_DIR = os.path.join(CONCLAVE_ROOT, "squads")
AGENTS_DIR = os.path.join(CONCLAVE_ROOT, "_conclave", "agents")
SKILLS_DIR = os.path.join(CONCLAVE_ROOT, "_conclave", "skills")
MEMORY_DIR = os.path.join(CONCLAVE_ROOT, "_conclave", "state", "memory")
HISTORY_DIR = os.path.join(CONCLAVE_ROOT, "_conclave", "state", "history")
INTENTION_MATRIX = os.path.join(CONCLAVE_ROOT, "_conclave", "core", "intention_matrix.json")
REGISTRY_FILE = os.path.join(MEMORY_DIR, "sentinel_registry.json")
REPORT_FILE = os.path.join(CONCLAVE_ROOT, "_conclave", "runtime", "scratch", "sentinel-report.md")

def load_json(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

def load_yaml(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    return None

def write_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def log_anomaly(registry, anomaly_type, description, severity="medium", auto_repaired=False):
    registry.setdefault("anomalies", []).append({
        "ts": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": anomaly_type,
        "description": description,
        "severity": severity,
        "auto_repaired": auto_repaired
    })

def scan_agents(registry, findings):
    findings["agents"] = {"total": 0, "issues": []}
    if not os.path.exists(AGENTS_DIR): return
    for f in os.listdir(AGENTS_DIR):
        if f.endswith(".agent.md"):
            findings["agents"]["total"] += 1
            path = os.path.join(AGENTS_DIR, f)
            with open(path, 'r') as file:
                content = file.read()
                if not content.startswith("---"):
                    issue = f"Missing frontmatter in {f}"
                    findings["agents"]["issues"].append(issue)
                    log_anomaly(registry, "agent_structure", issue, "low", False)

def scan_squads(registry, findings):
    findings["squads"] = {"total": 0, "broken_stubs": [], "issues": []}
    if not os.path.exists(SQUADS_DIR): return
    matrix = load_json(INTENTION_MATRIX) or []
    matrix_squads = [s.get("squad_id") for s in matrix]
    
    for d in os.listdir(SQUADS_DIR):
        path = os.path.join(SQUADS_DIR, d)
        if os.path.isdir(path):
            findings["squads"]["total"] += 1
            squad_yaml = os.path.join(path, "squad.yaml")
            if not os.path.exists(squad_yaml):
                issue = f"Broken stub detected: {d} (missing squad.yaml)"
                findings["squads"]["broken_stubs"].append(d)
                # Auto-repair logic
                if d in matrix_squads:
                    matrix = [entry for entry in matrix if entry.get("squad_id") != d]
                    write_json(matrix, INTENTION_MATRIX)
                    log_anomaly(registry, "squad_structure", f"Removed stub {d} from intention_matrix", "low", True)
                    findings["squads"]["issues"].append(f"Auto-repaired: {issue}")
                else:
                    findings["squads"]["issues"].append(issue)
            else:
                data = load_yaml(squad_yaml)
                if not data:
                    findings["squads"]["issues"].append(f"Invalid squad.yaml in {d}")

def scan_memory(registry, findings):
    findings["memory"] = {"total": 0, "stale": []}
    if not os.path.exists(MEMORY_DIR): return
    cutoff_date = datetime.now() - timedelta(days=60)
    
    for f in os.listdir(MEMORY_DIR):
        if f.endswith(".md") or f.endswith(".json"):
            findings["memory"]["total"] += 1
            path = os.path.join(MEMORY_DIR, f)
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            if mtime < cutoff_date:
                # Basic check, ignores if frontmatter has recent last_validated
                findings["memory"]["stale"].append(f)
                log_anomaly(registry, "stale_memory", f"Memory {f} is older than 60 days", "low", False)

def run_deepscan():
    print("🛡️ Sentinel Deep Scan: Iniciando...")
    registry = load_json(REGISTRY_FILE) or {
        "system_health": "nominal",
        "last_deep_scan": None,
        "anomalies": [],
        "metrics": {"total_squads": 0, "total_skills": 0, "agents_active": 0}
    }
    
    findings = {}
    scan_agents(registry, findings)
    scan_squads(registry, findings)
    scan_memory(registry, findings)
    
    # Update metrics
    registry["metrics"]["total_squads"] = findings.get("squads", {}).get("total", 0)
    registry["metrics"]["agents_active"] = findings.get("agents", {}).get("total", 0)
    registry["last_deep_scan"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Determine health
    critical_issues = len(findings.get("squads", {}).get("issues", [])) + len(findings.get("agents", {}).get("issues", []))
    if critical_issues > 0:
        registry["system_health"] = "degraded"
    else:
        registry["system_health"] = "nominal"
        
    write_json(registry, REGISTRY_FILE)
    
    # Generate Report
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, 'w') as f:
        f.write("# 🛡️ Sentinel Deep Scan Report\n\n")
        f.write(f"**Date:** {registry['last_deep_scan']}\n")
        f.write(f"**System Health:** {registry['system_health'].upper()}\n\n")
        
        f.write("## 📋 Metrics\n")
        f.write(f"- Active Agents: {registry['metrics']['agents_active']}\n")
        f.write(f"- Total Squads: {registry['metrics']['total_squads']}\n\n")
        
        f.write("## 🔍 Findings\n")
        for k, v in findings.items():
            f.write(f"### {k.capitalize()}\n")
            if "issues" in v and v["issues"]:
                for issue in v["issues"]:
                    f.write(f"- ⚠️ {issue}\n")
            if "stale" in v and v["stale"]:
                for stale in v["stale"]:
                    f.write(f"- 🟡 Stale (needs review): {stale}\n")
            if not v.get("issues") and not v.get("stale"):
                f.write("- ✅ Nominal\n")
            f.write("\n")
            
    print(f"✅ Sentinel Deep Scan concluído. Relatório gerado em {REPORT_FILE}")

if __name__ == "__main__":
    run_deepscan()
