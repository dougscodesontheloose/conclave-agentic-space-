---
name: node-debugger
description: >
  Debug Node.js via --inspect e Chrome DevTools Protocol CLI. Breakpoints reais,
  step in/over/out, scope dumps, eval em frame pausado, CPU/heap profiles.
type: tool_orchestration
tags: [development, debugging, code]
---

# Node.js Debugger

Drive o inspector V8 do Node.js via terminal. Breakpoints reais, stepping, scope dumps, e eval em frames pausados.

**Core principle:** Use quando `console.log` não resolve em menos de 1 minuto.

## When to Use

- "Debug este script Node.js"
- "Preciso inspecionar variáveis em runtime"
- "O processo trava e não sei onde"
- Testes Node falham e o traceback não revela o problema

**Auto-trigger:** Quando debugging Node.js requer inspeção de estado em runtime.

## Prerequisites

### Dependencies

```bash
# node inspect — built-in, zero install
# Opcional: npm i -g chrome-remote-interface  (para automação CDP)
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Script/processo** | Yes | Arquivo ou PID para debugar |
| **Linha/função alvo** | Recommended | Onde colocar breakpoint |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Quick Reference — node inspect

```bash
node inspect path/to/script.js      # Lança pausado na primeira linha
node --inspect-brk script.js        # Inspector + pausa na primeira linha
```

| Comando | Ação |
|---|---|
| `c`/`cont` | continue |
| `n`/`next` | step over |
| `s`/`step` | step into |
| `o`/`out` | step out |
| `sb('file.js', 42)` | breakpoint na linha 42 |
| `sb('functionName')` | break ao chamar função |
| `bt` | backtrace (call stack) |
| `repl` | REPL no scope atual |
| `exec expr` | avaliar expressão |

## Phase 2: Attach a Processo Rodando

```bash
kill -SIGUSR1 <pid>                  # Habilita inspector
node inspect -p <pid>                # Attach
```

## Phase 3: Pitfalls Comuns

1. **`--inspect` vs `--inspect-brk`:** Sem `-brk`, script roda antes de você settar breakpoints
2. **Port collisions:** Default 9229. Use `--inspect=0` para porta aleatória
3. **Child processes:** `--inspect` no parent NÃO inspeciona filhos
4. **Segurança:** Nunca `--inspect=0.0.0.0:9229` em rede pública

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Estado das variáveis** | Terminal output | Exibido ao usuário |
| **Call stack** | Backtrace | Terminal |

## Cost

| Component | Cost |
|---|---|
| Ferramentas | Free (built-in) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Breakpoint não para** | Execução passa direto | Verificar `--inspect-brk`, attach timing |
| **Port em uso** | Erro ao iniciar | Usar porta diferente |

## Composability

**Receives data from:**
- `systematic-debugging` — hipótese direciona onde colocar breakpoints

**Feeds into:**
- `tdd-protocol` — bug encontrado → escrever teste que reproduz

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Patterns** | `[OPERACIONAL]: node-debugger — [insight]` | `Usar --inspect-brk para TypeScript` |

## Quality Gate

- [ ] **Breakpoint atinge o alvo**
- [ ] **Source listing mostra arquivo correto**
- [ ] **Cleanup pós-debug:** Sem breakpoints stale

**If any check fails:** Verificar configuração de inspector.
