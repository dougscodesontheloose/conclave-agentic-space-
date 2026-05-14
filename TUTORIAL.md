<!-- AUTO-GENERATED — não edite manualmente. Regenere com: /conclave docs -->
<!-- Gerado em: 2026-04-26 | Última sessão: 2026-04-26 -->

# 📘 Conclave — Tutorial & Referência

> Sistema de orquestração multi-agente. Crie e execute squads de IA para qualquer projeto a partir de qualquer diretório.

---

## ⚡ Como funciona (em 3 linhas)

1. **Squads** são pipelines de agentes especializados. Cada squad tem um objetivo, agentes com persona, e uma sequência de steps executados automaticamente.
2. **Skills** são módulos reutilizáveis (integrações MCP, frameworks de escrita, ferramentas de imagem) que qualquer agente pode usar.
3. **GAIA Subroutines** são observadores de sistema que fecham os loops de aprendizado entre as runs — automaticamente.

---

## 🖥️ Todos os Comandos `/conclave`

### Navegação

| Comando | O que faz |
|---|---|
| `/conclave` | Abre o menu principal interativo |
| `/conclave menu` | Alias para o menu principal |
| `/conclave help` | Exibe este guia de referência rápida |
| `/conclave where` | Mostra os caminhos resolvidos GLOBAL_ROOT e PROJECT_ROOT (debug) |
| `/conclave init` | Inicializa o Conclave em qualquer pasta (cria `_conclave/`, squads/, skills/) |

### Squads

| Comando | O que faz |
|---|---|
| `/conclave create <descrição>` | Cria um novo squad (chama o Arquiteto — wizard interativo) |
| `/conclave list` | Lista todos os squads do projeto com status |
| `/conclave run <nome>` | Executa o pipeline completo de um squad |
| `/conclave edit <nome> <mudanças>` | Modifica um squad existente via Arquiteto |
| `/conclave delete <nome>` | Remove um squad (pede confirmação, cria backup antes) |

### Skills

| Comando | O que faz |
|---|---|
| `/conclave skills` | Abre o menu de skills (ver, instalar, criar, remover) |
| `/conclave install <nome>` | Instala uma skill do catálogo no projeto atual |
| `/conclave uninstall <nome>` | Remove uma skill instalada |

### Perfil & Memória

| Comando | O que faz |
|---|---|
| `/conclave edit-company` | Edita o perfil da empresa (company.md) |
| `/conclave show-company` | Exibe o perfil da empresa atual |
| `/conclave settings` | Abre preferências do projeto ou globais |
| `/conclave reset` | Reseta configuração local (com backup automático) |
| `/conclave recall <busca>` | Busca em todos os arquivos de memória (logs, runs, user model) |
| `/conclave model` | Exibe ou atualiza o user model inferido |

### Documentação

| Comando | O que faz |
|---|---|
| `/conclave docs` | 📘 Regenera este TUTORIAL.md com dados ao vivo do sistema |

### GAIA Subroutines

| Comando | O que faz |
|---|---|
| `/conclave tide` | 🌊 **POSEIDON** — agrega streams JSONL, detecta padrões, propõe ações |
| `/conclave curate` | ☀️ **APOLLO** — curadoria de memória: deduplicação, arquivamento, conflitos |
| `/conclave forge` | 🔨 **HEPHAESTUS** — revisa candidatos de manufatura (skills, templates, agentes) |
| *(passivo)* | 🦉 **MINERVA** — roteamento por intenção em linguagem natural |
| *(passivo)* | 🌱 **ELEUTHIA** — verifica drift do company.md a cada 60 dias |
| *(passivo)* | 🏹 **ARTEMIS** — propaga sinais entre squads via gossip bus |

---

## 🤖 GAIA Subroutines — Detalhe

Inspiradas na franquia Horizon Zero Dawn (Guerrilla Games). São observadores de sistema — nunca escrevem em arquivos do usuário sem aprovação explícita.

**HADES Veto Cláusula:** Nenhuma subroutine muta arquivos do usuário sem aprovação por ação. Observam, propõem, fazem handoff. O usuário fecha todo loop de mutação.

| Ícone + Codename | Papel | Invocação |
|---|---|---|
| 🌊 **POSEIDON** | Tide Observer — agrega streams, detecta correntes | `/conclave tide` |
| ☀️ **APOLLO** | Memory Curator — dedup, arquivo, conflitos | `/conclave curate` |
| 🦉 **MINERVA** | Intent Listener — roteamento NLU contextual | passivo (substitui router estático) |
| 🔨 **HEPHAESTUS** | Manufacturing Watch — propõe skills, templates, promoções | `/conclave forge` + advisory no menu |
| 🌱 **ELEUTHIA** | Profile Refresh Cradle — drift check do company.md (60 dias) | passivo (toda invocação) |
| 🏹 **ARTEMIS** | Squad Gossip Bus — propaga sinais cross-squad | passivo (D4.5 emission + Tier 2) |

---

## 🏟️ Squads Ativos (6)

