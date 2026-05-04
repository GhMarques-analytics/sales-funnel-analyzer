# 📚 Python & Pandas Glossary · Glossário Python & Pandas

> **EN** — Quick reference guide for all functions and concepts used in this project. Use this to explain your code confidently in interviews.
>
> **PT** — Guia de referência rápida de todas as funções e conceitos usados neste projeto. Use para explicar seu código com segurança em entrevistas.

---

## 📦 1. Libraries | Bibliotecas

| Library | Apelido | Para que serve |
|---|---|---|
| `pandas` | `pd` | Manipulação de dados em tabelas (DataFrames). Equivalente ao Excel em código |
| `numpy` | `np` | Operações matemáticas e arrays. Usado principalmente para `seed` de reprodutibilidade |
| `matplotlib.pyplot` | `plt` | Criação de gráficos — o motor principal por baixo de tudo |
| `matplotlib.ticker` | `mtick` | Formatação de eixos de gráficos (ex: mostrar `8%` em vez de `0.08`) |
| `seaborn` | `sns` | Gráficos mais bonitos e estatísticos. Funciona em cima do matplotlib |
| `random` | — | Gera valores aleatórios (nativo do Python, sem instalar) |
| `os` | — | Interage com o sistema de arquivos (criar pastas, verificar caminhos) |
| `datetime` / `timedelta` | — | Trabalha com datas e intervalos de tempo |

---

## 🔢 2. Core Concepts | Conceitos Fundamentais

### `seed` — Reprodutibilidade
```python
np.random.seed(42)
random.seed(42)
```
**PT:** Fixa o ponto de partida do gerador de números aleatórios. Com a mesma seed, o dataset gerado é sempre idêntico — essencial para que qualquer pessoa que clone o repositório obtenha os mesmos resultados.

**EN:** Fixes the starting point of the random number generator. Same seed = same dataset every time — critical for reproducibility.

---

### `DataFrame`
**PT:** A estrutura principal do pandas. Pense numa tabela do Excel com linhas e colunas, mas que vive no código e pode ser manipulada com funções.

**EN:** The core pandas structure. Think of it as an Excel spreadsheet that lives in code and can be manipulated with functions.

---

### `f-string`
```python
print(f"Total de leads: {len(df)}")
```
**PT:** Forma moderna de inserir variáveis dentro de texto. O `f` antes das aspas ativa o modo, e `{}` é substituído pelo valor da variável.

**EN:** Modern way to embed variables in strings. The `f` prefix activates it, and `{}` is replaced by the variable's value.

---

## 📊 3. Pandas Functions | Funções do Pandas

### `pd.read_csv(path)`
```python
df = pd.read_csv('../data/crm_leads.csv')
```
**PT:** Lê um arquivo `.csv` e transforma em DataFrame. O `../` significa "voltar uma pasta" na estrutura de diretórios.

**EN:** Reads a `.csv` file and converts it into a DataFrame. `../` means "go up one folder" in the directory structure.

---

### `df.shape`
```python
print(df.shape)  # Ex: (500, 12)
```
**PT:** Retorna uma tupla `(número de linhas, número de colunas)`. Confirma se o dataset carregou corretamente.

**EN:** Returns a tuple `(rows, columns)`. Confirms if the dataset loaded correctly.

---

### `df.head(n)` / `df.tail(n)`
```python
df.head()   # Mostra as 5 primeiras linhas (padrão)
df.head(10) # Mostra as 10 primeiras linhas
df.tail()   # Mostra as 5 últimas linhas
```
**PT:** Primeira coisa a fazer ao carregar dados. Permite "ver" como o dataset está estruturado.

**EN:** First step after loading data. Lets you "see" the dataset structure.

---

### `df.info()`
```python
df.info()
```
**PT:** Mostra o tipo de dado de cada coluna (`int64`, `float64`, `object`) e se há valores nulos. Essencial para auditoria inicial dos dados.

**EN:** Shows the data type of each column and whether there are null values. Essential for initial data audit.

---

