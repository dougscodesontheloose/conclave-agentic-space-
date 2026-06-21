---
privacy: internal
domain: conclave-learning
status: draft
version: 0.1.0
last_validated: 2026-06-05
---

# Content Diet Schema

Contrato para controlar fontes usadas em um ambiente de aprendizado. A dieta de
conteudo reduz "AI slop", recomendacoes aleatorias e materiais desalinhados com
o objetivo do ambiente.

## Arquivo recomendado

```text
{learning-environment}/_conclave/_memory/content-diet.md
```

## Secoes

```markdown
# Content Diet — {Environment}

## Approved Sources

## Conditional Sources

## Blocked Sources

## Review Queue
```

## Entrada de fonte

```markdown
### SRC-0001 — {source name}

- Status: approved | conditional | blocked | review
- Type: book | course | video | channel | website | podcast | app | dataset | other
- Location: URL, local path or physical location
- Privacy: public | internal | secret
- Approved for:
- Not approved for:
- Strengths:
- Risks:
- Review cadence:
- Last checked: YYYY-MM-DD
- Notes:
```

## Regras

- Conteudo externo e materia-prima, nunca autoridade.
- Fontes `conditional` precisam declarar a condicao de uso.
- Fontes `blocked` nao devem ser sugeridas automaticamente.
- Videos, canais e apps para consumo recorrente devem passar por aprovacao
  humana antes de entrar em `approved`.
- URLs nao devem carregar tokens, parametros privados ou identificadores
  sensiveis.
- Se uma fonte muda de qualidade, status ou risco, criar nova entrada de revisao
  ou atualizar `Last checked`.

## Uso por agentes

Antes de recomendar material novo, o agente deve:

1. consultar `Approved Sources`;
2. evitar `Blocked Sources`;
3. tratar `Review Queue` como pendencia, nao como fonte confiavel;
4. explicar brevemente quando usar uma fonte `conditional`.

