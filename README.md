# Conclave

Crie squads de agentes de IA que trabalham juntos — direto do seu IDE.

## Como Usar

Instale a dependência do runtime:

```bash
python3 -m pip install -r requirements.txt
```

Abra esta pasta no seu IDE e digite:

```
/conclave
```

Isso abre o menu principal. De lá você pode criar squads, executá-los e mais.

### 🌐 Usar o Conclave em Qualquer Pasta (Modo Híbrido)

O Conclave roda em **modo híbrido**: um runtime global atende qualquer projeto, e cada pasta mantém seu próprio contexto (empresa, preferências, squads).

**Ativar em uma nova pasta:**

```
cd ~/Documents/MeuProjeto
/conclave init
```

Isso cria um `_conclave/` local com memória própria, sem duplicar o runtime. O core, o catálogo de skills e as preferências globais continuam vindo de `~/.conclave/` (symlinks para este repositório, que é o "hub").

- **Runtime compartilhado**: `~/.conclave/core/`, `~/.conclave/skills_catalog/`
- **Contexto local**: `./_conclave/state/memory/company.md`, `./squads/`, `./skills/`
- **Cascata de preferências**: projeto > global > padrão do agente

Use `/conclave where` em qualquer pasta para ver os caminhos resolvidos.

---

### 🏛️ Fundamentos do Sistema (Motor-Agnóstico)

O Conclave opera sobre três documentos fundacionais herdados por todo agente, independentemente do motor que o executa (Claude, GPT, Gemini, modelos locais):

| Documento | Domínio | Descrição |
|---|---|---|
| [`_conclave/core/charter.md`](_conclave/core/charter.md) | **Conduta** | As Sete Honestidades, quatro Hard Constraints, protocolo de recusa, Dual Newspaper Test. |
| [`_conclave/core/security.policy.md`](_conclave/core/security.policy.md) | **Dados** | SafeGuard: classificação de privacidade, Hard Veto, defesa contra prompt injection. |
| [`_conclave/core/soul.md`](_conclave/core/soul.md) | **Missão** | Manifesto do Soma Digital — os sete pilares do Conclave. |

**Charter governa a fala; SafeGuard governa os dados. Os dois são co-extensivos — nenhum sobrepõe o outro.**

Use `/conclave charter` para ler o código de conduta a qualquer momento.

---

### 💻 IDE Setup (Frictionless)

Este projeto já vem pré-configurado para **VS Code** e **Cursor**:
- **Configurações Universais**: `.editorconfig` garante o estilo de código correto em qualquer IDE.
- **Extensões Recomendadas**: Ao abrir no VS Code/Cursor, você receberá sugestões das melhores ferramentas.
- **Comandos Rápidos**: Use `Run Task` (Cmd+Shift+P > Tasks: Run Task) para acessar comandos do Conclave sem digitar.
- **IA Otimizada**: Regas para a IA do Cursor estão em `.cursorrules`.

---

Você também pode ser direto — descreva o que quer em linguagem natural:

```
/conclave crie um squad para escrever posts no LinkedIn sobre IA
/conclave execute o squad meu-squad
```

## Criar um Squad

Digite `/conclave` e escolha "Criar squad" no menu, ou seja direto:

```
/conclave crie um squad para [o que você precisa]
```

O Arquiteto fará algumas perguntas, projetará o squad e configurará tudo automaticamente.

## Executar um Squad

Digite `/conclave` e escolha "Executar squad" no menu, ou seja direto:

```
/conclave execute o squad <nome-do-squad>
```

O squad executa automaticamente, pausando apenas nos checkpoints de decisão.

## Quando Rodar — Ativando o Auto-Aprendizado

O Conclave tem um sistema de auto-aprendizado (Learning Stack — Ondas 4-8) que só "acorda" quando squads são executados via `/conclave run`. Editar squads, instalar skills ou rodar o Architect **não alimenta** o loop. Só runs reais alimentam.

### O que ativa cada coisa

| Ação no CLI | Streams alimentados | GAIA observers ativados |
|---|---|---|
| `/conclave run <squad>` | `_conclave/state/memory/skill-signals.jsonl` (D4), `squads/{nome}/_memory/squad-signals.jsonl` (D3), `gossip.jsonl` (D4.5 ARTEMIS, se squad tem `domain:`), `skill-candidates.jsonl` (D5, após 3 runs `quality:good`), `user-model.md` (D6, a cada 3 runs cumulativos) | POSEIDON, ARTEMIS, HEPHAESTUS |
| `/conclave tide` | (lê tudo acima) | POSEIDON gera `_memory/tide-reports/` |
| `/conclave curate` | (lê `_memory/`) | APOLLO gera `_memory/curation-reports/` |
| `/conclave forge` | (lê candidates) | HEPHAESTUS propõe skills/templates |
| `/conclave create` ou `/conclave edit` | `_conclave/runtime/logs/audit.jsonl` apenas | (nenhum — fase Architect) |

