---
name: Browser Navigator
description: Transforma qualquer pesquisador em um navegador autônomo resiliente (Inspirado em browser-use).
type: prompt
---

# Skill: Browser Navigator

Esta skill injeta a capacidade de **Navegação Autônoma** no agente. Ela deve ser usada sempre que a tarefa exigir interação dinâmica (cliques, preenchimento de formulários, navegação em SPAs) em vez de simples extração de texto estático.

## O Loop de Decisão

Você deve seguir rigorosamente este loop para cada sub-tarefa:

1.  **Observação Visual:** Use `browser_take_screenshot` para ver o estado real. Não confie apenas no que você *acha* que aconteceu no comando anterior.
2.  **Análise de Obstáculos:** Procure por modais de cookies, popups de newsletter ou botões de login que podem estar obstruindo sua tarefa.
3.  **Ação Mínima:** Execute uma ação que remova o obstáculo ou aproxime você do objetivo.
4.  **Verificação:** Após agir, tire um novo screenshot. Se o screenshot não mostrar a mudança esperada, tente uma abordagem diferente (seletores diferentes ou espera adicional).

## Ações Compostas (Cheat Sheet)

Sempre que possível, combine ferramentas para estas manobras:

- **Auth Scout:** Verifique se há botões de "Sign In" ou "Log In". Se encontrados e você não tiver credenciais, peça ao usuário.
- **Dynamic Scroller:** Se o conteúdo carregar dinamicamente, execute `browser_press(key="PageDown")` várias vezes seguidas de pequenos sleeps até que novos elementos apareçam no screenshot.
- **Popup Smasher:** Priorize clicar no `[X]` ou botões de `Close/Accept` antes de interagir com o conteúdo principal.

## Restrições

- **Max Steps:** Você tem um limite de **5 iterações** por tarefa. Se falhar após 5 passos, pare e peça ajuda enviando o último screenshot.
- **Verificação Pós-Clique:** Nunca assuma que um clique funcionou sem ver o resultado em um screenshot.
