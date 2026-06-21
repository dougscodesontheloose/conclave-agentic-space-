# ⚡ Conclave Cheat Sheet (Folha de Referência)

Este documento contém os principais comandos, gatilhos e atalhos para operar o ecossistema Conclave com máxima eficiência.

## 🕹️ Comandos de Barra (Slash Commands)

| Comando | Ação |
| :--- | :--- |
| `/conclave` | Abre o Menu Principal interativo. |
| `/conclave init` | Inicializa o Conclave no diretório atual. |
| `/conclave help` | Exibe a ajuda detalhada do sistema. |
| `/conclave list` | Lista todos os squads disponíveis em `squads/`. |
| `/conclave run <nome>` | Inicia a execução de um squad específico. |
| `/conclave create <desc>` | Ativa o Arquiteto para criar um novo squad. |
| `/conclave edit <nome>` | Ativa o Arquiteto para modificar um squad existente. |
| `/conclave delete <nome>` | Remove permanentemente um diretório de squad. |
| `/conclave skills` | Abre o gerenciador de habilidades (Skills Engine). |
| `/conclave show-company` | Exibe o perfil atual em `company.md`. |
| `/conclave edit-company` | Re-inicia o fluxo de configuração do perfil. |
| `/conclave settings` | Atalho para editar `preferences.md`. |
| `/conclave recall <query>` | Busca em todos os arquivos de memória, logs e runs. |
| `/conclave model` | Visualiza ou atualiza o seu modelo de usuário inferido. |
| `/conclave docs` | Regenera o `TUTORIAL.md` a partir dos dados ao vivo. |
| `/conclave tide` | 🌊 Roda o POSEIDON (agrega streams e detecta tendências). |
| `/conclave curate` | ☀️ Roda o APOLLO (deduplica, arquiva e resolve memórias). |
| `/conclave forge` | 🔨 Roda o HEPHAESTUS (revisa candidatos a novas skills). |
| `/conclave where` | Exibe os caminhos resolvidos do sistema (debug). |
| `/conclave exodus` | 📦 Exporta o Conclave de forma segura (Fullride ou Open Source). |

---

## 🚀 Gatilhos e Automações

### Início e Fim de Sessão
- **Start:** O Conclave inicia automaticamente ao detectar sua presença (Heartbeat).
- **Wrap-up:** Use as frases **"Call it a day"** ou **"Bed time"** para encerrar a sessão, rodar o Heartbeat (End) e gerar o relatório de progresso.

### Linguagem Natural
Você não precisa apenas de comandos. Pode dizer coisas como:
- *"Preciso de um squad para analisar os leads do LinkedIn"* (O **Router** irá sugerir o melhor caminho).
- *"O que aprendemos com o projeto Cliff Palace?"* (O **Poseidon** buscará nas memórias e na Crônica).

---

## 🧠 Personas do Core (Agentes do Sistema)

| Agente | Especialidade | Quando chamar |
| :--- | :--- | :--- |
| **Architect** | Estrutura e Design | Criar ou refatorar squads e agentes. |
| **Runner** | Execução e Controle | Rodar pipelines e garantir checkpoints. |
| **Router** | Intenção e Triagem | Decidir qual squad ou skill resolve um problema. |
| **Apollo** | Research & Leads | Prospecção, busca de empresas e contatos. |
| **Artemis** | Inteligência GTM | Estratégia de marketing, growth e análise. |
| **Exodus** | Segurança | O Arquivista de exportação e backup do sistema. |
| **Minerva** | Qualidade e Ética | Revisão de código e conformidade com SafeGuard. |
| **Poseidon** | Memória e Evolução | Recuperar contextos históricos e aprendizados. |

---

## 📂 Mapa de Diretórios Essenciais

- 📁 `squads/`: Seus squads operacionais (ex: `cliff_palace`, `headhunter`).
- 📁 `_conclave/state/memory/`: Onde mora sua identidade (`company.md`) e preferências.
- 📁 `_conclave/state/history/`: A **Crônica**, registrando a evolução do sistema.
- 📁 `agents/`: Definições `.agent.md` de todos os agentes disponíveis.
- 📁 `_conclave/core/`: O "cérebro" do sistema (não editar manualmente sem o Architect).

---

## 🛡️ Protocolo SafeGuard (Segurança)

- **Tier SECRET:** Dados sensíveis (CPF, Endereço, Dados Bancários). **Nunca** saem do seu ambiente local.
- **Veto Automático:** O sistema interrompe a execução se detectar vazamento de dados SECRET para pastas de saída pública.

> **Dica:** Em caso de dúvida, digite `/conclave help` ou peça ao **Docs Agent** para explicar uma função específica.
