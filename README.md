# GlobalStock AI V7
### Historical Financial Market Machine Learning Research

GlobalStock AI V7 is an independent educational machine-learning research project investigating whether traditional classification models can identify historical stock-market price direction across multiple financial assets and prediction horizons.

The project emphasizes systematic experimentation, time-aware validation, statistical evaluation, reproducibility and transparent reporting of limitations.

**Research outcome:** The tested machine-learning models did not outperform the majority-class baseline on average. This negative result is documented as part of the research rather than presented as a successful predictive advantage.

---

## Research Report

**[Read the GlobalStock AI V7 Research Report (PDF)](reports/final_report/GlobalStock_AI_V7_Research_Report.pdf)**

The report documents the experimental design, validation methodology, model comparisons, statistical analysis, probability calibration, visualizations, limitations and future research directions.

---

## Research Scope

| Component | Description |
|---|---|
| Financial assets | 34 |
| Data frequency | Daily historical market data |
| Prediction horizons | 1-day and 5-day |
| Classification models | Logistic Regression and Random Forest |
| Primary baseline | Training-majority classifier |
| Validation | Five-fold expanding-window walk-forward validation |
| Statistical evaluation | Paired tests, bootstrap analysis and Holm correction |
| Additional analysis | Model stability, baseline robustness and probability calibration |

---

## Key Research Findings

The average walk-forward accuracy results were:

| Horizon | Model | Accuracy |
|---|---|---:|
| 1-day | Logistic Regression | 50.75% |
| 1-day | Random Forest | 49.89% |
| 1-day | Majority baseline | 52.10% |
| 5-day | Logistic Regression | 49.02% |
| 5-day | Random Forest | 48.56% |
| 5-day | Majority baseline | 52.39% |

### Interpretation

- Neither tested machine-learning model outperformed the majority baseline on average.
- Logistic Regression performed closer to the baseline than Random Forest in both horizons.
- All four model-versus-baseline accuracy differences were negative and statistically significant after Holm correction.
- Statistical significance does not imply predictive usefulness.
- The experiments do not establish a reliable predictive advantage or demonstrate future market performance.

These findings highlight the importance of baseline comparisons and rigorous validation in financial machine-learning research.

---

## Methodology

The V7 research workflow includes:

1. Historical dataset preparation and integrity checks.
2. Data cleaning and feature engineering.
3. Construction of 1-day and 5-day prediction targets.
4. Logistic Regression and Random Forest experiments.
5. Expanding-window walk-forward validation.
6. Comparison against simple historical baselines.
7. Per-asset performance evaluation.
8. Statistical significance testing with multiple-comparison correction.
9. Model stability and baseline robustness analysis.
10. Probability calibration diagnostics.
11. Research reporting and reproducibility checks.

The validation design uses five expanding-window folds, a 50% initial training proportion and a five-observation purge gap.

---

## Project Structure

```text
GlobalStock_AI_V7/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── globalstock_ai_v7.py
│   ├── features/
│   ├── models/
│   └── validation/
│
├── notebooks/
│   └── GlobalStock_AI_V7.ipynb
│
├── docs/
│   └── SOURCE_CODE_STRUCTURE.md
│
└── reports/
    ├── final_report/
    │   └── GlobalStock_AI_V7_Research_Report.pdf
    │
    ├── visualizations/
    ├── V7_research_findings_and_limitations.md
    ├── V7_final_research_scorecard.xlsx
    ├── V7_walk_forward_summary.csv
    ├── V7_statistical_significance_report.csv
    ├── V7_model_stability_summary.csv
    └── ...
```

The repository contains the research code, notebook, documentation and selected research outputs. Large datasets and intermediate files are maintained separately.

---

## Research Visualizations

The project includes visualizations covering:

- Model accuracy versus baseline performance.
- Model comparisons.
- Asset-level performance heatmaps.
- Assets outperforming the baseline.
- Average baseline differences.
- 1-day probability calibration.
- 5-day probability calibration.

See the [`reports/visualizations/`](reports/visualizations/) directory.

---

## Installation and Reproducibility

### Requirements

Python 3 and the dependencies listed in `requirements.txt`.

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the research

The original Jupyter notebook is the primary record of the research workflow.

Open `notebooks/GlobalStock_AI_V7.ipynb` in Google Colab or a compatible Jupyter environment.

Configure the project paths and provide the required historical datasets before executing the workflow.

The exported Python file is a consolidated reference export and is not presented as a fully modularized production application.

For exact experimental outputs and methodology, consult the research report and original notebook.

---

## Limitations

This project has important limitations:

- Historical performance does not guarantee future results.
- Financial markets are noisy and non-stationary.
- Financial assets may have correlated movements.
- Findings depend on the selected historical period, features and methodology.
- Transaction costs and slippage are not fully represented in the reported classification results.
- The tested models have not demonstrated a reliable predictive edge.
- Further independent out-of-sample evaluation is necessary.

---

## Future Research

Potential extensions include:

- Testing on an untouched future time period.
- Investigating changing market regimes.
- Studying feature importance and feature stability.
- Improving probability calibration.
- Expanding experiment tracking and reproducibility.
- Evaluating additional models against carefully selected baselines.

---

## Disclaimer

GlobalStock AI V7 is an educational and experimental research project.

It is not financial advice, an investment recommendation, a trading service or a guarantee of future market performance. The research does not establish a reliable predictive advantage. No real-money trading use is intended or supported.

---

## Author

**GlobalStock AI V7 — Independent Educational Research Project**

The project demonstrates an end-to-end research process involving financial data preparation, machine learning, validation, statistical analysis, documentation and transparent reporting.