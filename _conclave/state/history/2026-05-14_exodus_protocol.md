# Protocolo Exodus e Esmagamento de Limites do GitHub

**Data:** 14 de Maio de 2026
**Responsáveis:** <user_name> e Antigravity (Conclave System)

## Objetivo
Implementar o "Protocolo Exodus", uma solução definitiva e arquitetural para o versionamento e exportação do ecossistema Conclave em duas vias distintas:
1. **Conclave Prime:** O host original e privado (Fullride), contendo o sistema intacto, os ambientes de trabalho (ambientes/) e memórias pessoais.
2. **Conclave Agentic Space (Open Source):** A versão pública, higienizada, livre de chaves de API, arquivos pesados de mídia, pastas pessoais e assinaturas comportamentais (<user_name>/<user_name>/<user_name>), preparada para ser iniciada limpa por um novo usuário via `Conclave.init`.

## O que Aconteceu e Erros Cometidos
Durante a execução do Protocolo Exodus, enfrentamos três falhas críticas relacionadas aos limites estruturais do Git e às defesas ativas do GitHub. **Estas falhas estão sendo documentadas aqui para que o sistema se auto-regule em futuras iterações.**

### Erro 1: Travamento da Indexação Local (`git add .`)
- **Problema:** A pasta do Conclave havia crescido para mais de 24.5 GB devido a milhares de ativos multimídia em `references/` e builds pesados de frameworks (como Electron) em `ambientes/`. O comando de indexação local (`git add .`) engasgou e a memória estourou.
- **Aprendizado:** Repositórios Git locais não foram feitos para lidar com pastas de assets de design gigantes. 
- **Solução (Redundância):** O arquivo `.gitignore` foi fortificado com exclusões expressivas de `references/*` e exclusões de compilações `ambientes/**/node_modules`, `dist/`, etc. Em contrapartida, foi gerado o arquivo `references/MAPA.md` para documentar a taxonomia do espaço ausente para a IA.

### Erro 2: Bloqueio Físico de Envio (Limite de 100MB)
- **Problema:** Ao tentar o push (`git push -u origin main --force`), o GitHub rejeitou completamente a subida. O motivo foi um arquivo de log ZIP de 1.4 GB (`ba3d2a4f...zip` na pasta `knowledge/memory-lane/`).
- **Aprendizado:** O limite absoluto por arquivo na versão gratuita/padrão do GitHub é de 100MB. Arquivos compactados antigos que cruzam a margem farão o pipeline inteiro de commit cair.
- **Solução (Redundância):** Adicionadas regras rígidas no `.gitignore` (`*.zip`, `*.rar`, `*.tar.gz`). O arquivo teve que ser purgado da árvore do Git (`git rm --cached`) seguido de um `commit --amend`. No futuro, a IA e o usuário devem rastrear arquivos grandes (`find . -type f -size +90M`) *antes* de executar commits inteiros de backup.

### Erro 3: Proteção Ativa Contra Vazamento de Segredos (GH013)
- **Problema:** O push da versão *Open Source* foi barrado pelo "GitHub Push Protection", que identificou um segredo do LinkedIn Client Secret ("WPL_AP1...") exposto nos arquivos `legacy/linkedin-auth/linkedin-auth2.py`.
- **Aprendizado:** A higienização heurística básica via script ignorou esse tipo de assinatura porque procurou apenas por "sk-ant" e "sk-proj".
- **Solução (Redundância):** O script de sanitização e a IA responsável pelo expurgo devem sempre rastrear não apenas as chaves modernas da OpenAI e Anthropic, mas a estrutura inteira de códigos "legacy" com chaves de clientes OAuth (client_secret, access_token). A string precisou ser esmagada localmente (`<linkedin_client_secret>`) e o commit rescrito com `--amend`.

## Decisões Arquiteturais Consolidadas
- A separação entre o *Prime* e o *Agentic Space* agora funciona organicamente através da lógica de diretório clonado e higienizado da raiz, protegido do `main` local.
- Adicionado um bloco semântico no *Router Agent* e no `opensource.md` instruindo formalmente a IA a não apenas "limpar nomes", mas investigar ativamente as restrições físicas de limite de bytes e políticas de segredos no ato do backup.
