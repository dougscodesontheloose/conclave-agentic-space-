---
name: Disk Guardian
description: Skill de auto-higiene e zeladoria do sistema Conclave.
type: prompt
---

# Skill: Disk Guardian

Esta skill permite que o Conclave mantenha sua própria casa limpa. Ela deve ser invocada periodicamente ou após grandes atualizações de sistema para consolidar o diretório e remover lixo digital.

## Ações de Zeladoria

### 1. Limpeza de Backups (.bak)
O sistema Conclave cria backups automáticos antes de cada edição. Com o tempo, esses arquivos se acumulam.
*   **Ação:** Executar `python3 _conclave/scripts/disk_guardian.py`.
*   **Resultado:** Remoção de arquivos `.bak-*` com mais de 7 dias e geração de um relatório de limpeza.

### 2. Higiene de Outputs
Diretórios de `output/` de squads antigos podem ocupar espaço desnecessário.
*   **Ação:** Verificar se existem pastas de output sem atividade nos últimos 30 dias.
*   **Recomendação:** Sugerir ao usuário o arquivamento (`zip`) ou deleção dessas pastas.

### 3. Verificação de Integridade
*   **Ação:** Validar se todos os arquivos `.agent.md` possuem os metadados obrigatórios.
*   **Ação:** Verificar se o `intention_matrix.json` está sincronizado com a pasta `squads/`.

## Relatório de Limpeza
Ao final de cada ativação do Disk Guardian, apresente ao usuário um resumo:
- Quantos arquivos foram removidos.
- Espaço total recuperado (KB/MB).
- Status de integridade dos squads.

## Regras de Ouro
- NUNCA delete arquivos de fonte (`.py`, `.md`, `.json`, `.yaml`) que não sejam explicitamente backups (`.bak`).
- Sempre informe o usuário ANTES de rodar uma limpeza profunda em pastas de output.
- O relatório deve ser salvo em `_conclave/logs/disk_guardian_report.md`.
