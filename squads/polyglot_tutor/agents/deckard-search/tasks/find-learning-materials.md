---
task: "Find Learning Materials"
order: 1
input: |
  - focus: O tópico ou foco de estudo atual
output: |
  - links: Lista de URLs categorizados
  - summary: Resumo de por que o material é bom
---

# Find Learning Materials

Encontra recursos e ferramentas fáceis para o nível e o idioma especificados.

## Process
1. Analisa o foco definido no input.
2. Navega e busca vídeos/artigos que ensinem o tópico.
3. Compila os links e resume os pontos fortes.

## Output Format
```yaml
materials:
  - url: "..."
    type: "video|article"
    reason: "..."
```

## Output Example
> Use as quality reference, not as rigid template.

Encontrei 3 vídeos essenciais sobre verbos irregulares em espanhol que usam storytelling em vez de tabelas.
Vídeo 1: [Link] - Foca na pronúncia com moradores locais.

## Quality Criteria
- [ ] Links são funcionais
- [ ] Material tem alta retenção
- [ ] Aderência ao foco

## Veto Conditions
Reject and redo if ANY are true:
1. Menos de 3 referências encontradas.
2. Material predominantemente monótono ou sem aplicação prática.
