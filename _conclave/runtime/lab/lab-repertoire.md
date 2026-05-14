# 📔 Lab Repertoire — Conclave Data Science

Este é o repositório de conhecimentos técnicos, snippets e ferramentas descobertas durante os estudos no Lab. 

## 🛠️ Snippets de Utilidade

### Python (Saneamento de Dados)
```python
import pandas as pd

def quick_clean(df):
    # Remover duplicados
    df = df.drop_duplicates()
    # Padronizar nomes de colunas (snake_case)
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    return df
```

### SQL (Templates)
```sql
-- Template de análise de Cohort
SELECT ...
```

## 📚 Glossário de Estudos
- **Analytics Engineering:** A ponte entre a engenharia de dados bruta e a análise de negócios, focando em modelagem (dbt) e qualidade.

## 🔗 Referências Externas
- [Alura - Formação Data Science](https://www.alura.com.br/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
