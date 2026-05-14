# Protocolo Exodus: Conclave Prime (Fullride)

**Este é o protocolo de backup primordial, privado e irrestrito do ambiente Conclave.**

A exportação `Fullride` preserva a essência exata do sistema para o uso exclusivo de seu criador (Douglas). O objetivo deste commit é servir como um porto seguro (disaster recovery) ou ponto de clonagem caso o desenvolvedor mude de máquina ou perca os dados locais.

## O que ESTÁ incluído:
- Toda a pasta `_conclave/` (núcleo lógico, agentes, roteadores, memórias globais).
- A pasta `squads/` (composição, histórico e memória dos squads).
- A pasta `skills/` (arquitetura das habilidades criadas).
- A lógica de projetos dentro de `ambientes/` e códigos essenciais.
- Preferências de comportamento, arquivos sensíveis (`.cursorrules`, `CLAUDE.md`, `AGENTS.md`) e estilo pessoal ("Doug/<user_name>").

## O que NÃO ESTÁ incluído (por Limitações Físicas do Git):
- A pasta `references/` (com seus arquivos MD, imagens, vídeos, brand style e visual style) foi excluída propositalmente pelo `.gitignore` para evitar exceder o limite de repositório (apenas o arquivo `MAPA.md` é salvo).
- Builds massivos e binários compilados dentro de `ambientes/` (`node_modules`, `dist`, `.app`, `.dmg`, `.venv`) também são ignorados.
- Chaves de API ativas salvas em variáveis de ambiente `.env` ou chaves MCP globais protegidas, para prevenir vazamento mesmo em repositório privado.

## Como Executar este Protocolo:
Caso a IA seja solicitada a realizar o "Backup Conclave Prime" ou "Fullride":

1. A IA deve informar ao usuário o início da operação.
2. A IA deve executar no terminal:
   ```bash
   git add .
   git commit -m "chore(exodus): commit fullride de seguranca"
   git push origin main
   ```
3. A IA deve validar e informar ao usuário o êxito da operação.
