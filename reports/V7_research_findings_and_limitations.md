# GLOBALSTOCK AI V7
## Research Findings and Limitations Report

Report date: 2026-11-25

---

## 1. Executive Summary

GlobalStock AI V7 is an experimental machine-learning research project investigating historical price-direction classification across 34 financial assets.
The experiments compare Logistic Regression and Random Forest against a training-majority baseline across 1-day and 5-day prediction horizons.
The overall results do not demonstrate that either machine-learning model consistently improves on the baseline.

## 2. Experimental Scope

- Assets analysed: 34
- Prediction horizons: 1-day and 5-day
- Models: Logistic Regression and Random Forest
- Validation: 5-fold expanding-window walk-forward validation
- Initial training proportion: 50%
- Purge gap: 5 observations
- Walk-forward experiments: 1,020

## 3. Model Performance

| Horizon | Model | Accuracy | Baseline | Difference |
|---|---|---:|---:|---:|
| 1D | LogisticRegression | 50.75% | 52.10% | -1.35 pp |
| 1D | RandomForest | 49.89% | 52.10% | -2.21 pp |
| 5D | LogisticRegression | 49.02% | 52.39% | -3.36 pp |
| 5D | RandomForest | 48.56% | 52.39% | -3.83 pp |

## 4. Statistical Significance

Paired asset-level statistical tests compared average model accuracy with the majority baseline. Holm correction was applied to account for multiple comparisons.
- 1D LogisticRegression: mean difference -1.35 percentage points; Holm-adjusted p-value 0.00918.
- 1D RandomForest: mean difference -2.21 percentage points; Holm-adjusted p-value 0.00039.
- 5D LogisticRegression: mean difference -3.36 percentage points; Holm-adjusted p-value 0.00918.
- 5D RandomForest: mean difference -3.83 percentage points; Holm-adjusted p-value 0.00094.

## 5. Probability Calibration

Brier Score and Log Loss were used to examine the quality of predicted probabilities. Lower values indicate better probabilistic performance.
- 1D LogisticRegression: Brier Score 0.2609; Log Loss 0.7203.
- 1D RandomForest: Brier Score 0.2628; Log Loss 0.7210.
- 5D LogisticRegression: Brier Score 0.2812; Log Loss 0.7832.
- 5D RandomForest: Brier Score 0.2898; Log Loss 0.7924.

## 6. Per-Asset Analysis

Per-asset comparisons identified variation across assets. Some individual experiments exceeded the baseline, while many performed below it. These isolated results are exploratory and do not establish future predictive ability.

## 7. Important Limitations

- Historical results do not guarantee future performance.
- Accuracy is close to chance-level in many experiments.
- Asset returns may be correlated.
- Market regimes can change over time.
- Transaction costs and slippage were not modelled.
- Probability calibration requires further validation.
- The project has not established a reliable predictive edge.
- The results are not suitable for real-money trading decisions.

## 8. Future Research

- Test on a completely untouched future time period.
- Investigate changing market regimes.
- Study feature importance and feature stability.
- Evaluate probability calibration on independent data.
- Improve reproducibility and experiment tracking.
- Document computational and methodological limitations.

## 9. Conclusion

GlobalStock AI V7 demonstrates a structured research workflow covering data preparation, feature engineering, walk-forward validation, statistical testing, stability analysis, baseline robustness, calibration and visualisation.
The current evidence does not support a claim that the tested machine-learning models outperform simple baselines. This negative result is an important part of the project's research contribution.