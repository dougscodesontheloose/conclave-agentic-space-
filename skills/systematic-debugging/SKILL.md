---
name: systematic-debugging
description: >
  Protocolo rigoroso de 4 fases para isolamento de falhas e correção de bugs baseada em evidências.
  Iron Law: NENHUM FIX SEM ROOT CAUSE INVESTIGATION. Inclui a "Regra de Três" e
  escalation para problemas arquiteturais. Baseado no framework Superpowers.
type: playbook
tags: [development, quality-assurance, debugging, superpowers]
---

# Systematic Debugging (Superpowers Edition)

Random fixes desperdiçam tempo e criam novos bugs. No Conclave, seguimos a abordagem de engenharia rigorosa para garantir que cada correção seja definitiva.

**Core principle:** SEMPRE encontre a causa raiz antes de tentar correções. Fix de sintoma é uma falha de engenharia.

## When to Use

- Qualquer comportamento inesperado ou erro no código.
- Test failures ou inconsistências de ambiente.
- Quando a solução parece "óbvia" mas não foi testada (red flag).
- Quando já houve tentativas de correção que falharam.

**Auto-trigger:** Ativado automaticamente ao detectar um erro de execução, falha de teste ou report de bug.

## Prerequisites

### Dependencies

Nenhuma. Pure reasoning skill + ferramentas de inspeção nativas (`git`, `grep`, `debugger`).

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| **Sintoma** | Yes | Descrição do erro, log ou stack trace |
| **Contexto** | Recommended | Código relacionado e mudanças recentes |

## Phase 0: Intake

Antes de investigar, colete os artefatos de erro:

1.  **Qual o log de erro exato?** (Copie e cole o stack trace completo).
2.  **O erro é reprodutível?** (Quais os passos exatos para dispará-lo?).
3.  **O que mudou recentemente no código?**

## Phase 1: Root Cause Investigation (The Iron Law)

> **NENHUM FIX SEM INVESTIGAÇÃO DE CAUSA RAIZ PRIMEIRO.**

### Step 1: Análise de Stack Trace
Não ignore avisos. Note números de linha, caminhos de arquivo e mensagens específicas.

### Step 2: Rastreio de Dados
Identifique onde o dado incorreto entra no sistema. Siga o fluxo upstream até a fonte.

### Step 3: Instrumentação (se necessário)
Adicione logs temporários para verificar o estado entre componentes.
- `INPUT LOG`: O que entra no componente.
- `OUTPUT LOG`: O que sai.

---

## Phase 2: Pattern Analysis

### Step 2A: Comparação com Referência
Localize código similar que *funciona*. O que há de diferente entre o funcional e o quebrado?

---

## Phase 3: Hypothesis & Testing (Método Científico)

### Step 3A: Uma Variável por Vez
Forme uma hipótese: "Acho que X causa Y porque Z". Teste fazendo a MENOR mudança possível. Se falhar, desfaça e tente outra hipótese. **NUNCA acumule fixes.**

---

## Phase 4: Implementation & Verification

### Step 4A: Teste de Regressão
Escreva um teste que reproduz o erro. Ele deve FALHAR agora e PASSAR após o fix.

### Step 4B: Implementação Definitiva
Corrija a causa raiz.

---

## Rule of Three (A Regra de Três)

Conte as tentativas de fix:
1.  **Falha 1**: Re-analise a investigação.
2.  **Falha 2**: Re-leia toda a documentação e contratos de API.
3.  **Falha 3 (HARD STOP)**: Pare tudo. Isso indica um **problema arquitetural**. Informe o usuário e reavalie o design.

---

## Phase N: Output

### Output Format

| Output | Format | Location |
| --- | --- | --- |
| **Análise de Causa Raiz** | Markdown | Exibido ao usuário |
| **Fix Aplicado** | Code Changes | Arquivos do projeto |
| **Teste de Regressão** | Arquivo de Teste | Pasta `tests/` |

## Cost

| Component | Cost |
| --- | --- |
| LLM reasoning | Free (incluído na sessão) |

## Error Handling

| Failure Mode | Detection | Recovery |
| --- | --- | --- |
| **Bug não reprodutível** | Não consegue disparar o erro | Coletar mais logs de runtime |
| **3+ fixes falharam** | Contador de tentativas atinge 3 | Trigger Hard Stop e reavaliar arquitetura |

## Composability

**Receives data from:**
- Qualquer agente ou ferramenta que encontre um erro.

**Feeds into:**
- `tdd-protocol` — Garante que o fix seja testado.
- `code-review` — Valida a qualidade do fix.

## Memory & Learning

| What to Save | Format | Example |
| --- | --- | --- |
| **Root Cause Insight** | `[OPERACIONAL]: systematic-debugging — [bug] causado por [causa]` | `Crash causado por race condition no cache` |
| **Patterns** | `[OPERACIONAL]: systematic-debugging — Pattern de erro detectado em [módulo]` | `Erros de off-by-one frequentes em pagination.py` |

## Quality Gate

- [ ] Causa raiz identificada e documentada.
- [ ] Teste de regressão criado e passando.
- [ ] **A Regra de Três foi respeitada.**
- [ ] Nenhum código "tentativo" deixado no sistema.
