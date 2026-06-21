---
name: arxiv-paper-scanner
description: >
  Pesquisa e recuperação de papers acadêmicos via arXiv REST API e Semantic Scholar.
  Busca por keyword, autor, categoria ou ID. Gera BibTeX, analisa citações, descobre papers relacionados,
  e monta workflows completos de pesquisa acadêmica. Sem API key — usa apenas curl e Python stdlib.
type: tool_orchestration
tags: [research, data, analytics]
---

# arXiv Paper Scanner

Pesquise, descubra e analise papers acadêmicos usando a API gratuita do arXiv e o Semantic Scholar — sem API keys, sem dependências externas.

**Core principle:** Pesquisa acadêmica rigorosa exige verificação programática. Nunca gere citações de memória — sempre busque via API.

## When to Use

- "Busque papers sobre [tópico] no arXiv"
- "Quero ver os papers mais recentes sobre [área]"
- "Encontre papers do autor [nome]"
- "Gere BibTeX para este paper"
- "Quantas citações tem o paper [ID]?"
- Qualquer request que envolva pesquisa acadêmica, papers, ou citações

**Auto-trigger:** Sempre que o usuário mencionar arXiv, papers acadêmicos, ou pedir referências científicas.

## Prerequisites

### Environment Variables

```
Nenhuma — APIs são gratuitas e sem autenticação.
```

### Dependencies

```bash
# Nenhuma. Usa curl + Python stdlib (xml.etree.ElementTree, json).
# Opcional: pip install requests  (para DOI→BibTeX)
```

## Inputs

| Input | Required | Description |
|---|---|---|
| **Query de busca** | Yes | Tópico, keyword, autor, ou arXiv ID |
| **Tipo de busca** | No | all/title/author/abstract/category (default: all) |
| **Quantidade** | No | Número de resultados (default: 5, max: 30000) |
| **Ordenação** | No | relevance/submittedDate/lastUpdatedDate (default: relevance) |

## Phase 0: Intake

1. **Qual o tópico ou paper específico?** — obrigatório
2. **Quantos resultados deseja?** — default 5
3. **Quer buscar por autor, título, categoria, ou busca geral?** — default: geral

> **Regra:** Se o usuário fornecer um arXiv ID direto (ex: 2402.03300), pule para a busca específica.

## Phase 1: Busca de Papers

### Step 1A: Busca via arXiv API

```bash
# Busca geral
curl -s "https://export.arxiv.org/api/query?search_query=all:QUERY&max_results=5&sortBy=submittedDate&sortOrder=descending" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom'}
root = ET.parse(sys.stdin).getroot()
for i, entry in enumerate(root.findall('a:entry', ns)):
    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
    arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    published = entry.find('a:published', ns).text[:10]
    authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
    summary = entry.find('a:summary', ns).text.strip()[:200]
    cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
    print(f'{i+1}. [{arxiv_id}] {title}')
    print(f'   Authors: {authors}')
    print(f'   Published: {published} | Categories: {cats}')
    print(f'   Abstract: {summary}...')
    print(f'   PDF: https://arxiv.org/pdf/{arxiv_id}')
    print()
"
```

### Prefixos de Busca

| Prefix | Busca em | Exemplo |
|---|---|---|
| `all:` | Todos os campos | `all:transformer+attention` |
| `ti:` | Título | `ti:large+language+models` |
| `au:` | Autor | `au:vaswani` |
| `abs:` | Abstract | `abs:reinforcement+learning` |
| `cat:` | Categoria | `cat:cs.AI` |

### Operadores

```
# AND (default com +)
search_query=all:transformer+attention

# OR
search_query=all:GPT+OR+all:BERT

# AND NOT
search_query=all:language+model+ANDNOT+all:vision
```

### Step 1B: Busca por ID Específico

```bash
curl -s "https://export.arxiv.org/api/query?id_list=2402.03300"
```

## Phase 2: Análise de Impacto (Semantic Scholar)

### Step 2A: Citações e Métricas

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:PAPER_ID?fields=title,authors,citationCount,referenceCount,influentialCitationCount,year,abstract" | python3 -m json.tool
```

### Step 2B: Papers que Citaram Este

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:PAPER_ID/citations?fields=title,authors,year,citationCount&limit=10" | python3 -m json.tool
```

### Step 2C: Referências do Paper

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:PAPER_ID/references?fields=title,authors,year,citationCount&limit=10" | python3 -m json.tool
```

### Step 2D: Recomendações

```bash
curl -s -X POST "https://api.semanticscholar.org/recommendations/v1/papers/" \
  -H "Content-Type: application/json" \
  -d '{"positivePaperIds": ["arXiv:PAPER_ID"], "negativePaperIds": []}' | python3 -m json.tool
