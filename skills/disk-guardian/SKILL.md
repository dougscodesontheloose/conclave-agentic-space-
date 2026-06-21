---
name: Disk Guardian
description: Skill de auto-higiene e zeladoria do sistema Conclave.
type: prompt
tags: [system, maintenance, quality-assurance]
---

# Skill: Disk Guardian

**Core principle:** Sistemas resilientes assumem a falha como padrão e a recuperação como regra.


Esta skill permite que o Conclave mantenha sua própria casa limpa. Ela deve ser invocada periodicamente ou após grandes atualizações de sistema para consolidar o diretório e remover lixo digital.

## Ações de Zeladoria

### 1. Limpeza de Backups (.bak)
O sistema Conclave cria backups automáticos antes de cada edição. Com o tempo, esses arquivos se acumulam.
*   **Ação:** Executar `python3 _conclave/tools/scripts/disk_guardian.py`.
*   **Resultado:** Remoção de arquivos `.bak-*` com mais de 7 dias e geração de um relatório de limpeza.

### 2. Higiene de Outputs
Diretórios de `output/` de squads antigos podem ocupar espaço desnecessário.
*   **Ação:** Verificar se existem pastas de output sem atividade nos últimos 30 dias.
*   **Recomendação:** Sugerir ao usuário o arquivamento (`zip`) ou deleção dessas pastas.

### 3. Verificação de Integridade
*   **Ação:** Validar se todos os arquivos `.agent.md` possuem os metadados obrigatórios.
*   **Ação:** Verificar se o `intention_matrix.json` está sincronizado com a pasta `squads/`.

## Relatório de Limpeza
Ao final de cada ativação do Disk Guardian, apresente ao usuário um resumo:
- Quantos arquivos foram removidos.
- Espaço total recuperado (KB/MB).
- Status de integridade dos squads.

## Regras de Ouro
- NUNCA delete arquivos de fonte (`.py`, `.md`, `.json`, `.yaml`) que não sejam explicitamente backups (`.bak`).
- Sempre informe o usuário ANTES de rodar uma limpeza profunda em pastas de output.
- O relatório deve ser salvo em `_conclave/runtime/logs/disk_guardian_report.md`.


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

Use `Disk Guardian` when you need to:
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
| **Key findings** | `[OPERACIONAL]: disk-guardian — [finding]` | `[OPERACIONAL]: disk-guardian — Apify scraper returned 0 results for domain X, switched to direct mode` |
| **Parameter tuning** | `[OPERACIONAL]: disk-guardian — [param] works better as [value]` | `[OPERACIONAL]: disk-guardian — --max-results 50 is optimal for G2 (beyond 50 = mostly duplicates)` |
| **Strategic insights** | `[ESTRATÉGICO]: disk-guardian — [insight]` | `[ESTRATÉGICO]: disk-guardian — Competitor X has no case studies page, vulnerability for battlecard` |

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

