---
privacy: internal
domain: conclave-learning
status: draft
version: 0.1.0
last_validated: 2026-06-05
---

# Decision Ledger Schema

Contrato para estabilizar decisoes de aprendizado, design pedagogico e
operacao local. O ledger evita que agentes reabram escolhas ja fechadas ou
repitam propostas rejeitadas.

## Arquivo recomendado

```text
{learning-environment}/_conclave/_memory/decision.md
```

## Quando registrar

Registre apenas quando houver decisao explicita, validada ou recorrente o
suficiente para orientar proximas sessoes.

Exemplos validos:

- objetivo principal do ambiente;
- habilidade prioritaria;
- metodologia escolhida;
- restricao pedagogica;
- fonte aprovada ou vetada;
- criterio de avancar, repetir ou reduzir dificuldade.

Nao registre:

- inferencias fracas sobre preferencia;
- notas soltas de sessao;
- metricas temporarias;
- conteudo bruto de transcricao, OCR ou web;
- dados classificados como `secret`.

## Formato de entrada

```markdown
## DEC-YYYYMMDD-001 — {short title}

- Status: active | superseded | retired
- Date: YYYY-MM-DD
- Scope: environment | squad | source | method | safety | output
- Decision:
- Rationale:
- Evidence:
- Replaces:
- Review trigger:
- Owner: human | agent-assisted
```

## Regras

- Decisoes novas nao apagam decisoes antigas; elas marcam a anterior como
  `superseded`.
- Toda decisao deve ser acionavel em uma frase.
- O ledger tem prioridade sobre sugestoes genericas de agentes.
- Se a decisao conflitar com SafeGuard, SafeGuard vence.
- Se a decisao conflitar com uma instrucao direta do usuario na sessao atual,
  a sessao atual vence e o ledger deve ser revisado depois.

