# Internal Evidence Resweep

## Objetivo

Rodada interna feita depois da varredura ampliada no FamilySearch. O objetivo foi reabrir OCR, imagens e fichas privadas para procurar discriminadores que permitam buscas por evento, local e filiacao.

## Achados novos ou reforcados

### Joao Moura da Silva

- Nascimento confirmado em `1940-05-01`.
- Naturalidade confirmada em `Alagoas`.
- Pais confirmados: `Manoel Porfirio da Silva` e `Luiza Maria da Conceicao`.
- Casamento com `Maria das Gracas da Silva` registrado no Rio de Janeiro, 14a Circunscricao, livro `1.B.R.13`, folha `235`, termo `3835`.
- Casamento religioso citado na `Paroquia de Santo Sepulcro`, em Cascadura/RJ.
- Municipio de nascimento em Alagoas ainda nao apareceu.

### Maria das Gracas da Silva

- Nascimento confirmado em `1947-12-24`.
- Naturalidade confirmada em `Pernambuco`.
- Pais confirmados: `Jose Alfredo da Silva` e `Benedita da Costa Silva`.
- Itambe/PE vira hipotese forte para nascimento porque os pais dela nasceram e casaram nesse municipio, mas ainda nao e prova direta do nascimento dela.

### Linha Jose Alfredo / Benedita

- Casamento localizado em `Itambe/PE`, `1o Distrito`, realizado em `1946-10-26`.
- Registro: livro `9`, folha `93`, termo `281`.
- Jose Alfredo da Silva: nascido nesse municipio em `1915-02-15`.
- Benedita Elias da Costa: nascida nesse municipio em `1916-10-08`.
- Localidade interna citada: `Vila de Ibiranga` ou leitura proxima; precisa validacao paleografica.

### Pedro Jacinto de Paula

- Obito registrado no Rio de Janeiro/RJ, 8a Circunscricao, Engenho Velho/Tijuca.
- Registro: livro `515`, folha `73`, termo `79812`.
- Naturalidade confirmada como `Espirito Santo`.
- Pais confirmados: `Sebastiao Jacinto de Paula` e `Alvina Margarida da Conceicao`.
- A forma forte continua sendo `Pedro Jacinto de Paula`; `Pedro Teixeira de Paula` aparece como conflito em certidao posterior.

### Herotildes Teixeira de Paula

- A certidao de nascimento de Angela confirma o nome `Herotildes Teixeira de Paula`.
- Pais provaveis, a validar em imagem melhor: `Sebastiao Teixeira` e `Maria Teixeira da Rocha`.
- Isso muda a busca: agora a frente de Herotildes deve usar os pais como filtro, nao apenas o nome dela.

## Matriz de busca atualizada

| Alvo | Busca principal | Filtro novo | Fonte prioritaria |
|---|---|---|---|
| Joao Moura da Silva | nascimento em Alagoas | data `1940-05-01`; pais Manoel + Luiza | FamilySearch Alagoas, cartorios AL |
| Maria das Gracas da Silva | nascimento em Pernambuco | data `1947-12-24`; pais Jose Alfredo + Benedita; testar Itambe/PE | FamilySearch Pernambuco, Itambe/PE |
| Jose Alfredo da Silva | nascimento em Itambe/PE | data `1915-02-15`; pais Francisco + Valdevina | FamilySearch Pernambuco, cartorio Itambe |
| Benedita Elias da Costa | nascimento em Itambe/PE | data `1916-10-08`; pais Jose Cosme + Filadelfia | FamilySearch Pernambuco, cartorio Itambe |
| Pedro Jacinto de Paula | nascimento no Espirito Santo | idade 61 em 1987; pais Sebastiao Jacinto + Alvina | FamilySearch ES, APEES |
| Herotildes Teixeira de Paula | nascimento/casamento/obito | pais provaveis Sebastiao Teixeira + Maria Teixeira da Rocha | RJ/ES, registros derivados |

## Decisao operacional

A proxima rodada deve abandonar busca por nome solto. Usar combinacoes de:

- nome + data exata;
- nome + pais;
- nome + evento;
- nome + cartorio/livro/termo quando houver.

Prioridade imediata:

1. Buscar `Maria das Gracas da Silva` em Itambe/PE com pais Jose Alfredo e Benedita.
2. Buscar `Joao Moura da Silva` em Alagoas com pais Manoel Porfirio e Luiza Maria.
3. Buscar `Herotildes` usando os pais provaveis `Sebastiao Teixeira` e `Maria Teixeira da Rocha`.
4. Buscar `Pedro Jacinto` no Espirito Santo usando pais e idade calculada.
