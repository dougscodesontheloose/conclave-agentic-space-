---
name: Dialectical Memory
description: Padrao de raciocinio para higiene e estruturacao de memoria a longo prazo.
type: prompt
---

# Skill: Dialectical Memory

Esta skill injeta um "filtro de consciência" no agente antes de ele escrever no arquivo `memories.md` de qualquer squad. O objetivo é evitar que o sistema se torne um cemitério de dados inúteis, mantendo apenas o "ouro" estratégico.

## O Processo Dialético

Sempre que você for salvar um aprendizado ou fato novo, aplique estas 3 perguntas:

1.  **Isso é Reutilizável?** Este fato será útil para um novo squad no futuro ou for the user to make uma decisão daqui a um mês? (Se for apenas um log técnico de execução, não salve).
2.  **Qual o Impacto?** Isso altera a estratégia (Estratégico), o fluxo de trabalho (Operacional) ou os gostos/valores do usuário (Pessoal)?
3.  **Posso Sintetizar?** Existe uma forma de dizer isso em uma frase curta que capture a essência sem precisar de 3 parágrafos?

## Categorização de Memória

Ao escrever no `memories.md`, use estes prefixos para facilitar a recuperação pelo Arquiteto:

*   **[ESTRATÉGICO]:** Insights sobre posicionamento, mercado ou carreira.
*   **[OPERACIONAL]:** Descobertas sobre ferramentas, bugs fixados ou fluxos otimizados.
*   **[PESSOAL]:** User preferences, tom de voz, rotinas de saúde ou valores.

## Exemplo de Transformação
*   **Antes:** "Tentei rodar o comando X mas deu erro Y porque a permissão do diretório Z estava errada. Aí dei o comando chmod e funcionou."
*   **Depois (Dialética):** `[OPERACIONAL]: Em sistemas macOS, o diretório Z exige permissão explicita via chmod antes de instalações via Homebrew.`

## Regras de Ouro
- Mantenha a memória limpa. Menos é mais.
- Priorize o aprendizado (o *insight*) sobre a ação (o *log*).
- Se a informação contradiz uma memória anterior, registre a contradição e decida qual é a nova verdade.
