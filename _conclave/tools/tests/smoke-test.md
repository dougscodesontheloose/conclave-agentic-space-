# Conclave Smoke Test

Run before any major update to the core runtime or Architect prompts.  
Pass = all blocking items (✦) checked. Warnings (◈) are non-blocking.

---

## 0. Static Validation (automated)

```bash
cd ~/Documents/Bancada/Conclave
python3 _conclave/tools/scripts/validate_conclave.py
```

- [ ] ✦ Exit code 0 (zero blocking failures)
- [ ] ◈ Zero warnings (or warnings are understood and acceptable)
- [ ] ✦ All core runtime files present
- [ ] ✦ All existing squads pass structural gates

**If any blocking failure:** stop. Fix before proceeding.

---

## 1. Architect — Create Squad (minimal flow)

**Input:** Use a simple, deterministic prompt to avoid variability.

> "Crie um squad de pesquisa simples: ele busca notícias sobre IA no Brasil e gera um resumo diário em Markdown."

**Steps to verify:**

### 1a. Discovery Phase
- [ ] ✦ Pergunta inicial aberta (não apresenta opções antes do usuário responder)
- [ ] ✦ Detecta domínio `research` silenciosamente
- [ ] ✦ Pergunta 1 por vez (nunca 2 perguntas juntas na mesma mensagem)
- [ ] ✦ Máximo 8 perguntas totais no flow
- [ ] ✦ Não pergunta sobre ferramentas (deve auto-detectar)
- [ ] ✦ Oferece opção de investigação (Step 5) com trade-off claro
- [ ] ✦ Apresenta summary com confirmação antes de escrever arquivo
- [ ] ✦ Escreve `squads/{code}/_build/discovery.yaml` após confirmação
- [ ] ◈ `discovery.yaml` tem todos os campos: squad_code, purpose, domain, company, language, context, investigation, target_formats

### 1b. Design Phase
- [ ] ✦ Lê `discovery.yaml`, `company.md`, `preferences.md`
- [ ] ✦ Executa Phase A (best-practices): consulta `_catalog.yaml` e lê apenas arquivos relevantes
- [ ] ✦ Executa Phase B (research): faz buscas web e compila research brief
- [ ] ✦ Apresenta design completo (agentes, pipeline, formatos) antes de construir
- [ ] ✦ Espera aprovação do usuário antes de continuar
- [ ] ✦ Escreve `squads/{code}/_build/design.yaml` após aprovação
- [ ] ◈ `design.yaml` tem campos: squad, agents, pipeline, research_brief, skills_installed

### 1c. Build Phase
- [ ] ✦ Gera `squad.yaml` com campos name, code, description, icon, skills, data, pipeline.steps
- [ ] ✦ Gera `squad-party.csv` com todos os agentes
- [ ] ✦ Gera todos os `.agent.md` com seções completas (Persona, Principles, etc.)
- [ ] ✦ Gera todos os arquivos de steps em `pipeline/steps/`
- [ ] ✦ Gera arquivos em `pipeline/data/` (research-brief.md, domain-framework.md, etc.)
- [ ] ✦ Step-00 existe e é atribuído ao `pietro-prompt` agent
- [ ] ✦ Valida Gates 0–3 e reporta resultado
- [ ] ✦ Gate 0: todos os nomes de agentes têm exatamente 2 palavras
- [ ] ✦ Gate 1: todos os `.agent.md` têm seções mínimas
- [ ] ✦ Gate 2: todos os steps têm Context Loading, Instructions, Output Format, Veto Conditions
- [ ] ✦ Gate 3: pipeline é coerente (outputFile → inputFile, checkpoints nos lugares certos)
- [ ] ✦ Apresenta summary final com `/conclave run {code}` como próximo passo

### 1d. Post-creation
- [ ] ✦ Rodar `python3 _conclave/tools/scripts/validate_conclave.py` novamente
- [ ] ✦ Novo squad passa todos os gates sem erros bloqueantes
- [ ] ✦ Intention matrix atualizada (`intention_matrix.json` contém o novo squad)
- [ ] ✦ Audit log tem entrada `squad.created` em `_conclave/runtime/logs/audit.jsonl`

---

## 2. Pipeline Runner — Executar Squad

**Squad de teste:** usar o squad criado em T1 ou qualquer squad existente.

```
/conclave run {code}
```

- [ ] ✦ Carrega squad.yaml, squad-party.csv, todos os agent files
- [ ] ✦ Carrega company.md e preferences.md
- [ ] ✦ Carrega squad memories.md
- [ ] ✦ Step-00 (refinement) executa inline e pede confirmação
- [ ] ✦ Steps subagent são despachados como background task (não bloqueiam)
- [ ] ✦ Checkpoints usam `AskUserQuestion` (nunca texto plano)
- [ ] ✦ Pipeline respeita a ordem dos steps declarada em squad.yaml
- [ ] ✦ Outputs são salvos em `output/{run_id}/` (não em `pipeline/data/`)
- [ ] ✦ `runs.md` é atualizado com o run
- [ ] ✦ Audit log tem entradas `run.started` e `run.completed`

---

## 3. Architect — Edit Squad

```
/conclave edit {code}
```

- [ ] ✦ Lista squads disponíveis (ou confirma o squad se especificado)
- [ ] ✦ Cria backup do arquivo antes de reescrever (`.bak-YYYYMMDD-HHmmss`)
- [ ] ✦ Anuncia backup ao usuário ("🛟 Backup saved: ...")
- [ ] ✦ Aplica mudança solicitada sem recriar todo o squad do zero
- [ ] ✦ Apresenta summary das mudanças antes de confirmar
- [ ] ✦ Roda reindex após edição
- [ ] ✦ Audit log tem entrada `squad.edited`

---

## 4. Fluxo de Memória e Contexto

- [ ] ✦ `company.md` é lido em toda criação/execução de squad
- [ ] ✦ `preferences.md` define idioma de output corretamente
- [ ] ✦ `global-preferences.md` serve como fallback quando preferences.md não define o campo
- [ ] ◈ Squad memory (`memories.md`) é atualizada ao final de um run completo

---

## 5. Overwrite Protection

- [ ] ✦ Tentar editar um squad com arquivo existente: backup é criado antes de sobrescrever
- [ ] ✦ Backup usa timestamp: `{file}.bak-YYYYMMDD-HHmmss`
- [ ] ✦ Arquivo original não é perdido se o edit falhar a meio

---

## 6. Checklist de Regressão Pós-Update

Rodar após qualquer mudança em arquivos de `_conclave/core/`:

```bash
python3 _conclave/tools/scripts/validate_conclave.py
```

- [ ] ✦ Zero blocking failures
- [ ] ✦ Todos os squads existentes ainda passam Gate 1 (agents) e Gate 2 (steps)
- [ ] ✦ Intention matrix ainda é JSON válido
- [ ] ✦ Nenhum arquivo de squad foi alterado inadvertidamente (verificar via `git diff` ou timestamps)

---

## Notas

- **Frequência:** Executar T0 (estático) antes de qualquer PR/merge em `_conclave/core/`.
- **Frequência:** Executar T1–T5 (dinâmico) antes de releases maiores do Conclave.
- **Falha em T0 = bloqueante.** Nenhuma outra etapa deve ser executada antes de corrigir.
- **Falha em T1–T5 = investigar causa raiz.** Não prosseguir com o update que causou a falha.
