---
execution: inline
agent: squads/clube_do_livro/agents/rachael-dialect
---

# Passo 01: Diálogo Dialético

Conduzir a discussão socrática e crítica das ideias contidas nas notas de leitura enviadas pelo <user_name>.

## Context Loading

- ../../_conclave/_memory/soul.md
- ../../_conclave/_memory/learning-loop.md

## Instructions

1. Analise o progresso e as notas fornecidas no Passo 00.
2. Identifique os argumentos centrais e teses do autor do livro correspondentes a essas páginas.
3. Desenvolva uma reflexão crítica, questionando as premissas do autor ou expondo trade-offs/limites da ideia.
4. Conecte o conceito com temas de marketing analytics, growth, desenvolvimento de carreira ou outras leituras anteriores.
5. Redija a provocação em português claro e direto (sem bajular o usuário com termos como "excelente").
6. Encerre com **uma única pergunta de reflexão profunda** para o <user_name> interagir.

## Output Format

```markdown
### 🏛️ Interlocução Crítica — Rachael Dialect

[Análise e reflexão estruturada do capítulo/conceito...]

*Trade-off / Limitação:*
- [Descrever o contraponto ou custo oculto do conceito]

*Ponte de Aplicação:*
- [Relacionar o conceito com dados, performance ou polimatia]

👉 [Única pergunta direcionada ao <user_name> para debate]
```

## Output Example

```markdown
### 🏛️ Interlocução Crítica — Rachael Dialect

A premissa do autor em *A Startup Enxuta* sobre o Produto Mínimo Viável (MVP) assume que o custo de lançar algo imperfeito é sempre menor do que o custo de planejar em excesso. 

No entanto, no contexto de **Marketing Analytics** e marcas com alta exposição digital, um MVP excessivamente falho pode erodir a confiança na marca e gerar dados de feedback ruidosos (viesados por bugs de usabilidade e não pelo desinteresse no valor principal).

Como você ponderaria o trade-off entre velocidade de aprendizado e integridade da coleta de dados de performance no seu projeto atual?
```

## Veto Conditions

1. Não concordar de forma automática com o autor do livro ou com a anotação do <user_name>.
2. Não fazer mais de uma pergunta de encerramento para não sobrecarregar o usuário.
3. Não divagar em conceitos abstratos desvinculados do livro ou do perfil do <user_name>.

## Quality Criteria

- [ ] Apresentou pelo menos uma perspectiva crítica ou trade-off da leitura?
- [ ] Conectou o assunto da leitura com os temas de interesse do <user_name> (analytics, performance, polimatia)?
- [ ] Encerrou com uma pergunta cirúrgica sem soar amigável ou bajuladora por padrão?

<!-- Padding para validação de infraestrutura ---------------------------------------------------------------------------------------------------- -->
 -->
 -->
