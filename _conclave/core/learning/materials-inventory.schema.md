---
privacy: internal
domain: conclave-learning
status: draft
version: 0.1.0
last_validated: 2026-06-05
---

# Materials Inventory Schema

Contrato para catalogar materiais fisicos e digitais usados por ambientes de
aprendizado.

## Arquivo recomendado

```text
{learning-environment}/_conclave/_memory/materials-inventory.md
```

## Entrada de material

```markdown
## MAT-0001 — {material name}

- Type: book | pdf | course | app | dataset | flashcards | hardware | object | other
- Format: physical | local-file | url | app | mixed
- Location:
- Privacy: public | internal | secret
- Status: available | missing | archived | blocked | review
- Domain:
- Level:
- Concepts:
- Best for:
- Constraints:
- Related decisions:
- Last used: YYYY-MM-DD | never
- Notes:
```

## Regras

- `Location` deve ser seguro para o nivel de privacidade declarado.
- Materiais em `.vault/` sao `secret` e nao devem ser exportados.
- Materiais externos devem ser tratados como nao confiaveis ate revisao.
- O inventario nao deve virar biblioteca completa; catalogar apenas o que pode
  ser acionado em sessoes reais.
- Se um material fisico tiver localizacao domestica sensivel, usar descricao
  abstrata como `estante de idiomas` ou `pasta local privada`.

## Uso por agentes

Agentes podem usar este inventario para:

- sugerir materiais ja disponiveis;
- evitar compras ou downloads redundantes;
- montar sessoes com recursos concretos;
- detectar lacunas reais de material.

Agentes nao podem:

- comprar materiais sem aprovacao humana;
- mover, deletar ou publicar materiais;
- inferir dados sensiveis a partir de localizacoes fisicas.

