---
name: creative-ideation
description: >
  Gere ideias de projetos através de constraints criativos. Constraint + direção = criatividade.
  Funciona para código, arte, hardware, escrita, ferramentas, e qualquer coisa que pode ser feita.
type: playbook
tags: [creative, strategy, content]
---

# Creative Ideation

Gere ideias de projetos através de constraints criativos.

**Core principle:** Constraint + direção = criatividade. Sem nenhum dos dois, não há criatividade.

## When to Use

- "Quero construir algo"
- "Me dê uma ideia de projeto"
- "Estou sem inspiração"
- "O que devo fazer?"
- Qualquer variante de "tenho ferramentas mas sem direção"

**Auto-trigger:** Quando o usuário demonstra vontade de criar sem direção clara.

## Prerequisites

### Dependencies

Nenhuma. Pure reasoning skill.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Domínio** | No | Código, arte, marketing, hardware |
| **Mood** | No | Prático, weird, bonito, desafiador |


## Phase 0: Intake

Perguntas obrigatórias antes da execução:

1. **Audiência** — Para quem estamos escrevendo/criando?
2. **Tom de Voz** — Qual a diretriz de marca a ser usada?
3. **Canal** — Onde isso será publicado?

## Phase 1: Escolher Constraint

### Para Desenvolvedores

- **Solve your own itch:** Ferramenta que desejou ter esta semana. <50 linhas. Ship hoje.
- **Automate the annoying:** Parte mais tediosa do workflow. Automatize.
- **CLI que deveria existir:** `git undo-that-thing`. `docker why-is-this-broken`. Agora construa.
- **Nothing new except glue:** Tudo de APIs e libs existentes. Contribuição original = como conecta.
- **Subtract:** Quanto pode remover antes de quebrar? Strip ao mínimo essencial.

### Para Makers & Artistas

- **Blatantly copy:** Recrie algo admirado from scratch. Aprendizado está no gap.
- **One million of something:** 1M é muito e pouco ao mesmo tempo. O que fica interessante em escala?
- **Make something that dies:** Website que perde feature por dia. Chatbot que esquece.

### Para Qualquer Um

- **Text is the universal interface:** Só palavras. Entrada e saída.
- **Start at the punchline:** Frase engraçada. Trabalhe backwards para torná-la real.
- **Hostile UI:** Intencionalmente doloroso de usar. Password com 47 condições.

### Matching

| Usuário diz | Constraint |
|---|---|
| "Quero construir algo" (sem direção) | Random |
| "Estou aprendendo [X]" | Copy something, Automate |
| "Quero algo weird" | Hostile UI, Start at punchline |
| "Quero algo útil" | Solve your itch, CLI that should exist |
| "Quero algo bonito" | Do a lot of math, One million |
| "Estou burnout" | High concept low effort |

## Phase N: Output

### Output Format

```markdown
## Constraint: [Nome]
> [O constraint, uma frase]

### Ideas

1. **[One-line pitch]**
   [2-3 frases: o que construir e por que é interessante]
   ⏱ [weekend/week/month] • 🔧 [stack]

2. **[One-line pitch]**
   [2-3 frases]
   ⏱ ... • 🔧 ...

3. **[One-line pitch]**
   [2-3 frases]
   ⏱ ... • 🔧 ...
```

Após o usuário escolher, comece a construir.

## Cost

| Component | Cost |
|---|---|
| Reasoning | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **Ideias genéricas** | Sem especificidade | Re-gerar com constraint mais forte |
| **Scope muito grande** | >1 mês estimado | Dividir ou simplificar |

## Composability

**Feeds into:**
- `development-planning` — ideia escolhida vira plano
- `campaign-brief-generator` — ideia de campanha vira brief

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Preferências** | `[ESTRATÉGICO]: creative-ideation — Usuário prefere [tipo]` | `Usuário prefere projetos CLI práticos` |

## Quality Gate

- [ ] **3 ideias concretas com stack definido**
- [ ] **Estimativa de tempo realista**
- [ ] **Constraint claramente conectado às ideias**

**If any check fails:** Re-gerar com melhor constraint matching.
