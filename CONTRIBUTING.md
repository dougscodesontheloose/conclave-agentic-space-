# Contributing to Conclave

Thank you for your interest in contributing to Conclave! 🎉

## How to Contribute

### 🐛 Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/dougscodesontheloose/conclave-agentic-space-/issues)
2. Open a new issue with:
   - Clear title describing the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (IDE, OS, Node version)

### 💡 Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the use case and why it would be valuable
3. If possible, sketch how it might work (commands, file structure, etc.)

### 🔧 Submitting Changes

1. **Fork** the repository
2. **Create a branch** for your change: `git checkout -b feature/my-awesome-feature`
3. **Make your changes** following the style guidelines below
4. **Test your changes** by running the validator: `python _conclave/scripts/validate_conclave.py`
5. **Commit** with a clear message: `git commit -m "feat: add X capability to Y"`
6. **Push** and open a Pull Request

### 📝 Style Guidelines

- **Markdown**: Use GitHub Flavored Markdown. Prefer lists over dense paragraphs.
- **Indentation**: 2 spaces for YAML/JSON/JS/TS, 4 spaces for Python.
- **Agent files**: Follow the `.agent.md` format documented in `_conclave/core/schemas/`.
- **Skills**: Follow the `SKILL.md` format — see existing skills in `.agents/skills/` for examples.
- **File naming**: Use kebab-case for directories and files (`my-cool-skill/`, `step-01-research.md`).

### 🧩 Creating a New Skill

1. Create a directory in `.agents/skills/your-skill-name/`
2. Add a `SKILL.md` with YAML frontmatter (name, description) and detailed instructions
3. If needed, add `scripts/`, `examples/`, or `resources/` subdirectories
4. Test the skill by using it in a squad pipeline

### 🏗️ Creating a New Example Squad

1. Create a directory in `squads/your-squad-name/`
2. Add `squad.yaml` (pipeline configuration)
3. Add `squad-party.csv` (agent roster)
4. Add agent files in `agents/` subdirectory
5. Add `_memory/memories.md` (empty template)
6. Test by running: `/conclave run your-squad-name`

## Code of Conduct

Be respectful, constructive, and inclusive. We're building tools that empower people — let's embody that in how we collaborate.

## Questions?

Open an issue or start a discussion. We're happy to help!
