---
execution: inline
agent: trinity-copy
inputFile: squads/sexy_content/output/material-bruto.md
outputFile: squads/sexy_content/output/angulos-gerados.md
---

# Step 05: Gerar Ângulos (Trinity Copy)

## Context Loading

Load these files before executing:
- `squads/sexy_content/output/material-bruto.md` — material bruto extraído na pesquisa
- `squads/sexy_content/output/formato-selecionado.md` — formato escolhido (post / carousel / article)
- `pipeline/data/tone-of-voice.md` — voz e estilo do <user_name>
- `pipeline/data/anti-patterns.md` — ângulos e ganchos a evitar

## Instructions

### Process

1. Ler o material bruto e identificar: dado principal, tensão ou paradoxo central, implicação mais provocativa.
2. Ler o formato selecionado — o formato condiciona a profundidade e estrutura de cada ângulo.
3. Gerar exatamente 3 ângulos genuinamente distintos. Distintos = perspectiva diferente, não variação do mesmo argumento.
4. Para cada ângulo: definir perspectiva, escrever o hook (primeira frase que para o scroll), esboçar a estrutura e justificar por que funciona para a voz do <user_name>.
5. Verificar que nenhum ângulo começa com "Você sabia que", "Todo mundo sabe" ou pergunta retórica óbvia.
6. Verificar que ao menos 1 ângulo usa dado/estatística como gancho e ao menos 1 usa perspectiva contraintuitiva ou provocativa.

### Decision Criteria

- Quando o material tem dado forte → priorizar ângulo que abre com o número de forma inesperada.
- Quando o material tem paradoxo ou contradição → esse é o ângulo contraintuitivo.
- Quando formato = article → ângulos precisam sustentar 800+ palavras; evitar ângulos de "insight rápido".
- Quando formato = carousel → ângulo deve se desdobrar em 5–10 slides com progressão narrativa clara.

## Output Format

```markdown
# Ângulos Gerados

## Ângulo 1: [Nome do Ângulo]
**Perspectiva:** [qual aspecto do material está sendo explorado]
**Hook:** "[primeira frase exata — máx 15 palavras]"
**Estrutura:** [como o conteúdo se desenvolve em 3-4 linhas]
**Por que funciona:** [raciocínio estratégico para a voz do <user_name> — 1-2 linhas]

## Ângulo 2: [Nome do Ângulo]
...

## Ângulo 3: [Nome do Ângulo]
...
```

## Output Example

```markdown
# Ângulos Gerados

## Ângulo 1: O Dado Assustador
**Perspectiva:** Usar a estatística de 78% de aumento de produtividade como ponto de virada — o dado que muda a conversa
**Hook:** "78% de aumento de produtividade. Cursor mediu. O debate acabou."
**Estrutura:** Apresenta o dado → Contextualiza o que ele significa para devs → Separa quem vai usar de quem vai reclamar → CTA reflexivo sobre posicionamento
**Por que funciona:** <user_name> opera com dado + narrativa. Esse ângulo respeita a inteligência do leitor e não pede que acredite — mostra o número.

## Ângulo 2: A Redefinição de Cargo
**Perspectiva:** A frase do CEO como Rorschach — o que você vê nela diz tudo sobre como você enxerga IA
**Hook:** "'O dev do futuro é um diretor de agentes.' Você sentiu medo ou alívio?"
**Estrutura:** Cita a frase → Explica as duas leituras possíveis → Apresenta a leitura do <user_name> → Termina com o que separa os dois grupos
**Por que funciona:** É provocativo sem ser apocalíptico. A pergunta binária no hook funciona porque ambas as respostas são válidas — gera comentário.

## Ângulo 3: O Argumento Contraintuitivo
**Perspectiva:** Agentes autônomos não vão acabar com devs mediocres — vão acabar com devs sem opinião
**Hook:** "Agentes de IA não vão substituir devs. Vão substituir devs sem contexto."
**Estrutura:** Desfaz o medo genérico → Redefine o que é insubstituível → Apresenta o novo critério de valor → CTA sobre o que você está fazendo para desenvolver contexto
**Por que funciona:** Contraintuitivo na dose certa — não nega o impacto, redireciona o que importa. É o tipo de post que o <user_name> assina com autoridade.
```

## Veto Conditions

Reject and redo if ANY are true:
1. Os 3 ângulos são variações do mesmo argumento — perspectivas genuinamente distintas são obrigatórias.
2. Qualquer hook começa com "Você sabia que", "Todo mundo sabe", pergunta retórica óbvia ou emoji.

## Quality Criteria

- [ ] Exatamente 3 ângulos, cada um com perspectiva claramente distinta
- [ ] Ao menos 1 ângulo usa dado/estatística como gancho
- [ ] Ao menos 1 ângulo é contraintuitivo ou provocativo
- [ ] Todos os hooks têm no máximo 15 palavras e param o scroll sem contexto prévio
- [ ] Estrutura de cada ângulo é específica o suficiente para Trinity Copy executar sem reinterpretação
