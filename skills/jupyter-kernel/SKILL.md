---
name: jupyter-kernel
description: >
  Interaja com Jupyter notebooks via kernel ao vivo. Execute células, inspecione variáveis,
  edite conteúdo, e faça restart+run-all para verificação clean. Ideal para data science,
  análise exploratória e prototipagem interativa.
type: tool_orchestration
tags: [data, analytics, development]
---

# Jupyter Kernel

Controle notebooks Jupyter via terminal — execute células, inspecione variáveis, edite conteúdo.

**Core principle:** Notebooks são para exploração interativa. Use o kernel ao vivo, não edite JSON manualmente.

## When to Use

- "Execute este notebook"
- "Rode esta célula de análise"
- "Inspecione as variáveis do notebook"
- "Faça data analysis interativa"
- Qualquer trabalho com Jupyter notebooks

**Auto-trigger:** Quando o contexto envolve notebooks `.ipynb` ou data science interativa.

## Prerequisites

### Dependencies

```bash
pip install jupyterlab
# Verificar: jupyter lab --version
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Notebook** | Yes | Path do arquivo `.ipynb` |
| **Ação** | Yes | execute/variables/edit/restart |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

## Phase 1: Operações Básicas

### Executar Células

Execute código Python diretamente no kernel ao vivo do notebook.

### Inspecionar Variáveis

Liste variáveis disponíveis no namespace do kernel.

### Editar Células

Substitua ou delete células programaticamente.

### Restart + Run All

Para verificação clean, reinicie o kernel e execute todas as células.

## Practical Tips

1. **Primeiro execute após start pode dar timeout** — kernel precisa inicializar. Retry.
2. **Python do kernel = Python do JupyterLab** — pacotes devem estar no mesmo ambiente.
3. **Use --compact flag** — JSON output pode ser muito verboso.
4. **Para REPL puro**, crie um scratch.ipynb e use execute repetidamente.
5. **Timeouts generosos** (60+) para setup ou computação pesada.

## Phase N: Output

| Output | Format | Location |
|---|---|---|
| **Resultado de execução** | Text/JSON | Terminal |
| **Variáveis** | Tabela | Terminal |
| **Notebook atualizado** | `.ipynb` | Arquivo |

## Cost

| Component | Cost |
|---|---|
| JupyterLab | Free |
| Kernel execution | CPU/GPU local |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Timeout** | Execução não retorna | Retry ou aumentar --timeout |
| **Kernel crash** | Erro de conexão | Restart kernel |
| **Package missing** | ImportError | `pip install` no ambiente do Jupyter |

## Composability

**Receives data from:**
- `data-toolkit` — dados para análise exploratória
- `python-environment-management` — garante ambiente correto

**Feeds into:**
- `research-paper-writer` — resultados de notebooks para papers
- Visualizações e reports

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Notebooks úteis** | `[OPERACIONAL]: jupyter-kernel — [notebook] para [propósito]` | `analysis.ipynb para métricas de campanha` |

## Quality Gate

- [ ] **Kernel rodando e responsivo**
- [ ] **Todas as células executam sem erro**
- [ ] **Outputs salvos no notebook**

**If any check fails:** Restart kernel e re-executar.
