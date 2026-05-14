# Persona: Prompt Engineer (v2.2)

Este repositório contém o ecossistema completo para a skill **Prompt Engineer**, agora estruturado como um **Agent Squad** com comandos slash para uma experiência "Plug & Play". 

## 📁 Estrutura do Projeto

*   **[`prompt_engineer_skill_v2.md`](file:///Users/douglasdepaulamoura/Documents/Prompt%20Engineer/prompt_engineer_skill_v2.md)**: O documento mestre contendo o System Prompt [CORE] — com os **Agentes Especializados** (/build, /optimize, /score, /refine) — e as configurações por plataforma.
*   **[`technique-registry.md`](file:///Users/douglasdepaulamoura/Documents/Prompt%20Engineer/technique-registry.md)**: Catálogo detalhado das técnicas T01–T13 aplicadas pelo agente (inclui o padrão MSTCTRL — Meta-Self-Transformation Control Loop).

*   **[`anti-patterns.md`](file:///Users/douglasdepaulamoura/Documents/Prompt%20Engineer/anti-patterns.md)**: Guia de sobrevivência contra erros comuns que degradam o desempenho da IA.
*   **[`scoring-rubric.md`](file:///Users/douglasdepaulamoura/Documents/Prompt%20Engineer/scoring-rubric.md)**: O sistema de avaliação [C/S/F/R/P] para auditar a qualidade dos prompts.
*   **[`prompt-examples-library.md`](file:///Users/douglasdepaulamoura/Documents/Prompt%20Engineer/prompt-examples-library.md)**: Um banco de dados de prompts de alta performance prontos para uso.
*   **[`fallback-stress-tests.md`](file:///Users/douglasdepaulamoura/Documents/Prompt%20Engineer/fallback-stress-tests.md)**: Documentação de testes de robustez contra entradas vagas.

## 🚀 Como Usar

1.  Abra o arquivo `prompt_engineer_skill_v2.md`.
2.  Copie o bloco marcado entre `[CORE]` e `[/CORE]`.
3.  Cole nas instruções de sistema (System Prompt, Custom Instructions ou Project Instructions) da sua plataforma de preferência.
4.  Para performance máxima, adicione os demais arquivos `.md` como **Knowledge Files** (Arquivos de Conhecimento) se a plataforma suportar (ex: Claude Projects, GPTs ou Gemini Gems).

## 🛠️ Manutenção

Para evoluir este sistema para a v2.2, foque em:
- [ ] Adicionar mais exemplos reais na biblioteca.
- [ ] Criar scripts de automação para testes de scoring.
- [ ] Expandir o Technique Registry com novas técnicas de agentes (ex: DSPy patterns).

---
*Ambiente configurado e otimizado para engenharia de prompts de nível elite.*
