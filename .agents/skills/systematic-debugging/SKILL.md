---
name: Systematic Debugging
description: Protocolo rigoroso para isolamento de falhas e correção de bugs baseada em evidências.
type: prompt
---

# Skill: Systematic Debugging

Esta skill deve ser ativada sempre que você encontrar um comportamento inesperado no código ou um bug reportado. O objetivo é evitar o ciclo de "tentativa e erro" e focar na investigação científica do problema.

## O Protocolo de Depuração

Siga estes passos antes de fazer qualquer alteração no código:

### 1. Reprodução e Observação
*   **Identifique o Sintoma:** Qual é o comportamento exato? (Ex: crash, output incorreto, loop infinito).
*   **Crie um Caso de Teste Mínimo:** Tente isolar o bug em um script pequeno ou comando único.
*   **Recolha Evidências:** Use logs, prints ou screenshots para documentar o estado do erro.

### 2. Localização do Defeito (Isolamento)
*   **Rastreamento de Dados:** Siga o fluxo de dados desde a entrada até o ponto da falha.
*   **Verificação de Assunções:** Liste o que você *acha* que está acontecendo e use ferramentas (vview_file, command_status) para provar ou refutar.
*   **Busca Binária:** Comente blocos de código ou use check-outs anteriores para isolar em qual arquivo/linha o erro foi introduzido.

### 3. Análise de Causa Raiz
*   **O "Porquê":** Não se contente em saber *onde* quebrou. Pergunte por que o estado do sistema permitiu a quebra.
*   **Impacto:** Quais outras partes do sistema dependem dessa lógica?

### 4. Implementação da Solução
*   **Conserto Mínimo:** Aplique a correção mais simples que resolve a causa raiz.
*   **Evite Efeitos Colaterais:** Revise as dependências identificadas no passo 3.

### 5. Verificação de Sucesso
*   **Teste de Regressão:** Execute o caso de teste mínimo criado no passo 1.
*   **Verificação Global:** Execute o sistema completo para garantir que nada mais quebrou.

## Regras de Ouro
- **NUNCA** mude o código apenas para "ver o que acontece".
- **SEMPRE** tenha uma hipótese antes de agir.
- **SE** a mudança não resolveu o problema, reverta-a imediatamente antes de tentar o próximo passo.