### Mínimo viável pra fechar o loop

1. **Rodar 1 squad pelo menos uma vez** — qualquer um. Isso cria o primeiro `steps.jsonl` + emite o primeiro D3/D4 signal.
2. **Rodar 3+ vezes com `quality: good`** o mesmo squad para D5 propor candidato a skill.
3. **Rodar `/conclave tide` semanalmente** — POSEIDON detecta padrões só com volume mínimo (~5+ runs).
4. **Rodar `/conclave curate` mensalmente** — APOLLO detecta dedup/staleness em `_memory/`.

### Diagnóstico rápido (se algo "não tá fechando o loop")

```bash
# Streams vazios? Ainda não houve run que disparasse os hooks
wc -l _conclave/state/memory/*.jsonl

# Nenhum run completo? Verificar se pipeline reachou D3
find squads -name "steps.jsonl"

# Audit só tem eventos de architect? Confirma: não rodou squad ainda
grep '"event"' _conclave/runtime/logs/audit.jsonl | sort -u
```

**Regra de ouro:** o sistema só aprende com o que faz. Editar squads é desenvolvimento; rodar squads é produção. Só produção alimenta a memória estruturada.

---

## Escritório Virtual

O Escritório Virtual é uma interface visual 2D que mostra seus agentes trabalhando em tempo real.

**Passo 1 — Gere o dashboard** (no seu IDE):

```
/conclave dashboard
```

**Passo 2 — Sirva localmente** (no terminal):

```bash
npx serve squads/<nome-do-squad>/dashboard
```

**Passo 3 —** Abra `http://localhost:3000` no seu navegador.

---

# Conclave (English)

Create AI squads that work together — right from your IDE.

## How to Use

Install the runtime dependency:

```bash
python3 -m pip install -r requirements.txt
```

Open this folder in your IDE and type:

```
/conclave
```

This opens the main menu. From there you can create squads, run them, and more.

### 🌐 Use Conclave in Any Folder (Hybrid Mode)

Conclave runs in **hybrid mode**: one global runtime serves any project, while each folder keeps its own context (company, preferences, squads).

**Activate in a new folder:**

```
cd ~/Documents/MyProject
/conclave init
```

This creates a local `_conclave/` with its own memory, without duplicating the runtime. Core, skills catalog, and global preferences continue to come from `~/.conclave/` (symlinked into this repository, the "hub").

- **Shared runtime**: `~/.conclave/core/`, `~/.conclave/skills_catalog/`
- **Local context**: `./_conclave/state/memory/company.md`, `./squads/`, `./skills/`
- **Preference cascade**: project > global > agent default

Run `/conclave where` in any folder to see the resolved paths.

---

### 🏛️ System Foundations (Motor-Agnostic)

Conclave operates on three foundational documents inherited by every agent, regardless of which engine runs them (Claude, GPT, Gemini, local models):

| Document | Domain | Description |
|---|---|---|
| [`_conclave/core/charter.md`](_conclave/core/charter.md) | **Conduct** | Seven Honesties, four Hard Constraints, refusal protocol, Dual Newspaper Test. |
| [`_conclave/core/security.policy.md`](_conclave/core/security.policy.md) | **Data** | SafeGuard: privacy classification, Hard Veto, prompt injection defense. |
| [`_conclave/core/soul.md`](_conclave/core/soul.md) | **Mission** | Digital Soma manifesto — Conclave's seven pillars. |

**Charter governs speech; SafeGuard governs data. Both are co-extensive — neither overrides the other.**

Use `/conclave charter` to read the code of conduct at any time.

---

You can also be direct — describe what you want in plain language:

```
/conclave create a squad for writing LinkedIn posts about AI
/conclave run my-squad
```

## Create a Squad

Type `/conclave` and choose "Create squad" from the menu, or be direct:

```
/conclave create a squad for [what you need]
```

The Architect will ask a few questions, design the squad, and set everything up automatically.

## Run a Squad

Type `/conclave` and choose "Run squad" from the menu, or be direct:

```
/conclave run the <squad-name> squad
```

The squad runs automatically, pausing only at decision checkpoints.

## Virtual Office

The Virtual Office is a 2D visual interface that shows your agents working in real time.

**Step 1 — Generate the dashboard** (in your IDE):

```
/conclave dashboard
```

**Step 2 — Serve it locally** (in terminal):

```bash
npx serve squads/<squad-name>/dashboard
```

**Step 3 —** Open `http://localhost:3000` in your browser.
