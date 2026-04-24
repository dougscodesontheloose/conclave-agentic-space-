<div align="center">

# ⚔️ Conclave

### Multi-Agent Orchestration Framework for AI-Powered Workflows

**Create AI agent squads that work together — right from your IDE.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Getting Started](#-getting-started) • [How It Works](#-how-it-works) • [Creating Squads](#-creating-squads) • [Architecture](#-architecture) • [Skills Catalog](#-skills-catalog) • [Contributing](#-contributing)

</div>

---

## 🧠 What is Conclave?

Conclave is an **open-source, IDE-native multi-agent orchestration framework** that lets you build, manage, and run teams ("squads") of AI agents directly from your code editor.

Instead of prompting a single AI model, you design **specialized agents** with distinct roles, personas, and tools — then orchestrate them through **automated pipelines** with human-in-the-loop checkpoints.

### Why Conclave?

| Traditional AI Workflow | Conclave |
|---|---|
| One prompt → one response | Multi-agent pipelines with specialized roles |
| Context lost between sessions | Persistent memory per squad, per agent |
| Manual copy-paste between tools | Automated handoffs between agents |
| Generic outputs | Brand-aware, preference-respecting outputs |
| No quality control | Built-in review agents and checkpoints |

---

## ⚡ Getting Started

### Prerequisites

- An AI-powered IDE or terminal (VS Code + Copilot, Cursor, Claude Code, Gemini CLI, etc.)
- Node.js 18+ (for MCP servers and tooling)
- Python 3.10+ (optional, for data/analytics skills)

### Quick Start

1. **Clone this repository:**
   ```bash
   git clone https://github.com/dougscodesontheloose/conclave-agentic-space-.git
   cd conclave-agentic-space-
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure your API keys** (optional, for web scraping skills):
   ```bash
   cp .mcp.json.example .mcp.json
   # Edit .mcp.json with your API keys
   ```

4. **Open in your IDE and type:**
   ```
   /conclave
   ```

5. **Complete the onboarding:** Conclave will ask your name, preferred language, and company/project details to personalize all outputs.

---

## 🔧 How It Works

### The Core Loop

```
You describe what you need
       ↓
The Architect agent designs a squad
       ↓
Specialized agents execute a pipeline
       ↓
Checkpoints pause for your approval
       ↓
Outputs are saved and memories updated
```

### Key Concepts

- **Squad** — A team of AI agents organized around a goal (e.g., "LinkedIn content production", "data analysis", "cross-platform engineering")
- **Agent** — A specialized AI persona with a defined role, tools, and communication style (defined in `.agent.md` files)
- **Pipeline** — A sequence of steps that agents execute in order, with checkpoints for human decisions
- **Memory** — Persistent context that improves outputs over time (per-squad learnings, user preferences, brand identity)
- **Skill** — A reusable capability that any agent can leverage (e.g., web scraping, SEO analysis, email drafting)

---

## 🏗️ Creating Squads

### Via Menu

```
/conclave
→ Select "Create a new squad"
→ Describe what you need in natural language
```

### Via Command

```
/conclave create a squad for writing LinkedIn posts about AI
/conclave create a squad for analyzing sales pipeline data
/conclave create a squad for building cross-platform apps
```

The **Architect** agent will:
1. Ask clarifying questions about your needs
2. Design the squad structure (agents, pipeline, tools)
3. Generate all configuration files
4. Set up the squad's memory and output directories

### Running a Squad

```
/conclave run <squad-name>
```

The pipeline executes automatically, pausing only at decision checkpoints where your input is needed.

---

## 📁 Architecture

```
conclave/
├── _conclave/                    # Core system (don't modify manually)
│   ├── core/                     # Runner, Architect, Skills Engine, Security Policy
│   │   ├── runner.pipeline.md    # Pipeline execution instructions
│   │   ├── architect.agent.yaml  # Squad creation agent
│   │   ├── skills.engine.md      # Skill management system
│   │   ├── security.policy.md    # Security and privacy rules
│   │   ├── templates/            # Onboarding templates
│   │   └── schemas/              # Validation schemas
│   ├── config/                   # Tool configurations (Playwright, etc.)
│   ├── scripts/                  # System scripts (validator, reindexer, disk guardian)
│   └── _memory/                  # Persistent user memory
│       ├── company.md            # Your company/project profile
│       ├── preferences.md        # Your preferences (language, IDEs)
│       ├── global-preferences.md # Cross-squad design & writing rules
│       ├── user-model.md         # AI-inferred user behavior patterns
│       ├── visual-identity.md    # Visual brand system
│       ├── visual-voice.md       # Design language guide
│       └── linkedin-insights.md  # Social media audience data
│
├── squads/                       # Your squads live here
│   └── <squad-name>/
│       ├── squad.yaml            # Squad configuration
│       ├── squad-party.csv       # Agent roster
│       ├── agents/               # Agent persona files (.agent.md)
│       ├── pipeline/             # Pipeline steps (optional)
│       ├── _memory/              # Squad-specific learnings
│       └── output/               # Generated outputs
│
├── skills/                       # Installed skills (shared catalog)
│   ├── create-html-carousel/     # HTML carousel builder
│   ├── competitor-intel/         # Competitive intelligence
│   ├── brand-voice-extractor/    # Brand voice analysis
│   └── ...                       # 20+ skills included
│
├── .agents/                      # Global agent definitions & skill library
│   └── skills/                   # 100+ skills for GTM, sales, content, data
│
├── ref_visual_style/             # Your visual reference images
├── ref_brand-style/              # Your brand writing references
│
├── AGENTS.md                     # IDE instructions (Gemini/Antigravity)
├── CLAUDE.md                     # IDE instructions (Claude Code)
├── .cursorrules                  # IDE instructions (Cursor)
├── .mcp.json                     # MCP server configuration
└── .editorconfig                 # Code style rules
```

### Hybrid Mode

Conclave supports running across multiple projects:

```bash
# Initialize Conclave in any folder
cd ~/Documents/MyProject
/conclave init
```

This creates a local `_conclave/` with its own memory, while sharing the global runtime (core, skills catalog) from this hub repository.

### Preference Cascade

Preferences are resolved in order (highest wins):

1. **Step-level instructions** — inline in the pipeline step
2. **Squad memories** — `squads/{name}/_memory/memories.md`
3. **Project preferences** — `_conclave/_memory/preferences.md`
4. **Global preferences** — `_conclave/_memory/global-preferences.md`
5. **Agent defaults** — built into the agent's `.agent.md`

---

## 🧩 Skills Catalog

Conclave ships with **100+ skills** organized by category:

### 🔍 Research & Intelligence
- Competitor intelligence, ad monitoring, review scraping
- SEO analysis, domain profiling, content auditing
- Industry scanning, trend monitoring

### 📧 Outreach & Sales
- Cold email campaigns, LinkedIn messaging
- Lead qualification, ICP identification
- Signal detection (hiring, funding, leadership changes)

### ✍️ Content & Creative
- LinkedIn post writing, carousel creation
- HTML presentations, campaign briefs
- Brand voice extraction, content asset generation

### 📊 Data & Analytics
- Pipeline review, campaign analysis
- Churn detection, expansion signals
- Meeting prep, sales coaching

### 🛠️ Engineering & DevOps
- Code review, Python environment management
- Multi-agent collaboration, token efficiency
- Systematic debugging

### Browse and install skills:

```
/conclave skills
```

---

## 🛡️ Security

- **API keys** are stored in `.mcp.json` (gitignored by default)
- **Browser sessions** are stored in `_conclave/_browser_profile/` (gitignored)
- **No telemetry** — everything runs locally
- **Privacy tagging** — the security policy enforces `privacy: internal` headers on sensitive files
- **Overwrite protection** — any file rewrite creates a `.bak-{timestamp}` backup first

---

## 🌐 IDE Compatibility

Conclave is pre-configured for multiple IDEs:

| IDE | Config File | Status |
|---|---|---|
| VS Code / Cursor | `.vscode/settings.json`, `.cursorrules` | ✅ Ready |
| Claude Code | `CLAUDE.md`, `.claude/` | ✅ Ready |
| Gemini / Antigravity | `AGENTS.md` | ✅ Ready |
| Any IDE with MCP support | `.mcp.json` | ✅ Ready |

---

## 📦 Included Example Squads

This repository ships with several example squads to get you started:

| Squad | Purpose | Agents |
|---|---|---|
| `sexy_content` | LinkedIn content production | Researcher, Copywriter, Designer, Auditor, Publisher, Prompt Engineer, Renderer |
| `data_ops` | Data engineering & analytics | Senior Data Analyst, Senior Data Scientist |
| `refract` | Cross-platform app development | Architect, Web Dev, Python Dev, Swift Dev, .NET Dev, Visual Parity Auditor |
| `from-html-to-carousel` | HTML → LinkedIn carousel conversion | Specialized conversion agents |
| `council_test` | Testing squad for review features | Council agents |
| `lazarus` | Health & performance tracking | Analytics agent |

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Ideas

- **Create a new skill** — Add a skill to `.agents/skills/` following the SKILL.md format
- **Build a new example squad** — Design a squad for a use case we don't cover yet
- **Improve documentation** — Help make the onboarding smoother
- **Report bugs** — Open an issue with reproduction steps
- **Translate** — Help translate agent prompts and docs to other languages

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ by [Doug](https://github.com/dougscodesontheloose)**

*Conclave: because one AI is good, but a squad is better.*

</div>
