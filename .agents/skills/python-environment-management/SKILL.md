---
name: Python Environment Management
description: Configura e gerencia ambientes Python (uv/venv) de forma saudável, estável e autônoma sem perda de tempo com setup.
type: tool_orchestration
---

# Skill: Python Environment Management

Esta skill atua na raiz do projeto (ou no diretório atual do squad) para garantir que qualquer operação envolvendo Python rode dentro de um ambiente isolado, estável e reproduzível. Ela é crucial para preparar o terreno para upgrades e novos scripts no ecossistema Conclave.

## Protocolo Zero-Setup

Sempre que você precisar executar um script Python, instalar dependências ou auditar um repositório baseado em Python, siga este fluxo rigorosamente:

1. **Detecção:**
   - Verifique se já existe um diretório de ambiente virtual (como `.venv` ou `venv`).
   - Verifique a presença de `pyproject.toml`, `requirements.txt` ou `uv.lock`.

2. **Criação e Isolamento (se não existir):**
   - Priorize o uso de `uv` (extremamente rápido e confiável). Se o sistema não tiver `uv`, caia para o módulo padrão `venv`.
   - Crie o ambiente: `uv venv` (ou `python3 -m venv .venv`).
   - **Nunca** modifique o ambiente global do sistema.

3. **Gerenciamento de Dependências:**
   - Instale as dependências usando o ambiente virtual criado.
   - Usando `uv`: `uv pip install -r requirements.txt` ou `uv sync`.
   - Se estiver adicionando um novo pacote: `uv pip install <pacote>` e, em seguida, atualize o `requirements.txt` (via `uv pip freeze > requirements.txt` ou ferramentas equivalentes).

4. **Execução Isolada:**
   - Para executar scripts, NÃO ative o ambiente virtual usando comandos `source` no shell bash do agente (pois a ativação não persiste entre chamadas independentes).
   - Ao invés disso, chame o interpretador Python DIRETAMENTE do ambiente virtual ou use ferramentas que abstraem isso (como `uv run`).
   - Exemplo: `./.venv/bin/python script.py` ou `uv run script.py`.

5. **Self-Healing (Auto-reparo):**
   - Se ocorrer um erro de `ModuleNotFoundError` durante a execução, intercepte a falha. Instale a dependência que falta no `.venv`, atualize os arquivos de dependência e tente a execução novamente sem notificar o usuário (apenas documente nos logs do agente).