### `df.describe()`
```python
df.describe()
```
**PT:** Gera estatísticas descritivas das colunas numéricas: contagem, média, desvio padrão, mínimo, quartis e máximo.

**EN:** Generates descriptive statistics for numeric columns: count, mean, std deviation, min, quartiles, max.

---

### `df['coluna']`
```python
df['stage']          # Seleciona a coluna 'stage'
df['is_qualified']   # Seleciona a coluna 'is_qualified'
```
**PT:** Seleciona uma única coluna do DataFrame. Retorna uma `Series` (lista de valores com índice).

**EN:** Selects a single column from the DataFrame. Returns a `Series` (list of values with an index).

---

### `df[condição]` — Filtro Booleano
```python
lost_df = df[df['stage'] == 'Lost']
```
**PT:** Filtra linhas com base em uma condição. Funciona como o filtro do Excel. O pandas avalia cada linha: se a condição for `True`, a linha é mantida; se for `False`, descartada.

**EN:** Filters rows based on a condition. Like Excel's filter. Pandas evaluates each row: `True` = keep, `False` = discard.

---

### `.value_counts()`
```python
df['stage'].value_counts()
df['channel'].value_counts()
```
**PT:** Conta quantas vezes cada valor único aparece em uma coluna. Retorna ordenado do mais frequente para o menos frequente.

**EN:** Counts how many times each unique value appears in a column. Returns sorted by most frequent.

---

### `.reindex(lista)`
```python
stage_counts = df['stage'].value_counts().reindex(stage_order)
```
**PT:** Reordena os resultados de acordo com uma lista definida manualmente. Usado para garantir que as etapas do funil aparecem na ordem lógica (topo para fundo), e não por frequência.

**EN:** Reorders results according to a manually defined list. Used to ensure funnel stages appear in logical order (top to bottom), not by frequency.

---

### `.groupby('coluna')`
```python
df.groupby('channel')['is_qualified'].agg(['sum', 'count'])
```
**PT:** Agrupa os dados por uma coluna — equivalente ao `GROUP BY` do SQL. Permite calcular métricas separadas para cada grupo (canal, segmento, etc.).

**EN:** Groups data by a column — equivalent to SQL's `GROUP BY`. Enables calculating separate metrics for each group.

---

### `.agg(['função1', 'função2'])`
```python
.agg(['sum', 'count'])
```
**PT:** Aplica múltiplas funções de agregação ao mesmo tempo. `sum` soma os valores, `count` conta as ocorrências. Muito mais eficiente do que calcular um por um.

**EN:** Applies multiple aggregation functions at once. `sum` adds values, `count` counts occurrences. Much more efficient than calculating one by one.

**Funções de agregação mais usadas:**
| Função | O que faz |
|---|---|
| `sum` | Soma todos os valores |
| `count` | Conta todas as ocorrências (incluindo zeros) |
| `mean` | Calcula a média |
| `min` / `max` | Menor / Maior valor |
| `nunique` | Conta valores únicos |

---

### `.sort_values('coluna', ascending=False)`
```python
segment_conv.sort_values('Conversion Rate', ascending=False)
```
**PT:** Ordena o DataFrame por uma coluna. `ascending=False` = ordem decrescente (maior para menor). `ascending=True` = crescente (padrão).

**EN:** Sorts the DataFrame by a column. `ascending=False` = descending order (highest to lowest).

---

### `df.to_csv(path, index=False)`
```python
df.to_csv('data/crm_leads.csv', index=False)
```
**PT:** Salva o DataFrame como arquivo CSV. `index=False` evita que o pandas adicione uma coluna extra de números (0, 1, 2...) no arquivo.

**EN:** Saves the DataFrame as a CSV file. `index=False` prevents pandas from adding an extra number column (0, 1, 2...) to the file.

---

## 📈 4. Matplotlib / Seaborn Functions | Funções de Gráficos

### `plt.subplots(figsize=(w, h))`
```python
fig, ax = plt.subplots(figsize=(10, 5))
```
**PT:** Cria a "tela" onde o gráfico vai ser desenhado. `fig` é a figura inteira, `ax` é o eixo (onde os dados são plotados). `figsize` define largura x altura em polegadas.

