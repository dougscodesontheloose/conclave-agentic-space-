# Knowledge File: fallback-stress-tests.md

# Versão: 1.0.0 | Skill: prompt_engineer_v2

Este documento documenta os testes de stress realizados no Fallback Protocol para garantir que a IA não "alucine" prompts sem contexto suficiente.

---

## Protocolo de Referência

*Se o input tiver menos de 2 sentenças de contexto, responder APENAS com as informações faltantes.*

---

## Cenários de Teste

### Teste 01: Input de Palavra Única

- **Input do Usuário:** "Vendas"
- **Resposta Esperada:**
  > To build an effective prompt, I need to understand:
  > 1. What exactly are you trying to sell and to whom?
  > 2. What is the desired format (email, ad, script)?

### Teste 02: Intenção Vaga

- **Input do Usuário:** "Crie um prompt para um analista de dados."
- **Resposta Esperada:**
  > To build an effective prompt, I need to understand:
  > 1. What type of data or databases will the analyst query (SQL, Excel, Python)?
  > 2. What is the specific goal of the analysis (prediction, cleaning, report)?

### Teste 03: Prompt Curto sem Metadata

- **Input do Usuário:** "Melhore isso: 'faça um código em python'."
- **Resposta Esperada:**
  > To build an effective prompt, I need to understand:
  > 1. What should the Python code do specifically?
  > 2. Are there any specific libraries or version constraints?

### Teste 04: Linguagem Natural Ambigua

- **Input do Usuário:** "Me ajuda com minha IA."
- **Resposta Esperada:**
  > To build an effective prompt, I need to understand:
  > 1. Are you building a new prompt or trying to fix an existing one?
  > 2. What is the specific task the IA is failing at?

---

## Log de Resultados (Simulação)

| Data | Cenário | Resultado | Status |
| :--- | :--- | :--- | :--- |
| 2026-04-14 | Teste 01 | Bloqueou criação; pediu info. | ✅ PASS |
| 2026-04-14 | Teste 02 | Identificou falta de contexto técnico. | ✅ PASS |
| 2026-04-14 | Teste 03 | Evitou alucinação de código genérico. | ✅ PASS |
| 2026-04-14 | Teste 04 | Solicitou definição de modo (Build vs Improve). | ✅ PASS |

---
**Conclusão:** O protocolo de fallback está robusto. Os gatekeepers estão impedindo a execução de tarefas com entropia muito alta.
