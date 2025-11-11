# 🏠 Miami Housing — Análise e Modelagem de Dados Imobiliários

Este repositório apresenta uma análise completa do conjunto de dados **Miami Housing (2016)**, com foco em compreender os **fatores estruturais, contextuais e sazonais** que influenciam o preço de venda de imóveis (`SALE_PRC`).

O projeto foi desenvolvido em etapas incrementais, incluindo exploração, preparação e modelagem de dados, aplicando princípios de **Data Science**, **estatística aplicada** e **aprendizado de máquina supervisionado**.

---

## 📂 Estrutura do Repositório

```
.
├── project.ipynb               # Notebook principal com a análise e narrativa completa
├── modeling.ipynb              # Notebook dedicado à modelagem e avaliação preditiva
├── feature_engenieering.py     # Função de pré-processamento e criação de variáveis
├── data/
│   └── miami-housing.csv       # Dados originais (input principal)
└── requirements.txt            # Dependências do projeto
```

---

## ⚙️ Instalação e Execução

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente

- **Windows (PowerShell)**
  ```bash
  .venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o notebook

```bash
python -m notebook
```

Abra o arquivo `project.ipynb` e execute as células na ordem sugerida.

---

## 🧭 Estrutura Analítica

O fluxo analítico do projeto segue o ciclo clássico de ciência de dados:

1. **Entendimento do Negócio**  
   - Contextualiza o mercado imobiliário de Miami e define as perguntas de análise.  
   - Identifica as variáveis-alvo (`SALE_PRC`) e as variáveis explicativas em três grupos:
     - **Estruturais:** área construída, área do terreno, qualidade da estrutura, idade do imóvel.  
     - **Contextuais:** distâncias a pontos de interesse, exposição a ruído, localização relativa.  
     - **Sazonais:** mês da venda e variáveis temporais.

2. **Entendimento dos Dados**  
   - Inspeção das colunas, tipos, valores ausentes e estatísticas descritivas.  
   - Análise de coerência e padronização dos nomes das variáveis.

3. **Análise Global e Preliminar das Features**  
   - Exploração estatística inicial das variáveis numéricas.  
   - Cálculo de coeficientes de variação e análise de dispersão.  
   - Identificação de variáveis com alto potencial explicativo para o preço.

4. **Aspectos Contextuais e Sazonais**  
   - Estudo dos efeitos de `month_sold`, `SPEC_FEAT_VAL` e `avno60plus` sobre o preço.  
   - Visualizações com `plotnine` e interpretação dos padrões sazonais.  
   - Cálculo e plotagem do **índice sazonal** de preço por mês da venda.

5. **Feature Engineering**  
   Implementada na função `feature_engineering(df)`:

   - **Filtragem e limpeza:** remoção de outliers de qualidade estrutural (`structure_quality == 3`).  
   - **Transformações logarítmicas:** `log_sale_prc`, `log_tot_lvg_area`, `log_lnd_sqfoot`, `log_spec_feat_val`.  
   - **Codificação categórica:**  
     - `OCEAN_DIST` → bins e *dummies* (`ocean_rank_2`, `ocean_rank_3`)  
     - `structure_quality` → *dummies* (`quality_4`, `quality_5`)  
   - **Variável sazonal binária:** `critical_month` (meses 5, 6 e 11).  
   - **Output:** DataFrame processado e padronizado, pronto para modelagem.

6. **Modelagem Preditiva (em construção)**  
   - Avaliação inicial com regressão linear múltipla e regularização (Ridge/Lasso).  
   - Comparação de desempenho e análise de importância das variáveis.

---

## 🧩 Principais Tecnologias

| Categoria | Biblioteca |
|------------|-------------|
| Notebook e ambiente | `notebook`, `ipykernel` |
| Manipulação e cálculo | `pandas`, `numpy`, `scipy` |
| Visualização | `plotnine`, `matplotlib` |
| Modelagem estatística | `scikit-learn`, `statsmodels`, `patsy` |
| I/O e exportação | `openpyxl`, `pyarrow` |
| Formatação tabular | `tabulate` |

---

## 📊 Resultados Esperados

- **Compreensão** dos fatores que mais influenciam o preço de venda dos imóveis em Miami.  
- **Identificação** de sazonalidades e efeitos contextuais significativos.  
- **Criação** de um conjunto de features limpo e robusto para modelagem preditiva.  
- **Base** para futuras etapas de *machine learning supervisionado*.