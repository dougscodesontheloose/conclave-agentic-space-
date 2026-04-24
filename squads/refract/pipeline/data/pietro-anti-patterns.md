# Knowledge File: anti-patterns.md
# Versão: 1.0.0 | Skill: prompt_engineer_v2

Este arquivo lista erros comuns em engenharia de prompts que degradam o desempenho dos modelos de IA, seguidos pelas correções recomendadas.

---

## 1. O Paradoxo da Verborragia
**Erro:** Escrever parágrafos longos e narrativos achando que "mais contexto é sempre melhor", sem estrutura.
- **Sintoma:** A IA ignora instruções no meio do texto (efeito *lost in the middle*).
- **Correção:** Use Markdown, listas numeradas e delimitadores (como `###` ou `---`).
- **Antipattern:** "Oi IA, tudo bem? Eu queria que você fizesse um texto sobre gatos, mas não pode ser muito longo, e por favor use um tom fofo e fale sobre a raça persa também..."
- **Padrão:** 
  "Tarefa: Escrever sobre gatos.
   Raça: Persa.
   Tom: Fofo/Carinhoso.
   Restrição: Máximo 50 palavras."

## 2. Instruções Negativas Isoladas
**Erro:** Dizer apenas "não faça X" sem dar uma alternativa do que fazer.
- **Sintoma:** A IA foca no termo proibido e acaba mencionando-o.
- **Correção:** Combine restrições negativas com instruções positivas.
- **Antipattern:** "Não use termos técnicos."
- **Padrão:** "Use linguagem simples e acessível. Evite jargões técnicos ou termos acadêmicos."

## 3. Ambiguidade de Persona
**Erro:** Pedir para a IA ser "um especialista" sem definir qual área.
- **Sintoma:** Respostas genéricas e superficiais.
- **Correção:** Defina o cargo, anos de experiência e objetivo.
- **Antipattern:** "Aja como um especialista."
- **Padrão:** "Aja como um Arquiteto de Software Sênior especializado em microsserviços Java."

## 4. Falta de Delimitadores de Input
**Erro:** Colar um texto longo para análise sem indicar onde ele começa e termina.
- **Sintoma:** A IA confunde as instruções do prompt com o conteúdo do texto fornecido.
- **Correção:** Use tags XML ou delimitadores claros.
- **Antipattern:** "Resuma este texto: [COLAGEM DO TEXTO]"
- **Padrão:** 
  "Analise o texto delimitado por <content>:
   <content>
   [TEXTO AQUI]
   </content>"

## 5. Pedir "Sim ou Não" para Temas Complexos
**Erro:** Forçar o modelo a uma escolha binária em assuntos que exigem nuance.
- **Sintoma:** Alucinação ou viés forçado.
- **Correção:** Peça uma análise de prós e contras antes da conclusão.
- **Padrão:** "Avalie os pontos A e B. Liste os riscos de cada um e, ao final, recomende o mais seguro."

---
*Este arquivo será atualizado conforme novos edge cases forem identificados em testes de stress.*
