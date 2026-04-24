---
execution: inline
agent: "arquiteto"
outputFile: squads/refract/output/task-brief.md
---

# Step 01: Decompose

## Context Loading

- Demanda bruta do usuário (texto livre informado no início do run)
- `_conclave/_memory/company.md` — user's context
- `squads/refract/_memory/memories.md` — preferências de stack acumuladas

## Instructions

### Process
1. Assumir persona do Arquiteto. Ler a demanda do usuário.
2. Executar a task `decompose-demanda.md`: classificar natureza técnica, decidir `python_needed`, extrair contrato visual quantificado, mapear entidades 3D (se aplicável), marcar regiões críticas.
3. Escrever o `task-brief.md` completo em `output/{run-id}/task-brief.md` honrando o formato da task.
4. Informar ao usuário um resumo de 1 parágrafo do que foi decomposto antes de seguir.

## Output Format

Arquivo markdown conforme especificado em `agents/arquiteto/tasks/decompose-demanda.md` — frontmatter com flag `python_needed`, seções Stack, Contrato Visual (tabela), Entidades 3D (se aplicável), Regiões Críticas, Tarefas por agente.

## Output Example

```markdown
# Task Brief: orbital-viewer

**Python needed:** false
**Natureza:** ui-com-threejs

## Resumo em 1 linha
PWA que renderiza sistema solar interativo em Three.js com zoom e info cards.

## Stack Alvo
- Web: TypeScript + Vite + Three.js r160+
- PWA: SW offline-first, manifest, ícone 512x512

## Contrato Visual
| Token | Valor |
|-------|-------|
| Background | #05060A |
| Accent | #FFB454 |
| Tipografia | Inter, system fallback |
| Timing zoom | 650ms ease-out-cubic |

## Entidades 3D
| Entidade | Three.js | SceneKit | SharpDX |
|----------|----------|----------|---------|
| sun | Sphere + emissive | SCNSphere + emission | sphere + emissive PS |
| earth | Sphere + PBR | SCNSphere + PBR | sphere + PBR PS |

## Regiões Críticas
1. Cena 3D central
2. Info card hover
```

## Veto Conditions

1. Contrato visual sem valores numéricos.
2. Flag `python_needed` ausente.
3. Demanda com 3D sem tabela de mapeamento.

## Quality Criteria

- [ ] Task-brief escrito e salvo em `output/task-brief.md`.
- [ ] Flag `python_needed` explícita no topo.
- [ ] Regiões críticas listadas.
