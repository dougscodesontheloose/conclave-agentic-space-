---
id: browser-automation
name: Autonomous Browser Automation
maturity: draft
usedInSquads: []
---

# Padrão Conclave: Automação de Browser Autônoma

Este documento define o padrão de ouro para agentes que interagem com a web via Playwright no Conclave. Inspirado pelo framework `browser-use`, este padrão foca em resiliência, auto-correção e verificação de estado.

## 1. O Loop de Navegação Autônoma

Agentes de browser devem operar em um ciclo fechado de 5 passos para cada sub-tarefa:

1.  **OBSERVAR:** Tira um screenshot e extrai os elementos visíveis (DOM simplificado).
2.  **ORIENTAR:** Compara o estado atual com o objetivo. Detecta obstáculos (modais, popups de cookies, erros de carregamento).
3.  **DECIDIR:** Escolhe a **ação mínima** necessária (ex: clicar no botão "Aceitar Cookies" em vez de tentar clicar no link de destino imediatamente).
4.  **AGIR:** Executa a ação via tool call do Playwright.
5.  **VERIFICAR:** Tira um novo screenshot e confirma se o estado mudou como esperado. Se não, re-itera.

## 2. Verificação de Estado (Screenshot Feedback)

A verificação visual é obrigatória após qualquer ação interativa.

- **Falha Positiva:** O agente clicou em um botão, mas um modal de login apareceu impedindo o clique. Sem o screenshot, o agente assumiria que o clique funcionou.
- **Regra:** Sempre use `browser_take_screenshot` após `browser_click`, `browser_type` ou `browser_press`.

## 3. Manejo de Interrupções e Modais

Interrupções (popups de newsletter, cookies, ofertas) são normais.

- O agente deve ser instruído a tratar esses elementos como "Prioridade Zero" antes de prosseguir com a tarefa principal.
- **Dica:** Se o elemento principal não estiver visível ou clicável, a primeira ação deve ser procurar por botões de "Fechar" ou "Aceitar" no screenshot.

## 4. Limites e Segurança

Para evitar gastos excessivos de tokens e loops infinitos:

- **Max Iterations:** O limite padrão é **5 interações por tarefa** (passo do pipeline). Se não atingir o objetivo em 5 passos, o agente deve reportar o bloqueio ao usuário com um screenshot do estado atual.
- **Custo:** Screenshots consomem contexto. Priorize screenshots de resoluções menores ou áreas específicas se o modelo suportar.

## 5. Ações Compostas (Custom Tools)

Agentes devem preferir ações compostas documentadas para tarefas comuns:

- **`scout_page_for_leads`**: Scroll profundo + extração de links de perfil.
- **`capture_pricing_table`**: Localiza elementos de preço, alterna entre mensal/anual se necessário, e extrai dados.
- **`auth_and_proceed`**: Detecta campos de login, preenche (se tiver credenciais no cofre) e verifica sucesso.
