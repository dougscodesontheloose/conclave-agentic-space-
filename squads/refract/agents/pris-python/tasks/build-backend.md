---
task: "Build Backend"
order: 1
input: |
  - task_brief: output/{run-id}/task-brief.md (só executa se python_needed=true)
output: |
  - backend_code: backend/ com API rodável ou pipeline executado
  - contracts: backend/contracts/*.json (schemas JSON para o Wade Web)
---

# Build Backend

Constrói o backend Python conforme declarado no task-brief. Modo default é FastAPI servindo API local; modos alternativos são pipeline de dados batch ou scripts utilitários de conversão.

## Process

1. Abortar imediatamente se `python_needed: false` no task-brief. Retornar sem escrever arquivos.
2. Criar virtualenv em `backend/.venv` com Python 3.12+.
3. Escolher modo:
   - **API**: FastAPI + Pydantic v2 + uvicorn. Estrutura: `main.py`, `routers/`, `schemas/`, `services/`.
   - **Pipeline**: script único `pipeline.py` que lê input, processa, escreve output no formato web-friendly.
   - **Conversor**: utilitários em `tools/` (ex: `obj_to_gltf.py`).
4. Tipagem estrita com type hints em 100% do código; rodar `pyright --strict` e corrigir até passar.
5. Exportar schemas Pydantic em JSON Schema para `backend/contracts/` (um arquivo por model).
6. Se modo API: validar com curl — incluir `README.md` com comandos de exemplo.
7. `requirements.txt` pinado via `pip freeze > requirements.txt` após instalar deps.

## Output Format

Estrutura de `backend/` (modo API):
```
backend/
├── .venv/
├── main.py
├── routers/
│   └── {domain}.py
├── schemas/
│   └── {entity}.py
├── services/
│   └── {logic}.py
├── contracts/
│   └── {entity}.schema.json
├── requirements.txt
└── README.md
```

## Output Example

```python
# backend/main.py
from fastapi import FastAPI
from routers import planets

app = FastAPI(title="Refract Backend — Orbital Viewer", version="1.0.0")
app.include_router(planets.router, prefix="/api/planets", tags=["planets"])

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
```

```python
# backend/schemas/planet.py
from pydantic import BaseModel, Field

class Planet(BaseModel):
    id: str = Field(..., examples=["earth"])
    name: str
    radius_km: float
    orbital_period_days: float
    distance_au: float
    color_hex: str = Field(..., pattern=r"^#[0-9A-Fa-f]{6}$")
```

```json
// backend/contracts/planet.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Planet",
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "name": {"type": "string"},
    "radius_km": {"type": "number"},
    "orbital_period_days": {"type": "number"},
    "distance_au": {"type": "number"},
    "color_hex": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"}
  },
  "required": ["id", "name", "radius_km", "orbital_period_days", "distance_au", "color_hex"]
}
```

## Quality Criteria

- [ ] Virtualenv criado e ativado.
- [ ] Type hints em 100% do código.
- [ ] `pyright --strict` passa.
- [ ] Schemas exportados em `backend/contracts/`.
- [ ] Modo API: `uvicorn main:app` responde em /health.
- [ ] README com curls de exemplo.

## Veto Conditions

1. Arquivos escritos mesmo com `python_needed: false`.
2. Código sem type hints.
3. Dependência não-pinada em requirements.
