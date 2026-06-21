# Visual Identity — Sexy Content Engine

Guia de referência rápida para Flynn Design. Para a versão completa e detalhada, ler
`pipeline/data/<user_name>-visual-voice.md` e `_memory/<user_name>-color-palettes.md`.

---

## A Filosofia em Uma Frase

**Industrialismo Tecnológico com alma** — onde mecanismos internos (grids, tipografia mono,
transparências) convivem com formas orgânicas elegantes, luz volumétrica e respiro.

---

## Pacotes Visuais Disponíveis

| Pacote | Tema que Ativa | Características |
|---|---|---|
| **Transparência Anatômica** | IA, tecnologia, sistemas internos | Blueprints, camadas translúcidas, estrutura visível como elemento estético |
| **Arquitetura da Tensão** | Carreira, estratégia, posicionamento | Assimetria funcional, elementos ancorados nos cantos, tensão visual deliberada |
| **Telemetria & Cockpit** | Dados, métricas, BI, analytics | Grids de dados, displays de leitura, estética de painel de controle |
| **Brutalista Tecnológico** | Tendências, mercado, comportamento | Contraste extremo, tipografia dominante, mínimo de elementos |
| **Soft Minimal Anthropic** | Reflexão, humanidade, filosofia criativa | Paleta neutra, espaço negativo massivo, tipografia serifada opcional |

---

## Regras Tipográficas

**Fontes permitidas (com personalidade):**
- Display/Títulos: Cabinet Grotesk, Clash Display, Neue Montreal, Oswald
- Metadados/Detalhes: Space Mono, JetBrains Mono, Geist Mono
- Opcional (lirismo): Lora, Playfair Display, Editorial New

**Fontes proibidas (sem exceção):**
- Inter, Roboto, Arial, Helvetica, Open Sans, Lato

**Por quê:** Fontes genéricas são associadas a interfaces de sistema — removem a autoria do design.

---

## Elementos Estruturais Obrigatórios

1. **Metadados visíveis**: numeração de slides em monoespaçado — "03 / 08" — em canto discreto
2. **Espaço negativo intencional**: áreas vazias são decisão de design, não falta de conteúdo
3. **Hierarquia clara**: cada slide tem 1 elemento dominante (headline OU dado OU imagem)
4. **Assimetria funcional**: texto âncora em um dos lados, espaço no outro

---

## Cruzamentos Recomendados (Pacote + Paleta)

Para a lista completa de paletas, ler `pipeline/data/color-palettes.md`.

| Pacote | Paleta Óbvia (evitar) | Cruzamento Interessante |
|---|---|---|
| Transparência Anatômica | Azul tech | Cockpit Dark ou Oceânica & Coral |
| Arquitetura da Tensão | Cinza neutro | Brutalista ou Red Energy |
| Telemetria & Cockpit | Preto + ciano | Oceânica ou Biocenose |
| Brutalista Tecnológico | Preto + branco | Red Energy ou Cockpit invertido |
| Soft Minimal Anthropic | Bege claro | Nenhum acento forte — manter minimalismo |

**Regra:** o cruzamento não-óbvio é onde o design se torna único. A combinação óbvia entrega
o esperado — o cruzamento inesperado entrega o memorável.

---

## Dimensões e Especificações

- **Formato:** 1080×1080px por slide (quadrado, padrão LinkedIn)
- **Slides por carrossel:** 6–10 (mínimo 5, máximo 12)
- **Palavras por slide:** máximo 40
- **Skill de renderização:** `create-html-carousel`
- **Output:** `squads/sexy_content/output/carousel.html`

---

## O Slide de Capa

O primeiro slide é o ativo mais importante. Critérios obrigatórios:
- Funciona como imagem autônoma no feed (sem contexto dos outros slides)
- Headline em peso máximo disponível na fonte escolhida
- Elemento visual dominante (não apenas texto)
- Para o scroll antes de qualquer explicação

Se o rascunho mental do slide 1 não passa no critério acima: reescrever o headline antes de renderizar.
