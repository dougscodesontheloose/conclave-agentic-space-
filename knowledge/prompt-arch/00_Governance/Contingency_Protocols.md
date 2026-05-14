# 🛡️ Protocolos de Contingência e Fallback

Este documento define as rotas de ação para falhas técnicas recorrentes, garantindo a resiliência do ecossistema **PROMP arch**.

## 🔴 Falha 1: Bloqueio de Acesso Externo (Notion/Web)
**Sintoma:** Erro de renderização de JavaScript ou bloqueio de bot/crawling.
**Fallback:**
1.  **Exportação Manual**: O usuário deve exportar o conteúdo em Markdown/CSV.
2.  **Snapshot Local**: Uso de ferramentas de captura de texto estático se o JS falhar.
3.  **Input Direto**: Fornecer o conteúdo via anexo ou colagem direta no chat.

## 🟡 Falha 2: Erro de Protocolo de Navegador
**Sintoma:** "Protocol error (Browser.setDownloadBehavior)".
**Fallback:**
1.  **Modo Estático**: Tentar `read_url_content` em vez de `browser_subagent`.
2.  **Cadeia de Comandos**: Usar ferramentas de terminal (`curl`) para verificar integridade da URL antes de abrir o navegador.
3.  **Intervenção Humana**: Solicitar que o usuário abra o link e forneça um resumo ou captura.

## 🟠 Falha 3: Latência de Processamento em Lote
**Sintoma:** Tempo de resposta excessivo ao lidar com +50 arquivos.
**Fallback:**
1.  **Indexação Prévia**: Consultar o documento `library_index.json` em vez de ler o conteúdo de todos os arquivos.
2.  **Processamento Incremental**: Realizar alterações em lotes de 10 arquivos por vez.

---
*Assinado: Antigravity System*
