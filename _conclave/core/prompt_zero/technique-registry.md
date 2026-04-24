# Knowledge File: technique-registry.md
# Versão: 1.1.0 | Skill: prompt_engineer_v2

Este registro detalha as técnicas de engenharia de prompts (T01–T12) referenciadas no [CORE] da skill Prompt Engineer. Cada técnica inclui uma descrição, quando usar e um exemplo prático.

---

## [T01] Role Prompting (Atribuição de Persona)
**Descrição:** Define uma identidade específica ou nível de expertise para a IA.
- **Quando usar:** Sempre. É a base para calibrar o tom e o nível de conhecimento.
- **Exemplo:** "Você é um Especialista em Segurança Cibernética com 20 anos de experiência em auditorias de sistemas bancários."

## [T02] Chain-of-Thought (Cadeia de Pensamento)
**Descrição:** Induz o modelo a processar o raciocínio passo a passo antes de entregar a resposta final.
- **Quando usar:** Tarefas lógicas complexas, cálculos ou análises críticas.
- **Exemplo:** "Pense passo a passo: primeiro identifique os gargalos, depois calcule o impacto de cada um e, por fim, sugira a solução."

## [T03] Few-Shot Examples (Exemplos Poucos-Disparos)
**Descrição:** Fornece 2 a 3 exemplos de entrada e saída para mostrar o padrão desejado.
- **Quando usar:** Quando o formato de saída é muito específico ou difícil de descrever apenas com palavras.
- **Exemplo:** 
  "Entrada: [Texto] | Saída: [Resumo]
   Entrada: 'O sol nasce no leste' | Saída: 'Fenômeno astronômico'
   Entrada: 'A bolsa caiu 2%' | Saída: 'Evento financeiro'"

## [T04] Output Schema (Esquema de Saída)
**Descrição:** Define a estrutura exata da resposta (JSON, Markdown, Tabelas, YAML).
- **Quando usar:** Integrações de sistemas ou quando a legibilidade é prioridade.
- **Exemplo:** "Sua resposta deve ser estritamente em JSON no seguinte formato: `{"id": number, "status": string}`."

## [T05] Negative Constraints (Restrições Negativas)
**Descrição:** Instruções explícitas sobre o que a IA **não** deve fazer.
- **Quando usar:** Para evitar alucinações, termos proibidos ou estilos indesejados.
- **Exemplo:** "Não mencione concorrentes. Não use jargões técnicos. Não ultrapasse 50 palavras."

## [T06] Context Injection (Injeção de Contexto)
**Descrição:** Insere dados externos, documentos ou informações de domínio específicos no prompt.
- **Quando usar:** Quando a IA precisa saber detalhes que não estão no seu treinamento base.
- **Exemplo:** "Use os dados de vendas do Q3 anexados abaixo para projetar o crescimento do Q4."

## [T13] MSTCTRL — Meta-Self-Transformation Control Loop
**Descrição:** Loop recursivo de auto-auditoria estrutural com linguagem de sistemas (feedback loops, abstraction layers, optimization cycles). Diferente de T08 (verificação de output) e de MODE 3 (score quantitativo): aqui o foco é diagnóstico arquitetural qualitativo do próprio prompt.
- **Quando usar:** MODE 4 (META) ou sempre que o usuário pedir diagnóstico profundo da estrutura de um prompt, distinto de um score quantitativo.
- **Estrutura obrigatória (3 fases):**
  1. **Self-Analysis** — mapear persona, fluxo de raciocínio, dependências contextuais e ≥2 camadas de abstração.
  2. **Identified Limitations** — apontar ≥3 gargalos concretos (ambiguidade, acoplamento a plataforma, lacunas de fallback, risco de alucinação).
  3. **Optimization Strategies** — propor ≥3 estratégias acionáveis com feedback loops explícitos e ciclos de otimização mensuráveis.
- **Exemplo:** "Execute MSTCTRL sobre este prompt: identifique feedback loops, aponte camadas de abstração fracas e proponha 3 ciclos de otimização mensuráveis."
