<div align="center">

# 📈 Sales Funnel Analyzer

### Outbound Sales Funnel Analysis | Análise de Funil de Vendas Outbound

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)

</div>

---

## 🇺🇸 Overview | 🇧🇷 Visão Geral

**EN** — End-to-end analysis of an Outbound B2B sales funnel. This project simulates a real CRM dataset and answers key business questions: where leads drop off, which channels convert best, and how to optimize the pipeline for more qualified meetings.

**PT** — Análise completa de um funil de vendas Outbound B2B. O projeto simula um dataset real de CRM e responde perguntas-chave de negócio: onde os leads morrem, quais canais convertem melhor e como otimizar o pipeline para gerar mais reuniões qualificadas.

---

## 🎯 Business Questions | Perguntas de Negócio

| # | EN | PT |
|---|---|---|
| 1 | How many leads enter vs. become qualified meetings? | Quantos leads entram vs. viram reuniões qualificadas? |
| 2 | Which channel converts more: cold email, LinkedIn or calls? | Qual canal converte mais: cold email, LinkedIn ou ligações? |
| 3 | At which funnel stage do most leads drop off? | Em qual etapa do funil os leads mais morrem? |
| 4 | What is the average time per stage (funnel velocity)? | Qual o tempo médio por etapa (velocidade do funil)? |
| 5 | Which company segments show the highest conversion rate? | Quais segmentos de empresa têm maior taxa de conversão? |

---

## 🗂️ Project Structure | Estrutura do Projeto

```
sales-funnel-analyzer/
│
├── data/
│   └── crm_leads.csv           ← Synthetic CRM dataset | Dataset sintético de CRM
│
├── notebooks/
│   └── funnel_analysis.ipynb   ← Main analysis | Análise principal
│
├── src/
│   └── generate_data.py        ← Synthetic data generator | Gerador de dados
│
├── dashboard/
│   └── sales_funnel.pbix       ← Power BI dashboard (coming soon)
│
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack | Tecnologias

| Tool | Purpose | Uso |
|---|---|---|
| Python + pandas | Data manipulation | Manipulação de dados |
| matplotlib + seaborn | Visualizations | Visualizações |
| SQL (SQLite) | Pipeline queries | Queries de pipeline |
| Power BI | Executive dashboard | Dashboard executivo |

---

## 📊 Key Metrics | Métricas Analisadas

- **Conversion Rate by Stage** | Taxa de Conversão por Etapa
- **Channel Performance** | Performance por Canal (email / LinkedIn / calls)
- **Funnel Velocity** | Velocidade do Funil (dias médios por etapa)
- **ICP Segment Analysis** | Análise por Segmento do ICP
- **Lost Opportunity Reasons** | Motivos de Perda de Oportunidades

---

## 🚀 Status

- [x] Repository structure created | Estrutura do repositório criada
- [ ] Synthetic data generator (`generate_data.py`)
- [ ] Exploratory analysis notebook (`funnel_analysis.ipynb`)
- [ ] Power BI dashboard
- [ ] Final documentation | Documentação final

---

## 📝 Author | Autor

**Gustavo Marques** — [@GhMarques-analytics](https://github.com/GhMarques-analytics)

> *"Turning pipeline data into decisions · Transformando dados de pipeline em decisões"*