Cada squad tem: `squad.yaml` (pipeline), `squad-party.csv` (agentes), `agents/` (personas), `_memory/` (aprendizados), `output/` (artefatos gerados).

| Squad | Código | Domínio | Descrição |
|---|---|---|---|
| 💠 Sexy Content Engine | `sexy_content` | linkedin | Motor de conteúdo de alto impacto para LinkedIn. Produz Posts, Carrosséis e Artigos na voz do Doug. |
| 🎠 From HTML to Carousel | `from-html-to-carousel` | carousel | Traduz textos densos em carrosséis visuais (5-10 slides) para LinkedIn e Instagram. |
| 🔷 Refract | `refract` | engineering | Estúdio de engenharia cross-platform. Web-first (PWA/TS/Three.js/Python) com portabilidade gated para macOS e Windows. |
| 🧪 Lazarus Protocol | `lazarus` | research | Performance humana, biomecânica e biohacking. Integra dados de saúde offline (.csv). |
| ⚖️ Conselho de Teste | `council_test` | test | Squad para validar o protocolo de Resumo Estruturado do Conselho. |
| 📊 Data Ops | `data_ops` | data | Gestão do ciclo de vida completo de dados: criação, limpeza, engenharia, análise e envelopamento. |

---

## 🛠️ Skills Catalog (21)

Skills são módulos que agentes invocam por nome. Tipos: MCP (integração externa), `prompt` (framework de escrita/raciocínio), `script` (geração de artefatos), `hybrid`.

| Skill | Descrição |
|---|---|
| `apify` | Web scraping e automação. Extrai dados de qualquer site via Apify platform. |
| `battlecard-generator` | Gera battlecards competitivos: comparações head-to-head estruturadas. |
| `blotato` | Publicação e agendamento em redes sociais: Instagram, LinkedIn, Twitter/X, TikTok, YouTube. |
| `brand-voice-extractor` | Extrai o DNA de comunicação de uma marca a partir de conteúdo público. |
| `canva` | Cria, busca, preenche e exporta designs do Canva. |
| `competitor-intel` | Framework de pesquisa competitiva estruturada dado um nome ou URL de concorrente. |
| `conclave-agent-creator` | Guia criação e manutenção de arquivos de agentes seguindo boas práticas do Conclave. |
| `conclave-skill-creator` | Cria novas skills do Conclave, melhora skills existentes, roda evals e benchmarks. |
| `create-html-carousel` | Gera carrosséis HTML prontos para LinkedIn (1080×1080px por slide). |
| `creative-long-form` | Framework de escrita criativa e narrativa longa derivado da voz autoral do Doug. |
| `firecrawl` | Fallback de scraping para páginas JS-renderizadas e sites com anti-bot. |
| `icp-profiler` | Define o Ideal Customer Profile (ICP) de um produto ou serviço. |
| `image-ai-generator` | Gera imagens via Openrouter API usando modelos de IA de imagem. |
| `image-creator` | Renderiza HTML/CSS em imagens prontas para produção via Playwright. |
| `image-fetcher` | Adquire assets visuais de múltiplas fontes: busca web, bancos de imagens. |
| `industry-scanner` | Análise de paisagem industrial em 5+ dimensões: players, tendências, lacunas. |
| `instagram-publisher` | Publica carrosséis de imagens no Instagram a partir de arquivos locais. |
| `landing-page-intel` | Analisa qualquer landing page: posicionamento, copy, estratégia de conversão. |
| `linkedin-writing` | Framework operacional de escrita para LinkedIn — voz autoral do Douglas Moura. |
| `resend` | Envia emails via Resend MCP server oficial. |
| `template-designer` | Seleção de templates visuais para agentes de design de imagens. |

---

## 🏛️ Arquitetura

```
Conclave (modo híbrido)
│
├── Runtime global (~/.conclave/)          ← compartilhado entre projetos
│   ├── core/                              ← runner, architect, skills engine, agents GAIA
│   ├── skills_catalog/                    ← catálogo de skills (read-only)
│   └── _memory/                           ← global-preferences.md, user-model.md
│
└── Contexto por projeto ($CWD/)
    ├── _conclave/
    │   ├── _memory/                       ← company.md, preferences.md, session_logs.md
    │   └── logs/                          ← audit.jsonl (append-only)
    ├── squads/                            ← squads do projeto
    └── skills/                            ← skills instaladas no projeto
```

**Cascade de preferências (maior vence):**
`step-level` > `squad memories.md` > `preferences.md` > `global-preferences.md` > defaults do agente

**Proteção de escrita:** qualquer flow que reescreve arquivos do usuário cria backup `.bak-{YYYYMMDD-HHmmss}` antes.

---

## 📅 Última Sessão Registrada

`2026-04-26` — veja o histórico completo em [`_conclave/state/memory/session_logs.md`](_conclave/state/memory/session_logs.md)

---

*Regenerado automaticamente por `/conclave docs`. Fonte: squad.yaml, skills/\*/SKILL.md, \*.agent.md, session_logs.md*
