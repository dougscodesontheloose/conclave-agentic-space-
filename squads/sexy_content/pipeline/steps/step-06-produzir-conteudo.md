---
execution: inline
agent: "trinity-copy"
format: "linkedin-post"
inputFile: squads/sexy_content/output/angulos-gerados.md
outputFile: squads/sexy_content/output/draft-conteudo.md
---

# Step 06: Produzir Conteúdo

## Context Loading

- O ângulo apontado no checkpoint + o formato escolhido (carrossel ou post)
- `pipeline/data/visual-identity.md` e `pipeline/data/research-brief.md` ou habilidades da Laura.

## Instructions

### Process
1. Recupere todas as referências do <user_name>. Dica de colega + Zero clichê.
2. Escreva o conteúdo Markdown no layout aprovado no arquivo da tarefa principal.
3. Garanta que se for carrossel não fira as restrições arquiteturais ("Máx 40 palavras pro painel", "1 Âmbar signal").

## Output Format

```markdown
# Draft (Post)

[Começo...]
```

```markdown
# Draft (Carrossel)

## Slide 1
[Signal]
```

## Output Example

```markdown
# Draft (Carrossel)
## Slide 01 - Capa
**Signal:** CRO sem Analytics é só palpite decorado.
**Context:** O problema não é a cor do botão.

## Slide 02
**Signal:** 88% dos A/B tests dão empate técnico.
**Context:** Fonte: CXL Report 2024.
```

## Veto Conditions

Reject and redo if ANY of these are true:
1. O texto ficou massante (escore visual de clareza explodiu a capacidade do leitor pular as linhas).
2. O Post soa como um artigo acadêmico sem analogias práticas amigáveis.

## Quality Criteria

- [ ] Arquétipo mantido do passo do ângulo.
- [ ] Hook validado.
