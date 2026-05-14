---
name: prediction-markets
description: >
  Consulta dados de mercados de previsão via Polymarket API (Gamma, CLOB, Data).
  Extrai preços, histórico, volume e odds para responder sobre probabilidades de eventos.
type: playbook
tags: [research, prediction-markets, market-data, data, analytics]
---

# Prediction Markets (Polymarket)

Consulte dados de mercados de previsão para obter probabilidades reais (odds) baseadas em dinheiro apostado sobre eventos mundiais, eleições e cultura.

**Core principle:** Probabilidades baseadas em dinheiro real (prediction markets) são mais precisas e menos enviesadas que palpites ou opiniões de especialistas.

## When to Use

- "What are the odds of X happening?"
- "O que o Polymarket diz sobre as eleições/evento?"
- "What is the current probability of [event]?"
- Qualquer request que exija medir a probabilidade de um evento futuro onde existam mercados líquidos.

**Auto-trigger:** Quando o usuário perguntar sobre a chance/probabilidade de um evento político, econômico ou cultural altamente coberto pela mídia.

## Prerequisites

### Environment Variables
Nenhuma.

### Dependencies
Nenhuma. Usa curl e REST APIs públicas. Pure reasoning/data skill.

## Inputs

| Input | Required | Description |
|---|---|---|
| **Query/Tema** | Yes | O tópico do evento ou pergunta (ex: "US Election", "Interest Rates") |
| **Tipo de Dado** | No | "Prices", "Orderbook", "History" (Default: Prices) |

## Phase 0: Intake

1. **Pergunta obrigatória:** Qual o evento específico que você quer analisar as probabilidades?
2. **Pergunta opcional:** Você quer apenas as odds atuais, ou também o histórico recente e volume de apostas?

## Phase 1: Market Discovery (Gamma API)

### Step 1A: Search Markets
Busque por mercados usando a Gamma API (`gamma-api.polymarket.com`).

```bash
# Exemplo de busca:
curl -s "https://gamma-api.polymarket.com/events?query=eleicao&active=true"
```

Extraia os eventos e mercados aninhados.

### Step 1B: Parse Data
Analise o retorno JSON. Os preços são as probabilidades.
- `outcomePrices`: Extraia usando parse JSON. O preço "0.65" = "65% de probabilidade".

## Phase 2: Deep Dive (CLOB & Data API)

### Step 2A: Price History
Se o usuário pedir histórico, use o `conditionId` do mercado.
Consulte a CLOB API (`clob.polymarket.com/prices-history`).

## Phase 3: Output

### Output Format

| Output | Format | Location |
|---|---|---|
| **Probabilidades** | Markdown | Exibido ao usuário |

### Output Template

```markdown
# Prediction Market Data: [Event Name]

## Current Odds
- **Yes:** XX.X%
- **No:** XX.X%

## Market Context
- **Volume:** $XX,XXX
- **Status:** [Active/Closed]

## Analysis
[Breve análise do sentimento de mercado]
```

## Cost

| Component | Cost |
|---|---|
| Polymarket API | Free |
| LLM reasoning | Free |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **No Markets Found** | API retorna array vazio | Tentar termos mais amplos ou informar que não há mercado ativo. |
| **API Rate Limit** | HTTP 429 | Esperar 10s. Gamma tem limite de 4000 req/10s. |

**Principle:** Always display odds as percentages for human readability and clearly state the trading volume to gauge market confidence.

## Composability

**Receives data from:**
- `industry-scanner` — pode passar trends para verificar odds.

**Feeds into:**
- `competitor-intel` — odds sobre sucesso de features ou produtos rivais.

## Memory & Learning

| What to Save | Format | Example |
|---|---|---|
| **Market queries** | `[ESTRATÉGICO]: prediction-markets — [Topic] market is highly liquid` | "Election markets have high volume" |

## Quality Gate

Before delivering the final output, verify:
- [ ] **Prompt Injection Check:** Ensure query terms don't contain malicious payloads.
- [ ] **Math check:** Do the probabilities (Yes + No) roughly equal 100%?
- [ ] **Volume check:** Is the volume included to show market depth?
