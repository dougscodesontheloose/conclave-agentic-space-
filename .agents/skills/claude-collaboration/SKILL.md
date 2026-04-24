---
name: Claude Collaboration (Multi-Agent Handoff)
description: Permite que múltiplos devs e agentes trabalhem juntos no mesmo fluxo de forma serializada, usando protocolo de handoff e validação de qualidade.
type: orchestration
---

# Skill: Claude Collaboration (Handoff Protocol)

Esta skill orquestra a colaboração entre múltiplas sessões de IA ou diferentes agentes do Conclave trabalhando em um problema contínuo que excede a janela de contexto de uma única sessão.

## Protocolo de Handoff

Sempre que a sua janela de contexto começar a ficar longa demais, ou quando o seu agente finalizar o escopo de sua especialidade e precisar repassar a tarefa para o próximo (ex: do Planner para o Coder, ou do Coder para o Reviewer), siga o Protocolo de Handoff:

1. **Cadeia de Validação de Qualidade (Pré-Handoff):**
   Antes de "passar o bastão", você DEVE executar um checklist de qualidade sobre o trabalho realizado:
   - *O código compila ou o comando executa sem erro?* (Teste antes de passar).
   - *A documentação está atualizada de acordo com as mudanças?*
   - *O estado foi salvo corretamente?*
   - Não repasse o bastão se a etapa atual contiver um erro crítico não resolvido. Você deve tentar reparar ou registrar detalhadamente o erro para o próximo agente.

2. **Geração do Arquivo de Estado (Handoff State):**
   Crie ou atualize o arquivo `.conclave/handoff.md`. Este arquivo é a ponte entre você e o próximo agente.
   
   Ele deve conter RIGOROSAMENTE:
   - **Status Atual:** O que foi finalizado na sessão/sprint atual.
   - **Estado do Sistema:** Arquivos modificados, ferramentas instaladas, portas abertas, etc.
   - **Problemas Conhecidos:** Bugs restantes, limitações descobertas ou logs de erro.
   - **Próximo Passo Explícito (To-Do):** Instrução clara e inconfundível sobre qual é a próxima ação que o próximo agente deve realizar assim que assumir.
   - **Contexto Recuperável:** Links para arquivos de "tertiary-logs" (se houver).

3. **Finalização da Sessão:**
   Avise o usuário de que o Handoff foi gerado com sucesso, passe o status de qualidade, e sugira o próximo prompt para iniciar a sessão subsequente ou ativar o próximo agente.
