---
name: Python Environment Management
description: Configura e gerencia ambientes Python (uv/venv) de forma saudável, estável e autônoma sem perda de tempo com setup.
type: tool_orchestration
tags: [system, development, automation]
---

# Skill: Python Environment Management

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill atua na raiz do projeto (ou no diretório atual do squad) para garantir que qualquer operação envolvendo Python rode dentro de um ambiente isolado, estável e reproduzível. Ela é crucial para preparar o terreno para upgrades e novos scripts no ecossistema Conclave.

## Protocolo Zero-Setup

Sempre que você precisar executar um script Python, instalar dependências ou auditar um repositório baseado em Python, siga este fluxo rigorosamente:

1. **Detecção:**
   - Verifique se já existe um diretório de ambiente virtual (como `.venv` ou `venv`).
   - Verifique a presença de `pyproject.toml`, `requirements.txt` ou `uv.lock`.

2. **Criação e Isolamento (se não existir):**
   - Priorize o uso de `uv` (extremamente rápido e confiável). Se o sistema não tiver `uv`, caia para o módulo padrão `venv`.
   - Crie o ambiente: `uv venv` (ou `python3 -m venv .venv`).
   - **Nunca** modifique o ambiente global do sistema.

3. **Gerenciamento de Dependências:**
   - Instale as dependências usando o ambiente virtual criado.
   - Usando `uv`: `uv pip install -r requirements.txt` ou `uv sync`.
   - Se estiver adicionando um novo pacote: `uv pip install <pacote>` e, em seguida, atualize o `requirements.txt` (via `uv pip freeze > requirements.txt` ou ferramentas equivalentes).

4. **Execução Isolada:**
   - Para executar scripts, NÃO ative o ambiente virtual usando comandos `source` no shell bash do agente (pois a ativação não persiste entre chamadas independentes).
   - Ao invés disso, chame o interpretador Python DIRETAMENTE do ambiente virtual ou use ferramentas que abstraem isso (como `uv run`).
   - Exemplo: `./.venv/bin/python script.py` ou `uv run script.py`.

5. **Self-Healing (Auto-reparo):**
   - Se ocorrer um erro de `ModuleNotFoundError` durante a execução, intercepte a falha. Instale a dependência que falta no `.venv`, atualize os arquivos de dependência e tente a execução novamente sem notificar o usuário (apenas documente nos logs do agente).


## Prerequisites


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Escopo** — Quais arquivos ou diretórios serão afetados?
2. **Objetivo** — Qual o estado final desejado?
3. **Restrições** — Há limitações de dependências ou retrocompatibilidade?

### Environment Variables

```env
APIFY_API_TOKEN=required_for_scraping
```

### Dependencies

Requer ambiente de execução padrão do Conclave.

## When to Use

Use `Python Environment Management` when you need to:
- Maintain system health and operational quality
- Apply development best practices
- Support the infrastructure that other skills depend on

**Auto-trigger:** This skill should be loaded automatically when the user's request matches its description.


## Inputs

| Input | Required | Description |
|---|---|---|
| **Target scope** | Varies | Files, directories, or codebase to operate on |
| **Configuration** | No | Settings or preferences for the operation |


## Output Format

| Output | Format | Location |
|---|---|---|
| **Status report** | Markdown or terminal | Displayed to user |
| **Changes applied** | Log | Inline in response |


## Cost

| Component | Cost |
|---|---|
| Apify actor runs | ~$0.01–0.05 per run (varies by actor) |
| Apify free tier | $5/month included |
| LLM reasoning | Free (included in agent session) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Dependency not installed** | ImportError or command not found | Log exact install command needed. Do not attempt auto-install without user consent |
| **Permission denied** | OS permission error | Log the specific path and required permission. Suggest fix command |
| **Configuration missing** | Required config file not found | Provide template with defaults. Ask user to fill required fields |
| **Disk space insufficient** | Write failure or quota error | Run cleanup suggestions. Warn before large operations |

**Principle:** System skills must be self-diagnosing. Every failure should include the exact fix command.


## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Key findings** | `[OPERACIONAL]: python-environment-management — [finding]` | `[OPERACIONAL]: python-environment-management — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: python-environment-management — [param] works better as [value]` | `[OPERACIONAL]: python-environment-management — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: python-environment-management — [insight]` | `[ESTRATÉGICO]: python-environment-management — Competitor X has no case studies page, vulnerability for battlecard` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry


## Quality Gate

Before delivering the final output, verify:

- [ ] **Output completeness:** All required fields/sections are populated
- [ ] **No silent failures:** Every step that was attempted has a status in the output
- [ ] **Format valid:** Output matches the documented schema
- [ ] **User checkpoint:** Present results summary to user before finalizing

**If any check fails:** Report the specific gap and ask user how to proceed.

