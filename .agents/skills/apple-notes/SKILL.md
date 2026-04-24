---
name: Apple Notes Integration
description: Sincronização de notas, briefings e planos com o app nativo Notas da Apple via CLI memo.
type: prompt
---

# Skill: Apple Notes Integration

Esta skill permite que o Conclave leia e escreva diretamente no seu sistema de notas pessoal do macOS. Use-a para salvar briefings, registrar decisões de squads ou buscar informações históricas arquivadas no app Notas.

## Ferramenta Base
Esta skill depende da CLI `memo` instalada no sistema.

## Ações de Nota

### 1. Criar/Atualizar Briefing
Sempre que um squad finalizar um plano estratégico importante, ofereça-se para arquivá-lo:
*   **Comando:** `memo edit "CONCLAVE: [Nome do Squad] - Briefing"`
*   **Ação:** O agente abrirá a nota (ou criará se não existir) e injetará o conteúdo formatado em Markdown.

### 2. Buscar Contexto Pessoal
Se a tarefa envolver informações que o usuário mencionou ter "anotado", procure primeiro no Notas:
*   **Comando:** `memo list | grep -i "[Keyword]"`
*   **Ação:** Identifique a nota correta e use `memo cat "[Titulo]"` para ler o conteúdo.

### 3. Registro de Insights Rápidos
Durante uma execução, se surgir um insight valioso que não pertence ao output direto da tarefa:
*   **Comando:** `memo edit "CONCLAVE: Scrapbook/Insights"`
*   **Ação:** Adicione o insight com timestamp no final da nota centralizada de rascunhos.

## Regras de Ouro
- **Privacidade (SafeGuard):** Nunca salve dados da categoria **SECRET** (ex: senhas, CPFs) no Notas, a menos que a nota já esteja protegida ou o usuário peça explicitamente.
- **Prefixos:** Use sempre o prefixo `CONCLAVE:` para facilitar a organização do usuário dentro do app.
- **Formatação:** Mantenha a elegância do Markdown. O Notas da Apple suporta formatação rica básica.

> [!IMPORTANT]
> Se o comando `memo` falhar com erro de permissão, o usuário precisa autorizar a "Automação" para o terminal em **Ajustes do Sistema > Privacidade e Segurança > Automação**.
