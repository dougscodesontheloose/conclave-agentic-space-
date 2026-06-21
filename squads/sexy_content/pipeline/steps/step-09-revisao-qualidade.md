---
execution: inline
agent: demerzel-audit
inputFile: squads/sexy_content/output/draft-conteudo.md
outputFile: squads/sexy_content/output/revisao.md
---

# Step 09: Revisão de Qualidade (Demerzel Audit)

## Context Loading

Load these files before executing:
- `squads/sexy_content/output/draft-conteudo.md` — conteúdo produzido por Trinity Copy
- `squads/sexy_content/output/carousel.html` — design do carrossel (se formato = carousel)
- `squads/sexy_content/output/formato-selecionado.md` — formato do conteúdo
- `pipeline/data/quality-criteria.md` — rubrica completa de qualidade
- `pipeline/data/tone-of-voice.md` — voz e estilo do <user_name> para comparação

## Instructions

### Process

1. Ler o formato selecionado para saber qual checklist aplicar.
2. Aplicar o checklist de texto abaixo para todos os formatos.
3. Se formato = carousel, aplicar também o checklist visual.
4. Emitir veredicto: APROVADO, COM RESSALVAS ou REPROVADO.
5. Se REPROVADO: listar os itens exatos que falharam nos Veto Conditions, indicar qual step deve refazer.
6. Se COM RESSALVAS: listar ajustes necessários — Trinity Copy ou Flynn Design corrigem inline antes de prosseguir.

### Checklist de Qualidade — Texto (todos os formatos)

- [ ] O hook para o scroll sem contexto prévio?
- [ ] Voz do <user_name> presente? (técnico + narrativo, ponte entre tecnologia e emoção humana)
- [ ] Ausência de clichês corporativos? ("Nesse cenário", "Com isso em mente", "É importante salientar", "No mundo atual")
- [ ] Dado ou estatística presente e contextualizado organicamente?
- [ ] Uma metáfora inusitada (videogame, cultura pop, literatura) presente e bem integrada?
- [ ] CTA gera reflexão ou comentário real — nunca "curte e compartilha"?

### Checklist de Qualidade — Carrossel

- [ ] Nenhum slide passa de 40 palavras?
- [ ] A capa para o scroll sem contexto dos outros slides?
- [ ] A progressão dos slides conta uma história com início, meio e fim?
- [ ] Design não parece template genérico?
- [ ] Metadados visíveis (ex: "03 / 08") em todos os slides?
- [ ] Tipografia com personalidade (sem Inter/Roboto/Arial)?

## Output Format

```markdown
# Revisão de Qualidade

## Veredicto: [APROVADO / COM RESSALVAS / REPROVADO]

## Checklist — Texto
- [x] ou [ ] Hook para o scroll
- [x] ou [ ] Voz do <user_name>
- [x] ou [ ] Sem clichês corporativos
- [x] ou [ ] Dado contextualizado
- [x] ou [ ] Metáfora inusitada
- [x] ou [ ] CTA reflexivo

## Checklist — Carrossel (se aplicável)
- [x] ou [ ] ≤40 palavras/slide
- [x] ou [ ] Capa independente
- [x] ou [ ] Progressão narrativa
- [x] ou [ ] Design autoral
- [x] ou [ ] Metadados visíveis
- [x] ou [ ] Tipografia com personalidade

## Pontos Fortes
- [o que funciona bem]

## Ajustes Necessários
1. [ajuste específico com indicação de onde corrigir]

## Nota Final: X/10
```

## Output Example

```markdown
# Revisão de Qualidade

## Veredicto: COM RESSALVAS

## Checklist — Texto
- [x] Hook para o scroll — "78% de aumento de produtividade. Cursor mediu. O debate acabou." funciona.
- [x] Voz do <user_name> — técnico + narrativo, ponte correu.
- [x] Sem clichês corporativos — limpo.
- [x] Dado contextualizado — estatística do Cursor integrada no parágrafo 2.
- [x] Metáfora inusitada — "como descobrir que você é rápido na corrida, mas não sabe para onde correr" — forte.
- [ ] CTA reflexivo — "O que você está fazendo para desenvolver essa habilidade?" é genérico demais. Poderia ser mais específico sobre o que "desenvolver contexto" significa na prática.

## Pontos Fortes
- Hook abre com dado e não com pergunta retórica — escolha correta.
- A metáfora da corrida é concreta e evita o "universo tech" saturado.

## Ajustes Necessários
1. CTA: substituir por algo mais específico, ex: "Quantos prompts você escreveu hoje que não eram do trabalho?" — força o leitor a contar, não a refletir abstratamente.

## Nota Final: 8/10
```

## Veto Conditions

Reject and redo if ANY are true:
1. Hook começa com pergunta retórica óbvia, emoji genérico ou fórmula "Você sabia que" — rejeitar e devolver ao step-07.
2. Tom genérico sem identidade do <user_name> detectável — ausência de metáfora inusitada + linguagem corporativa = reprovação automática.
3. Slide de carrossel com mais de 50 palavras — limite absoluto, sem exceção.
4. Uso de mais de 3 emojis no mesmo post — sinal de conteúdo de baixa autoridade.

## Quality Criteria

- [ ] Veredicto emitido com justificativa para cada item do checklist
- [ ] Pontos fortes identificados (não apenas críticas)
- [ ] Ajustes necessários são específicos e acionáveis — nunca vagos ("melhorar o tom")
- [ ] Nota final atribuída de 1 a 10 com critério claro
