# Knowledge File: scoring-rubric.md
# Versão: 1.1.0 | Skill: prompt_engineer_v2

Este documento define os critérios de pontuação do sistema [C/S/F/R/P] utilizado pela skill Prompt Engineer para avaliar a qualidade de um prompt.

---

## 🟢 [C] Clarity (Clareza)
**Pergunta chave:** O objetivo é óbvio e sem ambiguidades?
- **10/10:** Instrução direta, sem termos vagos, objetivo único e claro.
- **5/10:** Instrução compreensível, mas exige que o modelo "adivinhe" partes da intenção.
- **0/10:** Prompt contraditório ou excessivamente confuso.

## 🔵 [S] Specificity (Especificidade)
**Pergunta chave:** O prompt restringe o modelo o suficiente para evitar variações indesejadas?
- **10/10:** Define persona, contexto, detalhes técnicos e nível de profundidade.
- **5/10:** Define a tarefa, mas ignora o contexto ou a expertise necessária.
- **0/10:** Prompt genérico (ex: "escreva sobre X").

## 🟣 [F] Format (Formato)
**Pergunta chave:** O formato de saída está definido de forma auditável?
- **10/10:** Especifica estrutura exata (ex: JSON com chaves X e Y, Tabela com colunas A, B, C).
- **5/10:** Sugere um formato (ex: "em uma lista"), mas sem detalhes de estrutura interna.
- **0/10:** Não menciona formato, deixando a cargo da IA.

## 🟠 [R] Robustness (Robustez)
**Pergunta chave:** O prompt lida com casos de erro ou inputs inesperados?
- **10/10:** Inclui protocolo de fallback e instruções para dados insuficientes.
- **5/10:** Menciona o que evitar, mas não define comportamento em caso de falha.
- **0/10:** Assume que o input será sempre perfeito.

## 🟡 [P] Portability (Portabilidade)
**Pergunta chave:** O prompt funciona consistentemente em diferentes modelos (GPT, Claude, Gemini)?
- **10/10:** Usa Markdown padrão, evita sintaxes proprietárias (como apenas tags XML do Claude ou apenas funções do GPT).
- **5/10:** Depende pesadamente de uma característica de um modelo específico, mas é adaptável.
- **0/10:** Só funciona em uma plataforma específica devido a comandos de sistema restritos.

---

## Cálculo do Score Final
O score final é a **média aritmética** das 5 dimensões.

| Score Total | Classificação | Ação Recomendada |
| :--- | :--- | :--- |
| **9.0 - 10** | **Elite** | Pronto para produção/automação. |
| **7.0 - 8.9** | **Strong** | Bom para uso manual; pequenos ajustes no formato/robustez. |
| **5.0 - 6.9** | **Average** | Requer revisão estrutural significativa. |
| **< 5.0** | **Weak** | Risco alto de alucinação ou inconsistência. |

---

## 🧠 Meta-Score (MSTCTRL / MODE 4)

Quando o MODE 4 é acionado, a avaliação **não substitui** o score C/S/F/R/P — ela o complementa com 3 checks binários (PASS/FAIL) sobre as fases obrigatórias do MSTCTRL:

| Fase | Critério de PASS |
| :--- | :--- |
| **Self-Analysis** | Mapeou explicitamente persona, fluxo de raciocínio e ≥2 camadas de abstração. |
| **Identified Limitations** | Apontou ≥3 gargalos concretos (ambiguidade, acoplamento, fallback, alucinação). |
| **Optimization Strategies** | Propôs ≥3 estratégias acionáveis, cada uma com feedback loop explícito. |

### Classificação do Meta-Score

| Passes | Classificação | Ação Recomendada |
| :--- | :--- | :--- |
| **3 / 3** | **Elite** | Meta-análise completa; integrar as estratégias propostas. |
| **2 / 3** | **Strong** | Usável, mas a fase omissa deve ser preenchida antes de iterar. |
| **< 2 / 3** | **Insuficiente** | Re-executar MSTCTRL; o diagnóstico não atingiu profundidade sistêmica. |