```

## Phase 3: Geração de BibTeX

```bash
curl -s "https://export.arxiv.org/api/query?id_list=PAPER_ID" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
root = ET.parse(sys.stdin).getroot()
entry = root.find('a:entry', ns)
if entry is None: sys.exit('Paper not found')
title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
authors = ' and '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
year = entry.find('a:published', ns).text[:4]
raw_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
cat = entry.find('arxiv:primary_category', ns)
primary = cat.get('term') if cat is not None else 'cs.LG'
last_name = entry.find('a:author', ns).find('a:name', ns).text.split()[-1]
print(f'@article{{{last_name}{year}_{raw_id.replace(\".\", \"\")}},')
print(f'  title     = {{{title}}},')
print(f'  author    = {{{authors}}},')
print(f'  year      = {{{year}}},')
print(f'  eprint    = {{{raw_id}}},')
print(f'  archivePrefix = {{arXiv}},')
print(f'  primaryClass  = {{{primary}}},')
print(f'  url       = {{https://arxiv.org/abs/{raw_id}}}')
print('}')
"
```

## Phase N: Output

### Output Format

| Output | Format | Location |
|---|---|---|
| **Lista de papers** | Tabela markdown | Exibido ao usuário |
| **BibTeX entries** | `.bib` format | Arquivo se solicitado |
| **Análise de citações** | Tabela markdown | Exibido ao usuário |

### Categorias Comuns

| Categoria | Campo |
|---|---|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation and Language (NLP) |
| `cs.CV` | Computer Vision |
| `cs.LG` | Machine Learning |
| `cs.CR` | Cryptography and Security |
| `stat.ML` | Machine Learning (Statistics) |

## Cost

| Component | Cost |
|---|---|
| arXiv API | Free |
| Semantic Scholar API | Free (1 req/sec, 100/sec com API key) |
| LLM reasoning | Free (incluído na sessão) |

## Error Handling

| Failure Mode | Detection | Recovery |
|---|---|---|
| **arXiv rate limit** | HTTP 429 ou timeout | Aguardar 3 segundos entre requests |
| **Semantic Scholar rate limit** | HTTP 429 | Aguardar 1 segundo, retry |
| **Paper não encontrado** | XML vazio ou sem entries | Informar ao usuário, sugerir busca alternativa |
| **Paper retirado** | Summary contém "withdrawn" | Avisar o usuário que o paper foi retirado |

**Principle:** APIs acadêmicas são gratuitas mas têm rate limits agressivos. Sempre respeitar intervalos e nunca paralelizar requests.

## Composability

**Receives data from:**
- `research-paper-writer` — papers para referência em documentos acadêmicos

**Feeds into:**
- `research-paper-writer` — citações verificadas e BibTeX
- `content-brief-factory` — referências acadêmicas para conteúdo técnico

**Integration pattern:** Usado como primeiro passo em qualquer workflow que requer fundamentação acadêmica.

## Memory & Learning

After each execution, persist the following to the squad's `memories.md`:

| What to Save | Format | Example |
|---|---|---|
| **Papers relevantes** | `[OPERACIONAL]: arxiv-paper-scanner — Paper [ID] sobre [tópico] tem [N] citações` | `arxiv-paper-scanner — Paper 2402.03300 sobre GRPO tem 150 citações` |
| **Categorias úteis** | `[OPERACIONAL]: arxiv-paper-scanner — Categoria [cat] relevante para [contexto]` | `arxiv-paper-scanner — cs.CL relevante para NLP research` |
| **Autores-chave** | `[ESTRATÉGICO]: arxiv-paper-scanner — Autor [nome] é referência em [área]` | `arxiv-paper-scanner — Vaswani é referência em attention mechanisms` |

**Rules:**
- Only save **reusable** learnings (apply the Dialectical Memory filter)
- Do not log raw execution data — save the *insight*, not the *log*
- If a learning contradicts a previous memory, update the previous entry

## Quality Gate

Before delivering the final output, verify:

- [ ] **Citações verificadas:** Cada paper mencionado existe e foi confirmado via API
- [ ] **IDs corretos:** arXiv IDs estão no formato correto (YYMM.NNNNN)
- [ ] **Dados atuais:** Resultados refletem papers recentes (verificar data)
- [ ] **User checkpoint:** Apresentar resumo dos papers encontrados antes de finalizar

**If any check fails:** Re-executar a busca com parâmetros ajustados.
