---
name: python-debugger
description: >
  Debug Python via breakpoint()/pdb e debugpy remoto (DAP). Breakpoints, stepping,
  post-mortem, inspeção de closures, attach a processos rodando.
type: tool_orchestration
tags: [development, debugging, code]
---

# Python Debugger

Três ferramentas por situação: `breakpoint()` + pdb (local), `python -m pdb` (sem edição), `debugpy` (remoto/headless).

**Core principle:** Comece com `breakpoint()`. É o mais barato que funciona.

## When to Use

- "Debug este script Python"
- "Preciso ver o estado das variáveis quando o erro acontece"
- "Post-mortem — quero inspecionar onde crashou"
- Testes Python falham e `--showlocals` não basta

**Auto-trigger:** Quando debugging Python requer inspeção de estado em runtime.

## Prerequisites

### Dependencies

```bash
# pdb — built-in, zero install
# Opcional: pip install debugpy  (para remote debug)
# Opcional: pip install remote-pdb  (pdb via rede)
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Script/teste** | Yes | Arquivo ou teste para debugar |
| **Linha/função alvo** | Recommended | Onde investigar |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: pdb Quick Reference

| Comando | Ação |
|---|---|
| `n` | next line (step over) |
| `s` | step into |
| `r` | return |
| `c` | continue |
| `l`/`ll` | list source |
| `w` | where (stack trace) |
| `p expr` | print expression |
| `interact` | REPL no scope atual |
| `b file:line` | set breakpoint |

## Phase 2: Receitas

### Local breakpoint

```python
def compute(x, y):
    result = some_helper(x)
    breakpoint()           # drops into pdb
    return result + y
```

### Debug pytest

```bash
pytest tests/test.py::test_name --pdb        # pdb on failure
pytest tests/test.py::test_name --trace       # pdb at start
pytest tests/test.py --showlocals --tb=long   # locals sem pdb
```

### Post-mortem

```bash
python -m pdb -c continue script.py  # pdb no crash
```

## Phase 3: Pitfalls

1. **pdb + pytest-xdist:** Silenciosamente não funciona. Usar `-p no:xdist`
2. **`breakpoint()` em CI:** Trava o processo. Nunca commitar.
3. **`PYTHONBREAKPOINT=0`:** Desabilita todos os breakpoints. Checar env.

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Estado variáveis** | Terminal output | pdb prompt |
| **Stack trace** | Backtrace | Terminal |

## Cost

| Component | Cost |
|---|---|
| pdb | Free (built-in) |
| debugpy | Free (pip) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Breakpoint não para** | Execução ignora | Checar PYTHONBREAKPOINT, xdist |
| **pdb em multi-thread** | Só debugga thread atual | Usar debugpy |

## Composability

**Receives data from:**
- `systematic-debugging` — hipótese direciona investigação
- `python-environment-management` — garante ambiente correto

**Feeds into:**
- `tdd-protocol` — bug encontrado → teste que reproduz

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Patterns** | `[OPERACIONAL]: python-debugger — [insight]` | `Usar -p no:xdist com pytest --pdb` |

## Quality Gate

- [ ] **Breakpoint atinge o alvo**
- [ ] **Stack trace mostra frame correto**
- [ ] **Cleanup:** Sem `breakpoint()` em código commitado
  ```bash
  rg -n 'breakpoint\(\)|set_trace\(' --type py
  ```

**If any check fails:** Verificar configuração e ambiente.
