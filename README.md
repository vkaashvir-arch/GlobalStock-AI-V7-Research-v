# GlobalStock AI V7
## Historical Stock-Market Machine Learning Research

GlobalStock AI V7 is an educational machine-learning research
project evaluating whether basic classification models can
outperform simple historical baselines across multiple assets
and prediction horizons.

### Research scope

- 34 financial assets
- Daily historical market data
- 1-day and 5-day prediction horizons
- Logistic Regression and Random Forest
- Five-fold expanding-window walk-forward validation
- Statistical significance testing
- Model stability analysis
- Baseline robustness evaluation
- Probability calibration diagnostics
- Per-asset performance analysis

### Key findings

The research did not demonstrate a reliable predictive advantage.

Average walk-forward accuracy:

| Horizon | Model | Accuracy |
|---|---|---:|
| 1D | Logistic Regression | 50.75% |
| 1D | Random Forest | 49.89% |
| 1D | Majority Baseline | 52.10% |
| 5D | Logistic Regression | 49.02% |
| 5D | Random Forest | 48.56% |
| 5D | Majority Baseline | 52.39% |

All four model-versus-majority-baseline accuracy comparisons
were statistically worse after Holm correction.

### Project structure

- `src/` — Exported Python research code
- `notebooks/` — Original research notebook
- `docs/` — Project documentation
- `reports/` — Research reports, summaries and visualisations
- `requirements.txt` — Captured Python dependencies

### Reproducibility

The original notebook is the primary record of the research
workflow. The exported Python file is a consolidated reference
export, not a fully modularised application.

Install dependencies with:

    pip install -r requirements.txt

Run the notebook in Google Colab after configuring the project
paths and obtaining the required historical data.

### Limitations

- Historical results do not establish future performance.
- Financial markets are noisy and non-stationary.
- The assets may be correlated.
- Results depend on the selected period, features and methodology.
- The project has not demonstrated a reliable predictive edge.
- This is an educational research prototype, not a financial
  product or investment recommendation.

No real-money trading use is intended or supported.

### Author

GlobalStock AI V7 — Independent educational research project.
