# Miami Housing — Análise de dados

Este repositório organiza um fluxo incremental para análise do conjunto **Miami Housing (2016)**, cobrindo inspeção, limpeza, EDA com gramática de gráficos e preparação para modelagem.

## Estrutura sugerida
```
.
├── project.ipynb               # notebook principal (relato + códigos)
├── data/
│   ├── miami-housing.csv       # dados originais (nome pode variar)
└── requirements.txt
```

## Ambiente e execução
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python -m notebook
```

Abra `project.ipynb` e execute as células na ordem. O notebook localizará automaticamente um `.csv` dentro de `data/` (ou subpastas).

## Organização dos dados
- O arquivo `.csv` do Miami Housing deve estar em `data/`.
- Artefatos tratados serão salvos em `data/` (ex.: `miami_clean.csv`).

## Fluxo analítico (alto nível)
1. **Descoberta**: leitura do CSV, *quick dict* de colunas (tipos, nulos, distintos).
2. **Tidy**: padronização de nomes, remoção de duplicados por id, criação de variáveis derivadas (ex.: `log_price`, `price_per_sqft`).
3. **EDA**: visualizações com `plotnine` (distribuições e relações chave) acompanhadas de interpretações.
4. **Preparação para modelagem**: exporta `data/miami_clean.csv` para uso em modelos.