**EN:** Creates the "canvas" for the chart. `fig` is the whole figure, `ax` is the axes (where data is plotted). `figsize` sets width x height in inches.

---

### `ax.bar(x, y)` · `ax.barh(x, y)`
```python
ax.bar(stage_counts.index, stage_counts.values)   # Barras verticais
ax.barh(segment_conv.index, segment_conv['Conversion Rate'])  # Barras horizontais
```
**PT:** Desenha gráficos de barras. `bar` = vertical (bom para poucos itens e sequências). `barh` = horizontal (melhor para muitos itens ou nomes longos).

**EN:** Draws bar charts. `bar` = vertical. `barh` = horizontal (better for many items or long labels).

---

### `ax.set_title()` · `ax.set_xlabel()` · `ax.set_ylabel()`
```python
ax.set_title('Título do Gráfico', fontsize=14, fontweight='bold')
ax.set_xlabel('Etapa')
ax.set_ylabel('Quantidade')
```
**PT:** Define o título e os rótulos dos eixos X e Y. Sempre obrigatório em gráficos profissionais.

**EN:** Sets the chart title and axis labels. Always required in professional charts.

---

### `ax.text(x, y, texto)`
```python
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 1,
            str(int(bar.get_height())),
            ha='center')
```
**PT:** Escreve texto em uma posição específica do gráfico. Usado para colocar o valor numérico em cima de cada barra. O loop `for bar in bars` passa por cada barra e calcula a posição automaticamente.

**EN:** Writes text at a specific position in the chart. Used to show numeric labels on top of each bar.

---

### `mtick.PercentFormatter(1.0)`
```python
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
```
**PT:** Formata o eixo Y para exibir percentuais. O `1.0` indica que os valores estão em formato decimal (0.08 = 8%). Se os valores já fossem 0–100, usaria `PercentFormatter(100)`.

**EN:** Formats the Y axis to display percentages. `1.0` means values are in decimal format (0.08 = 8%).

---

### `sns.color_palette('nome', n)`
```python
sns.color_palette('viridis', 6)
sns.color_palette('rocket', 3)
```
**PT:** Gera uma lista de cores a partir de uma paleta pré-definida. `n` é quantas cores você quer. Paletas mais usadas: `viridis`, `rocket`, `mako`, `coolwarm`.

**EN:** Generates a list of colors from a pre-defined palette. `n` = number of colors needed.

---

### `plt.tight_layout()` · `plt.show()`
```python
plt.tight_layout()
plt.show()
```
**PT:** `tight_layout()` ajusta margens automaticamente para nada ficar cortado. `show()` renderiza e exibe o gráfico. Sempre chamados no final de cada bloco de gráfico.

**EN:** `tight_layout()` auto-adjusts margins so nothing is cut off. `show()` renders and displays the chart.

---

## 🧠 5. Interview Phrases | Frases para Entrevista

> Use essas frases para explicar seu trabalho com confiança:

**Sobre dados sintéticos:**
> *"Como os dados reais são confidenciais por contrato, desenvolvi um gerador de dados sintéticos que replica a estrutura e os padrões comportamentais reais do CRM, com distribuições de conversão baseadas em benchmarks de mercado B2B."*

**Sobre groupby:**
> *"Usei `groupby` com `agg` para calcular a taxa de conversão por canal — é equivalente a um GROUP BY do SQL, mas direto no Python."*

**Sobre filtro booleano:**
> *"Para analisar os motivos de perda, filtrei apenas os leads com status 'Lost' usando filtragem booleana do pandas — a mesma lógica de um WHERE do SQL."*

**Sobre seed:**
> *"Fixei a seed para garantir reprodutibilidade — qualquer pessoa que clone o repositório e rode o gerador vai obter exatamente o mesmo dataset."*

---

*Gustavo Marques · [@GhMarques-analytics](https://github.com/GhMarques-analytics)*
