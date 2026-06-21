---
execution: subagent
agent: "pris-python"
inputFile: squads/refract/output/task-brief.md
outputFile: squads/refract/output/backend-status.md
model_tier: powerful
---

# Step 02: Build Backend (condicional)

## Context Loading

- `squads/refract/output/task-brief.md` — task-brief com flag `python_needed`

## Instructions

### Process
1. Assumir persona de Pris Python.
2. Ler o task-brief. Se `python_needed: false`, escrever `backend-status.md` com `status: skipped` e retornar imediatamente.
3. Se `python_needed: true`, executar a task `build-backend.md`: scaffold, venv, FastAPI/pipeline/conversor, type hints, schemas JSON em `contracts/`.
4. Rodar `uvicorn` (ou o comando equivalente ao modo) e validar que o endpoint/script funciona.
5. Escrever `backend-status.md` com `status: built`, arquivos criados, endpoints/comandos disponíveis.

## Output Format

```yaml
status: "built" | "skipped"
mode: "api" | "pipeline" | "conversor" | null
path: "squads/refract/output/backend/" | null
entrypoint: "uvicorn main:app" | "python pipeline.py" | null
endpoints:
  - method: GET
    path: /health
    response: "{status: ok}"
contracts_exported:
  - backend/contracts/planet.schema.json
notes: "..."
```

## Output Example

```yaml
status: "built"
mode: "api"
path: "squads/refract/output/2026-04-19-orbital-viewer/backend/"
entrypoint: "uvicorn main:app --reload"
endpoints:
  - method: GET
    path: /health
    response: '{"status": "ok"}'
  - method: GET
    path: /api/planets
    response: "List[Planet]"
contracts_exported:
  - backend/contracts/planet.schema.json
notes: "FastAPI 0.115, Pydantic 2.9, Python 3.12.4"
```

## Veto Conditions

1. Arquivos em `backend/` escritos mesmo com `python_needed: false`.
2. Modo API sem endpoint /health funcional.
3. Type hints ausentes no código gerado.

## Quality Criteria

- [ ] Flag `python_needed` foi consultada antes de agir.
- [ ] Se `built`: endpoint/script validado.
- [ ] Contracts JSON exportados se modo API.
