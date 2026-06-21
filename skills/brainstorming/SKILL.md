---
name: brainstorming
description: >
  Processo de diálogo Socrático para refinar ideias brutas em documentos de design sólidos.
  Impede o "pular para o código" garantindo que restrições e objetivos estejam claros.
type: playbook
tags: [creative, strategy, design, planning, brainstorming]
---

# Brainstorming (Superpowers Style)

Não comece a construir até entender o *porquê*, o *quem* e o *como*. O objetivo do brainstorm não é apenas gerar ideias, mas refinar uma ideia até que ela possa ser transformada em um plano de execução.

**Core principle:** Um diálogo Socrático precede qualquer plano ou código.

## When to Use

- "Tenho uma ideia de [app/feature/ferramenta]"
- "Como eu poderia resolver [problema]?"
- Antes de qualquer `writing-plans` para features novas ou mudanças arquiteturais.
- Quando a solicitação do usuário é vaga ou ambiciosa demais.

**Auto-trigger:** Quando o usuário propõe uma feature ou projeto sem uma especificação clara ou análise de trade-offs.

## Prerequisites

### Dependencies

Nenhuma. Pure reasoning skill.

## Inputs

| Input | Required | Description |
| --- | --- | --- |
| **Ideia Bruta** | Yes | O conceito inicial ou problema a ser resolvido |
| **Contexto do Codebase** | Recommended | Código existente, stack e padrões do projeto |
| **Público-alvo** | Recommended | Quem usará a solução |

## Phase 0: Intake

Antes de começar o diálogo, verifique se temos o contexto básico. Se não, pergunte:

1.  **Qual o problema central que estamos tentando resolver?**
2.  **Existem restrições técnicas (stack, libs, ambiente)?**
3.  **Qual o prazo ou nível de fidelidade esperado para o MVP?**

## Phase 1: Diálogo Socrático

**Regra de Ouro:** Faça perguntas, não dê apenas respostas.

### Step 1: Clarificação de Escopo
Faça de **1 a 3 perguntas** clarificadoras por vez. Não sobrecarregue o usuário.
*Exemplos:*
- "Quem é o usuário principal desta ferramenta?"
- "O que acontece se o sistema estiver offline?"

### Step 2: Descoberta de Edge Cases
Questione o que acontece quando as coisas dão errado ou quando os limites são atingidos.

## Phase 2: Proposta de Abordagens

Apresente de 2 a 3 caminhos possíveis com trade-offs claros.

### Step 2A: Abordagem Minimalista (YAGNI)
- **Foco:** Velocidade e simplicidade.
- **Prós:** Ship rápido, baixo custo de manutenção.
- **Contras:** Menos escalável, pode precisar de refactor futuro.

### Step 2B: Abordagem Robusta
- **Foco:** Escalabilidade e boas práticas.
- **Prós:** Duradouro, fácil de estender.
- **Contras:** Maior tempo de desenvolvimento inicial.

## Phase 3: Consolidação em Design Doc

Uma vez que o caminho foi escolhido, gere o documento.

### Step 3A: Criação do DESIGN.md
Crie ou atualize o arquivo de design (ex: `docs/design/feature.md`).

## Phase N: Output

### Output Format

| Output | Format | Location |
| --- | --- | --- |
| **Design Doc** | Markdown | `docs/design/` ou `DESIGN.md` |
| **Resumo de Decisão** | Markdown Table | Exibido ao usuário |

### Output Template

```markdown
# DESIGN: [Feature Name]

## Problem Statement
[O que estamos resolvendo]

## Proposed Solution
[Descrição técnica da abordagem escolhida]

## Success Criteria
[Como saberemos que funciona]

## Out of Scope
[O que não vamos fazer agora]
```

## Cost

| Component | Cost |
| --- | --- |
| LLM reasoning | Free (incluído na sessão) |

## Error Handling

| Failure Mode | Detection | Recovery |
| --- | --- | --- |
| **Indecisão do usuário** | Múltiplas rodadas sem escolha | Sugerir a abordagem Minimalista como default |
| **Escopo muito amplo** | Design doc > 200 linhas | Dividir a feature em sub-features e reiniciar o brainstorm |

## Composability

**Receives data from:**
- Intenção direta do usuário.

**Feeds into:**
- `writing-plans` — Transforma o Design Doc em tarefas.
- `development-planning` — Alternativa para quebra de tarefas.

## Memory & Learning

| What to Save | Format | Example |
| --- | --- | --- |
| **Decisões de Design** | `[ESTRATÉGICO]: brainstorming — [feature] decidida com [abordagem]` | `Auth decidido com JWT vs Session` |
| **Preferências** | `[OPERACIONAL]: brainstorming — Usuário prefere [tipo de solução]` | `Usuário prefere soluções serverless` |

## Quality Gate

- [ ] Pelo menos 2 abordagens apresentadas.
- [ ] Trade-offs (Prós/Contras) claramente listados.
- [ ] Design Doc salvo no sistema de arquivos.
- [ ] **User checkpoint:** Usuário confirmou a abordagem antes de finalizar.
