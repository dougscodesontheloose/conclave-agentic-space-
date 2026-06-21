---
privacy: internal
domain: conclave-learning
status: draft
version: 0.1.0
last_validated: 2026-06-05
---

# Session Log Schema

Contrato para registrar sessoes de aprendizado em JSONL. O log deve ser leve,
consultavel e suficiente para orientar a proxima sessao.

## Arquivo recomendado

```text
{learning-environment}/_conclave/_memory/session-log.jsonl
```

## Registro JSONL

Cada linha deve ser um objeto JSON independente:

```json
{
  "ts": "YYYY-MM-DDTHH:MM:SSZ",
  "session_id": "YYYY-MM-DD-environment-short-id",
  "environment": "environment-code",
  "mode": "guided-session",
  "duration_min": 20,
  "focus": ["reading", "chunking"],
  "input_refs": ["MAT-0001", "SRC-0003"],
  "activities": ["read", "listen", "review"],
  "evidence": ["recognized 8 recurring chunks"],
  "metrics": {
    "estimated_comprehension": 0.75,
    "repetitions": 2,
    "items_added_to_srs": 5
  },
  "decision": "repeat",
  "loop_update": "reduce text length next session",
  "privacy": "internal",
  "quality": "pending"
}
```

## Campos obrigatorios

- `ts`
- `session_id`
- `environment`
- `mode`
- `focus`
- `evidence`
- `decision`
- `privacy`

## Valores recomendados

### mode

- `plan`
- `guided-session`
- `review`
- `assessment`
- `curation`
- `inventory`

### decision

- `repeat`
- `advance`
- `reduce`
- `intensify`
- `hold`
- `archive`

### quality

- `pending`
- `good`
- `partial`
- `miss`

## Regras

- Nao salvar transcricao bruta no log principal.
- Nao salvar OCR integral, prints, dados pessoais ou arquivos externos crus.
- Usar `input_refs` para apontar para materiais, fontes ou artefatos locais.
- `evidence` deve ser observavel, nao interpretacao vaga.
- `loop_update` deve ser curto e acionavel.
- Se a sessao envolver conteudo externo, registrar a fonte e aplicar SafeGuard
  antes de qualquer uso por agentes.

