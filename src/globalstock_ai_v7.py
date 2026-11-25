#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ============================================
# GLOBALSTOCK AI V7
# STEP 2 — ENVIRONMENT SETUP
# ============================================

import sys
import subprocess
import importlib

packages = [
    "yfinance",
    "scikit-learn",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "joblib",
    "scipy"
]

print("=" * 55)
print("GLOBALSTOCK AI V7 — DEPENDENCY INSTALLATION")
print("=" * 55)

subprocess.check_call([
    sys.executable, "-m", "pip", "install", "-q", *packages
])

print("\nINSTALLATION COMPLETE\n")

modules = {
    "pandas": "pandas",
    "numpy": "numpy",
    "scikit-learn": "sklearn",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "yfinance": "yfinance",
    "joblib": "joblib",
    "scipy": "scipy"
}

print("LIBRARY VERIFICATION")
print("-" * 55)

for package, module in modules.items():
    imported = importlib.import_module(module)
    version = getattr(imported, "__version__", "Version unavailable")
    print(f"✓ {package}: {version}")

print("\nV7 STEP 2 COMPLETE")


# In[ ]:


import os
from google.colab import drive

print("=" * 55)
print("GLOBALSTOCK AI V7 — V6 FILE DISCOVERY")
print("=" * 55)

drive.mount("/content/drive")

possible_paths = [
    "/content/GlobalStock_AI_V6",
    "/content/drive/MyDrive/GlobalStock_AI_V6"
]

found_paths = []

for path in possible_paths:
    print("\nChecking:", path)

    if os.path.exists(path):
        found_paths.append(path)
        print("✓ FOUND")

        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)

            if level > 2:
                dirs[:] = []
                continue

            print("  " * level + os.path.basename(root) + "/")

            for file in files[:10]:
                print("  " * (level + 1) + file)
    else:
        print("✗ NOT FOUND")

print("\n" + "=" * 55)

if found_paths:
    print("V6 PROJECT LOCATION(S):")
    for path in found_paths:
        print(path)
else:
    print("V6 PROJECT NOT FOUND IN THESE LOCATIONS.")

print("\nV7 STEP 3 DISCOVERY COMPLETE")


# In[ ]:


import os

DRIVE_PATH = "/content/drive/MyDrive"

print("=" * 60)
print("GLOBALSTOCK AI V7 — V6 BACKUP SEARCH")
print("=" * 60)

matches = []

for root, dirs, files in os.walk(DRIVE_PATH):

    # Avoid searching unnecessary hidden/system folders
    dirs[:] = [
        d for d in dirs
        if not d.startswith(".")
    ]

    for file in files:
        name = file.lower()

        if "globalstock_ai_v6" in name or (
            "v6" in name and name.endswith((".zip", ".csv", ".pdf"))
        ):
            path = os.path.join(root, file)
            matches.append(path)

print("\nBACKUP FILES FOUND:")
print("-" * 60)

if matches:
    for path in matches:
        print("✓", path)
else:
    print("No matching V6 backup files found.")

print("\nTOTAL FILES FOUND:", len(matches))
print("\nV7 STEP 4 SEARCH COMPLETE")


# In[ ]:


import os
import json

NOTEBOOKS = [
    "/content/drive/MyDrive/Colab Notebooks/GlobalStock_AI_V6.ipynb",
    "/content/drive/MyDrive/Colab Notebooks/Copy of GlobalStock_AI_V6.ipynb"
]

keywords = [
    "GlobalStock_AI_V6",
    "to_csv",
    "to_pickle",
    "joblib.dump",
    "savefig",
    "drive.mount",
    "cleaned_data",
    "train_test_split",
    "final_report",
    "Portfolio_Package"
]

print("=" * 65)
print("GLOBALSTOCK AI V7 — V6 NOTEBOOK INSPECTION")
print("=" * 65)

for path in NOTEBOOKS:

    print("\nNOTEBOOK:", os.path.basename(path))
    print("-" * 65)

    with open(path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    cells = notebook.get("cells", [])

    print("Total cells:", len(cells))

    matches = 0

    for index, cell in enumerate(cells):

        source = "".join(cell.get("source", []))

        matched = [
            word for word in keywords
            if word.lower() in source.lower()
        ]

        if matched:
            matches += 1

            print(f"\nCell {index}")
            print("Matched:", ", ".join(matched))
            print(source[:900])

    print("\nMatching cells:", matches)

    # Check whether notebook contains saved outputs
    output_count = sum(
        len(cell.get("outputs", []))
        for cell in cells
    )

    print("Cells with outputs:", output_count)

print("\nV6 NOTEBOOK INSPECTION COMPLETE")


# In[ ]:


import json
import os
from html.parser import HTMLParser

NOTEBOOK_PATH = (
    "/content/drive/MyDrive/Colab Notebooks/"
    "GlobalStock_AI_V6.ipynb"
)

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        if data.strip():
            self.text.append(data.strip())

with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    notebook = json.load(f)

print("=" * 65)
print("GLOBALSTOCK AI V7 — V6 SAVED OUTPUT RECOVERY")
print("=" * 65)

for index in range(10, 21):

    cell = notebook["cells"][index]
    outputs = cell.get("outputs", [])

    print(f"\n\nCELL {index}")
    print("-" * 65)

    if not outputs:
        print("No saved output.")
        continue

    for output in outputs:

        if "text" in output:
            content = "".join(output["text"])
            print(content[:3000])

        data = output.get("data", {})

        if "text/plain" in data:
            content = "".join(data["text/plain"])
            print(content[:3000])

        elif "text/html" in data:
            extractor = HTMLTextExtractor()
            extractor.feed("".join(data["text/html"]))
            content = "\n".join(extractor.text)
            print(content[:3000])

print("\n" + "=" * 65)
print("V6 SAVED OUTPUT INSPECTION COMPLETE")


# In[ ]:


from google.colab import drive
import os
import shutil

# 1. Mount Google Drive
drive.mount('/content/drive')

# 2. Define project locations
OLD_DIR = "/content/GlobalStock_AI_V7"
BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

# 3. Copy existing V7 files to Google Drive
if os.path.exists(OLD_DIR):
    shutil.copytree(
        OLD_DIR,
        BASE_DIR,
        dirs_exist_ok=True
    )
    print("Existing V7 files copied to Google Drive.")
else:
    print("No existing runtime folder found. Creating a fresh Drive folder.")

# 4. Create all required project folders
folders = [
    "data",
    "models",
    "results",
    "reports",
    "reports/visualizations",
    "reports/final_report",
    "logs",
    "validation"
]

for folder in folders:
    folder_path = os.path.join(BASE_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)

# 5. Verify storage
print("\n" + "=" * 55)
print("GLOBALSTOCK AI V7 — PERMANENT STORAGE")
print("=" * 55)

print("Project location:", BASE_DIR)
print("Google Drive storage: READY")

for folder in folders:
    print("✓", folder)

print("\nV7 STEP 7 COMPLETE")


# In[ ]:


import os
import time
import pandas as pd
import yfinance as yf

# 1. Permanent project directory
BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# 2. Asset list used in V6
tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA",
    "META", "TSLA", "NFLX", "AMD", "INTC",
    "ORCL", "IBM", "CSCO", "QCOM", "AVGO",
    "JPM", "BAC", "WFC", "GS", "MS",
    "V", "MA", "PYPL", "KO", "PEP",
    "WMT", "COST", "DIS", "NKE", "TCS.NS",
    "INFY.NS", "RELIANCE.NS", "HDFCBANK.NS", "TMCV.NS"
]

# 3. Download approximately five years of daily data
print("=" * 65)
print("GLOBALSTOCK AI V7 — HISTORICAL DATA RECONSTRUCTION")
print("=" * 65)

successful = []
failed = []
summary = []

for ticker in tickers:
    try:
        print(f"\nDownloading: {ticker}")

        df = yf.download(
            ticker,
            period="5y",
            interval="1d",
            auto_adjust=True,
            progress=False,
            threads=False
        )

        if df.empty:
            raise ValueError("No historical data returned")

        # Handle yfinance MultiIndex columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()

        # Save directly to Google Drive
        filename = ticker.replace(".", "_") + ".csv"
        filepath = os.path.join(DATA_DIR, filename)
        df.to_csv(filepath, index=False)

        successful.append(ticker)

        summary.append({
            "Ticker": ticker,
            "Status": "SUCCESS",
            "Rows": len(df),
            "Start_Date": str(df.iloc[0, 0]),
            "End_Date": str(df.iloc[-1, 0]),
            "File": filename
        })

        print(f"SUCCESS — {len(df)} rows saved")

    except Exception as e:
        failed.append(ticker)

        summary.append({
            "Ticker": ticker,
            "Status": "FAILED",
            "Rows": 0,
            "Start_Date": None,
            "End_Date": None,
            "File": str(e)
        })

        print(f"FAILED — {str(e)[:150]}")

    time.sleep(0.5)

# 4. Save reconstruction report
report = pd.DataFrame(summary)

report_path = os.path.join(
    REPORT_DIR,
    "V7_historical_data_reconstruction.csv"
)

report.to_csv(report_path, index=False)

# 5. Final summary
print("\n" + "=" * 65)
print("V7 DATA RECONSTRUCTION SUMMARY")
print("=" * 65)

print("Total assets:", len(tickers))
print("Successfully downloaded:", len(successful))
print("Failed downloads:", len(failed))
print("Total rows:", report["Rows"].sum())

print("\nSuccessful assets:")
print(successful)

print("\nFailed assets:")
print(failed)

print("\nDataset location:", DATA_DIR)
print("Report saved:", report_path)

print("\nV7 STEP 8 COMPLETE")


# In[ ]:


import os
import pandas as pd
import numpy as np

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

audit_results = []

for filename in sorted(os.listdir(DATA_DIR)):

    if not filename.endswith(".csv"):
        continue

    filepath = os.path.join(DATA_DIR, filename)
    ticker = filename.replace(".csv", "").replace("_", ".")

    try:
        df = pd.read_csv(filepath)

        # Identify price columns
        required = ["Open", "High", "Low", "Close", "Volume"]
        missing_columns = [
            col for col in required if col not in df.columns
        ]

        if missing_columns:
            audit_results.append({
                "Ticker": ticker,
                "Rows": len(df),
                "Missing_Values": None,
                "Duplicate_Rows": None,
                "Invalid_Prices": None,
                "Missing_Columns": ", ".join(missing_columns),
                "Status": "REVIEW"
            })
            continue

        # Missing values
        missing_values = int(df.isna().sum().sum())

        # Duplicate rows
        duplicate_rows = int(df.duplicated().sum())

        # Invalid price values
        price_columns = ["Open", "High", "Low", "Close"]

        invalid_prices = int(
            (
                (df[price_columns] <= 0) |
                (~np.isfinite(df[price_columns]))
            ).sum().sum()
        )

        # Invalid OHLC relationships
        invalid_ohlc = int(
            (
                (df["High"] < df["Low"]) |
                (df["High"] < df[["Open", "Close"]].max(axis=1)) |
                (df["Low"] > df[["Open", "Close"]].min(axis=1))
            ).sum()
        )

        # Negative volume
        negative_volume = int((df["Volume"] < 0).sum())

        # Date ordering
        date_column = "Date" if "Date" in df.columns else df.columns[0]
        dates = pd.to_datetime(df[date_column], errors="coerce")
        date_order_ok = bool(dates.is_monotonic_increasing)

        # Overall status
        passed = (
            missing_values == 0
            and duplicate_rows == 0
            and invalid_prices == 0
            and invalid_ohlc == 0
            and negative_volume == 0
            and date_order_ok
        )

        audit_results.append({
            "Ticker": ticker,
            "Rows": len(df),
            "Missing_Values": missing_values,
            "Duplicate_Rows": duplicate_rows,
            "Invalid_Prices": invalid_prices,
            "Invalid_OHLC": invalid_ohlc,
            "Negative_Volume": negative_volume,
            "Date_Order_OK": date_order_ok,
            "Missing_Columns": "",
            "Status": "PASS" if passed else "REVIEW"
        })

    except Exception as e:
        audit_results.append({
            "Ticker": ticker,
            "Rows": None,
            "Missing_Values": None,
            "Duplicate_Rows": None,
            "Invalid_Prices": None,
            "Missing_Columns": str(e),
            "Status": "ERROR"
        })

# Save audit report
audit_df = pd.DataFrame(audit_results)

audit_path = os.path.join(
    REPORT_DIR,
    "V7_dataset_integrity_audit.csv"
)

audit_df.to_csv(audit_path, index=False)

print("=" * 60)
print("GLOBALSTOCK AI V7 — DATASET INTEGRITY AUDIT")
print("=" * 60)

print("Datasets checked:", len(audit_df))
print("PASS:", (audit_df["Status"] == "PASS").sum())
print("REVIEW:", (audit_df["Status"] == "REVIEW").sum())
print("ERROR:", (audit_df["Status"] == "ERROR").sum())

print("\nDetailed results:")
print(audit_df.to_string(index=False))

print("\nAudit report saved:", audit_path)
print("\nV7 STEP 9 COMPLETE")


# In[ ]:


import os
import numpy as np
import pandas as pd

# Project paths
BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"
DATA_DIR = os.path.join(BASE_DIR, "data")
FEATURE_DIR = os.path.join(BASE_DIR, "features")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(FEATURE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(
        alpha=1 / period,
        min_periods=period,
        adjust=False
    ).mean()

    avg_loss = loss.ewm(
        alpha=1 / period,
        min_periods=period,
        adjust=False
    ).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))

    rsi = rsi.mask((avg_loss == 0) & (avg_gain > 0), 100)
    rsi = rsi.mask((avg_loss == 0) & (avg_gain == 0), 50)

    return rsi


summary = []

for filename in sorted(os.listdir(DATA_DIR)):

    if not filename.endswith(".csv"):
        continue

    ticker = filename.replace(".csv", "").replace("_", ".")
    filepath = os.path.join(DATA_DIR, filename)

    try:
        df = pd.read_csv(filepath)

        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date").reset_index(drop=True)

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # Returns
        df["Return_1D"] = close.pct_change(1)
        df["Return_5D"] = close.pct_change(5)
        df["Return_10D"] = close.pct_change(10)

        # Moving averages
        df["SMA_20"] = close.rolling(20).mean()
        df["SMA_50"] = close.rolling(50).mean()

        df["EMA_12"] = close.ewm(
            span=12, adjust=False
        ).mean()

        df["EMA_26"] = close.ewm(
            span=26, adjust=False
        ).mean()

        # Price ratios
        df["Price_SMA20_Ratio"] = close / df["SMA_20"]
        df["Price_SMA50_Ratio"] = close / df["SMA_50"]

        # RSI
        df["RSI_14"] = calculate_rsi(close)

        # MACD
        df["MACD"] = df["EMA_12"] - df["EMA_26"]

        df["MACD_Signal"] = df["MACD"].ewm(
            span=9, adjust=False
        ).mean()

        # Bollinger Bands
        rolling_mean = close.rolling(20).mean()
        rolling_std = close.rolling(20).std()

        df["BB_Upper"] = rolling_mean + 2 * rolling_std
        df["BB_Lower"] = rolling_mean - 2 * rolling_std

        df["BB_Width"] = (
            (df["BB_Upper"] - df["BB_Lower"]) /
            rolling_mean
        )

        # Volatility
        df["Volatility_20D"] = (
            df["Return_1D"].rolling(20).std()
        )

        # Average True Range
        previous_close = close.shift(1)

        true_range = pd.concat([
            high - low,
            (high - previous_close).abs(),
            (low - previous_close).abs()
        ], axis=1).max(axis=1)

        df["ATR_14"] = true_range.rolling(14).mean()

        # Volume ratio
        volume_average = volume.rolling(20).mean()

        df["Volume_Ratio"] = (
            volume / volume_average.replace(0, np.nan)
        )

        # Targets: preserve unavailable future outcomes as NaN
        future_1d = close.shift(-1)
        future_5d = close.shift(-5)

        df["Target_1D"] = np.where(
            future_1d.notna(),
            (future_1d > close).astype(float),
            np.nan
        )

        df["Target_5D"] = np.where(
            future_5d.notna(),
            (future_5d > close).astype(float),
            np.nan
        )

        # Save features
        output_filename = (
            ticker.replace(".", "_") + "_features.csv"
        )

        output_path = os.path.join(
            FEATURE_DIR, output_filename
        )

        df.to_csv(output_path, index=False)

        summary.append({
            "Ticker": ticker,
            "Rows": len(df),
            "Columns": len(df.columns),
            "Target_1D_Missing": int(df["Target_1D"].isna().sum()),
            "Target_5D_Missing": int(df["Target_5D"].isna().sum()),
            "Status": "SUCCESS"
        })

        print(
            f"SUCCESS: {ticker} | "
            f"{len(df)} rows | {len(df.columns)} columns"
        )

    except Exception as e:
        summary.append({
            "Ticker": ticker,
            "Rows": 0,
            "Columns": 0,
            "Target_1D_Missing": None,
            "Target_5D_Missing": None,
            "Status": f"FAILED: {str(e)}"
        })

        print(f"FAILED: {ticker} — {e}")


# Save summary
summary_df = pd.DataFrame(summary)

summary_path = os.path.join(
    REPORT_DIR,
    "V7_feature_engineering_summary.csv"
)

summary_df.to_csv(summary_path, index=False)

# Final report
print("\n" + "=" * 60)
print("GLOBALSTOCK AI V7 — FEATURE ENGINEERING SUMMARY")
print("=" * 60)

print("Total datasets:", len(summary_df))
print("Successful:", (summary_df["Status"] == "SUCCESS").sum())
print("Failed:", (summary_df["Status"] != "SUCCESS").sum())

print("\nTotal rows processed:", summary_df["Rows"].sum())
print("\nTarget missing-value verification:")

print("Target 1D missing values:",
      summary_df["Target_1D_Missing"].sum())

print("Target 5D missing values:",
      summary_df["Target_5D_Missing"].sum())

print("\nFeature directory:", FEATURE_DIR)
print("Summary report:", summary_path)

print("\nV7 STEP 10 COMPLETE")


# In[ ]:


import os
import numpy as np
import pandas as pd

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"
FEATURE_DIR = os.path.join(BASE_DIR, "features")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

audit_results = []

for filename in sorted(os.listdir(FEATURE_DIR)):

    if not filename.endswith(".csv"):
        continue

    ticker = filename.replace("_features.csv", "").replace("_", ".")
    path = os.path.join(FEATURE_DIR, filename)

    df = pd.read_csv(path)

    feature_columns = [
        col for col in df.columns
        if col not in [
            "Date", "Open", "High", "Low",
            "Close", "Volume", "Adj Close",
            "Target_1D", "Target_5D"
        ]
    ]

    features = df[feature_columns]

    missing_features = int(features.isna().sum().sum())

    infinite_values = int(
        np.isinf(features.select_dtypes(include=[np.number])).sum().sum()
    )

    invalid_targets = int(
        (~df["Target_1D"].dropna().isin([0, 1])).sum()
        + (~df["Target_5D"].dropna().isin([0, 1])).sum()
    )

    target_1d_missing = int(df["Target_1D"].isna().sum())
    target_5d_missing = int(df["Target_5D"].isna().sum())

    audit_results.append({
        "Ticker": ticker,
        "Rows": len(df),
        "Feature_Count": len(feature_columns),
        "Missing_Feature_Values": missing_features,
        "Infinite_Values": infinite_values,
        "Target_1D_Missing": target_1d_missing,
        "Target_5D_Missing": target_5d_missing,
        "Invalid_Targets": invalid_targets
    })

audit_df = pd.DataFrame(audit_results)

audit_path = os.path.join(
    REPORT_DIR,
    "V7_feature_quality_audit.csv"
)

audit_df.to_csv(audit_path, index=False)

print("=" * 65)
print("GLOBALSTOCK AI V7 — FEATURE QUALITY AUDIT")
print("=" * 65)

print("Datasets checked:", len(audit_df))
print("Total feature columns:", audit_df["Feature_Count"].sum())
print("Missing feature values:",
      audit_df["Missing_Feature_Values"].sum())
print("Infinite values:", audit_df["Infinite_Values"].sum())
print("Invalid targets:", audit_df["Invalid_Targets"].sum())

print("\nDetailed results:")
print(audit_df.to_string(index=False))

print("\nReport saved:", audit_path)
print("\nV7 STEP 11 COMPLETE")


# In[ ]:


import os
import pandas as pd
import numpy as np

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

FEATURE_DIR = os.path.join(BASE_DIR, "features")
CLEAN_DIR = os.path.join(BASE_DIR, "cleaned_data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(CLEAN_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

summary = []

for filename in sorted(os.listdir(FEATURE_DIR)):

    if not filename.endswith(".csv"):
        continue

    ticker = filename.replace("_features.csv", "").replace("_", ".")

    filepath = os.path.join(FEATURE_DIR, filename)

    df = pd.read_csv(filepath)

    original_rows = len(df)

    # Identify numerical model features
    excluded = [
        "Date", "Open", "High", "Low",
        "Close", "Volume", "Adj Close",
        "Target_1D", "Target_5D"
    ]

    feature_columns = [
        col for col in df.columns
        if col not in excluded
    ]

    # Remove infinite values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Keep rows with complete features and both targets
    required_columns = feature_columns + [
        "Target_1D",
        "Target_5D"
    ]

    df_clean = df.dropna(
        subset=required_columns
    ).copy()

    # Verify binary targets
    df_clean = df_clean[
        df_clean["Target_1D"].isin([0, 1]) &
        df_clean["Target_5D"].isin([0, 1])
    ]

    df_clean = df_clean.sort_values("Date").reset_index(drop=True)

    # Save cleaned dataset
    output_path = os.path.join(
        CLEAN_DIR,
        ticker.replace(".", "_") + "_clean.csv"
    )

    df_clean.to_csv(output_path, index=False)

    summary.append({
        "Ticker": ticker,
        "Original_Rows": original_rows,
        "Cleaned_Rows": len(df_clean),
        "Removed_Rows": original_rows - len(df_clean),
        "Remaining_Missing": int(
            df_clean[required_columns].isna().sum().sum()
        ),
        "Status": "PASS"
    })

    print(
        f"{ticker}: {original_rows} → "
        f"{len(df_clean)} rows"
    )

# Save cleaning report
summary_df = pd.DataFrame(summary)

report_path = os.path.join(
    REPORT_DIR,
    "V7_cleaning_summary.csv"
)

summary_df.to_csv(report_path, index=False)

print("\n" + "=" * 60)
print("GLOBALSTOCK AI V7 — CLEANING SUMMARY")
print("=" * 60)

print("Datasets processed:", len(summary_df))
print("Total original rows:", summary_df["Original_Rows"].sum())
print("Total cleaned rows:", summary_df["Cleaned_Rows"].sum())
print("Total removed rows:", summary_df["Removed_Rows"].sum())
print("Remaining missing values:",
      summary_df["Remaining_Missing"].sum())

print("\nCleaning report:", report_path)
print("Cleaned datasets:", CLEAN_DIR)

print("\nV7 STEP 12 COMPLETE")


# In[ ]:


import os
import warnings
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

warnings.filterwarnings("ignore")

# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

CLEAN_DIR = os.path.join(BASE_DIR, "cleaned_data")
RESULT_DIR = os.path.join(BASE_DIR, "results")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(RESULT_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# =====================================================
# 2. CONFIGURATION
# =====================================================

HORIZONS = {
    "1D": "Target_1D",
    "5D": "Target_5D"
}

FEATURE_EXCLUSIONS = [
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Adj Close",
    "Target_1D",
    "Target_5D"
]

N_SPLITS = 5
INITIAL_TRAIN_RATIO = 0.50
PURGE_GAP = 5

results = []
skipped = []

# =====================================================
# 3. METRIC FUNCTION
# =====================================================

def evaluate_model(y_true, predictions, probabilities=None):

    auc = np.nan

    if probabilities is not None and len(np.unique(y_true)) == 2:
        auc = roc_auc_score(y_true, probabilities)

    return {
        "Accuracy": accuracy_score(y_true, predictions),
        "Balanced_Accuracy": balanced_accuracy_score(
            y_true, predictions
        ),
        "Precision": precision_score(
            y_true, predictions, zero_division=0
        ),
        "Recall": recall_score(
            y_true, predictions, zero_division=0
        ),
        "F1": f1_score(
            y_true, predictions, zero_division=0
        ),
        "ROC_AUC": auc
    }

# =====================================================
# 4. LOAD AND PROCESS DATASETS
# =====================================================

files = sorted([
    f for f in os.listdir(CLEAN_DIR)
    if f.endswith("_clean.csv")
])

print("=" * 70)
print("GLOBALSTOCK AI V7 — WALK-FORWARD VALIDATION")
print("=" * 70)

print("Datasets found:", len(files))

for file_number, filename in enumerate(files, start=1):

    ticker = filename.replace("_clean.csv", "").replace("_", ".")

    filepath = os.path.join(CLEAN_DIR, filename)

    df = pd.read_csv(filepath)

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    feature_columns = [
        col for col in df.columns
        if col not in FEATURE_EXCLUSIONS
    ]

    X = df[feature_columns].apply(
        pd.to_numeric,
        errors="coerce"
    )

    print(
        f"\n[{file_number}/{len(files)}] Processing {ticker}"
    )

    # -------------------------------------------------
    # 5. PROCESS BOTH HORIZONS
    # -------------------------------------------------

    for horizon, target_column in HORIZONS.items():

        y = df[target_column].astype(int)

        n = len(df)

        initial_train_end = int(n * INITIAL_TRAIN_RATIO)

        remaining = n - initial_train_end

        fold_size = remaining // N_SPLITS

        if fold_size < 10:
            skipped.append({
                "Ticker": ticker,
                "Horizon": horizon,
                "Reason": "Validation fold too small"
            })
            continue

        # -------------------------------------------------
        # 6. FIVE EXPANDING VALIDATION FOLDS
        # -------------------------------------------------

        for fold in range(N_SPLITS):

            test_start = initial_train_end + fold * fold_size

            if fold == N_SPLITS - 1:
                test_end = n
            else:
                test_end = test_start + fold_size

            train_end = test_start - PURGE_GAP

            if train_end <= 0:
                continue

            X_train = X.iloc[:train_end]
            y_train = y.iloc[:train_end]

            X_test = X.iloc[test_start:test_end]
            y_test = y.iloc[test_start:test_end]

            # Verify data availability
            if len(X_test) == 0 or len(X_train) < 30:
                continue

            if y_train.nunique() < 2:
                skipped.append({
                    "Ticker": ticker,
                    "Horizon": horizon,
                    "Fold": fold + 1,
                    "Reason": "Training data has only one class"
                })
                continue

            # -------------------------------------------------
            # 7. MAJORITY CLASS BASELINE
            # -------------------------------------------------

            majority_class = int(y_train.mode().iloc[0])

            baseline_predictions = np.full(
                len(y_test),
                majority_class
            )

            baseline_metrics = evaluate_model(
                y_test,
                baseline_predictions
            )

            results.append({
                "Ticker": ticker,
                "Horizon": horizon,
                "Fold": fold + 1,
                "Model": "Majority_Baseline",
                "Train_Rows": len(X_train),
                "Test_Rows": len(X_test),
                **baseline_metrics
            })

            # -------------------------------------------------
            # 8. LOGISTIC REGRESSION
            # -------------------------------------------------

            logistic_model = Pipeline([
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(
                    class_weight="balanced",
                    max_iter=2000,
                    random_state=42
                ))
            ])

            try:
                logistic_model.fit(X_train, y_train)

                predictions = logistic_model.predict(X_test)

                probabilities = logistic_model.predict_proba(
                    X_test
                )[:, 1]

                metrics = evaluate_model(
                    y_test,
                    predictions,
                    probabilities
                )

                results.append({
                    "Ticker": ticker,
                    "Horizon": horizon,
                    "Fold": fold + 1,
                    "Model": "LogisticRegression",
                    "Train_Rows": len(X_train),
                    "Test_Rows": len(X_test),
                    **metrics
                })

            except Exception as e:
                skipped.append({
                    "Ticker": ticker,
                    "Horizon": horizon,
                    "Fold": fold + 1,
                    "Model": "LogisticRegression",
                    "Reason": str(e)
                })

            # -------------------------------------------------
            # 9. RANDOM FOREST
            # -------------------------------------------------

            random_forest = RandomForestClassifier(
                n_estimators=300,
                max_depth=8,
                min_samples_leaf=5,
                max_features="sqrt",
                class_weight="balanced_subsample",
                random_state=42,
                n_jobs=-1
            )

            try:
                random_forest.fit(X_train, y_train)

                predictions = random_forest.predict(X_test)

                probabilities = random_forest.predict_proba(
                    X_test
                )[:, 1]

                metrics = evaluate_model(
                    y_test,
                    predictions,
                    probabilities
                )

                results.append({
                    "Ticker": ticker,
                    "Horizon": horizon,
                    "Fold": fold + 1,
                    "Model": "RandomForest",
                    "Train_Rows": len(X_train),
                    "Test_Rows": len(X_test),
                    **metrics
                })

            except Exception as e:
                skipped.append({
                    "Ticker": ticker,
                    "Horizon": horizon,
                    "Fold": fold + 1,
                    "Model": "RandomForest",
                    "Reason": str(e)
                })

# =====================================================
# 10. SAVE DETAILED RESULTS
# =====================================================

results_df = pd.DataFrame(results)

results_path = os.path.join(
    RESULT_DIR,
    "V7_walk_forward_results.csv"
)

results_df.to_csv(results_path, index=False)

# =====================================================
# 11. CREATE SUMMARY
# =====================================================

summary_df = (
    results_df
    .groupby(["Horizon", "Model"])
    .agg({
        "Accuracy": "mean",
        "Balanced_Accuracy": "mean",
        "Precision": "mean",
        "Recall": "mean",
        "F1": "mean",
        "ROC_AUC": "mean",
        "Fold": "count"
    })
    .reset_index()
)

summary_path = os.path.join(
    REPORT_DIR,
    "V7_walk_forward_summary.csv"
)

summary_df.to_csv(summary_path, index=False)

# =====================================================
# 12. SAVE SKIPPED EXPERIMENTS
# =====================================================

skipped_df = pd.DataFrame(skipped)

skipped_path = os.path.join(
    REPORT_DIR,
    "V7_skipped_experiments.csv"
)

skipped_df.to_csv(skipped_path, index=False)

# =====================================================
# 13. FINAL REPORT
# =====================================================

print("\n" + "=" * 70)
print("V7 WALK-FORWARD VALIDATION COMPLETE")
print("=" * 70)

print("Total experiments:", len(results_df))
print("Skipped experiments:", len(skipped_df))

print("\nMODEL PERFORMANCE SUMMARY")

print(
    summary_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)

print("\nDetailed results:", results_path)
print("Summary report:", summary_path)
print("Skipped report:", skipped_path)

print("\nV7 STEP 13 COMPLETE")


# In[ ]:


import os
import numpy as np
import pandas as pd

from scipy.stats import wilcoxon, ttest_rel

# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

RESULT_DIR = os.path.join(BASE_DIR, "results")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

INPUT_FILE = os.path.join(
    RESULT_DIR,
    "V7_walk_forward_results.csv"
)

os.makedirs(REPORT_DIR, exist_ok=True)

# =====================================================
# 2. LOAD WALK-FORWARD RESULTS
# =====================================================

df = pd.read_csv(INPUT_FILE)

required_models = [
    "Majority_Baseline",
    "LogisticRegression",
    "RandomForest"
]

df = df[df["Model"].isin(required_models)].copy()

# Average the five folds for each asset and model
asset_results = (
    df.groupby(["Ticker", "Horizon", "Model"])["Accuracy"]
    .mean()
    .reset_index()
)

# =====================================================
# 3. PAIRED STATISTICAL TESTING
# =====================================================

statistical_results = []

comparisons = [
    ("1D", "LogisticRegression"),
    ("1D", "RandomForest"),
    ("5D", "LogisticRegression"),
    ("5D", "RandomForest")
]

rng = np.random.default_rng(42)

for horizon, model_name in comparisons:

    subset = asset_results[
        asset_results["Horizon"] == horizon
    ]

    pivot = subset.pivot(
        index="Ticker",
        columns="Model",
        values="Accuracy"
    )

    paired = pivot[
        ["Majority_Baseline", model_name]
    ].dropna()

    baseline = paired["Majority_Baseline"].to_numpy()
    model = paired[model_name].to_numpy()

    differences = model - baseline

    n = len(differences)

    mean_difference = np.mean(differences)
    median_difference = np.median(differences)

    wins = int(np.sum(differences > 0))
    losses = int(np.sum(differences < 0))
    ties = int(np.sum(differences == 0))

    # Wilcoxon signed-rank test
    if np.allclose(differences, 0):
        wilcoxon_stat = 0.0
        wilcoxon_p = 1.0
    else:
        w_result = wilcoxon(
            differences,
            alternative="two-sided",
            method="auto"
        )

        wilcoxon_stat = float(w_result.statistic)
        wilcoxon_p = float(w_result.pvalue)

    # Paired t-test
    t_result = ttest_rel(model, baseline)

    t_stat = float(t_result.statistic)
    t_p = float(t_result.pvalue)

    # Bootstrap confidence interval across assets
    bootstrap_means = []

    for _ in range(10000):

        sample = rng.choice(
            differences,
            size=n,
            replace=True
        )

        bootstrap_means.append(np.mean(sample))

    ci_lower, ci_upper = np.percentile(
        bootstrap_means,
        [2.5, 97.5]
    )

    statistical_results.append({
        "Horizon": horizon,
        "Model": model_name,
        "Assets": n,
        "Mean_Baseline_Accuracy": np.mean(baseline),
        "Mean_Model_Accuracy": np.mean(model),
        "Mean_Accuracy_Difference": mean_difference,
        "Median_Accuracy_Difference": median_difference,
        "Assets_Beat_Baseline": wins,
        "Assets_Lost_To_Baseline": losses,
        "Ties": ties,
        "Wilcoxon_Statistic": wilcoxon_stat,
        "Wilcoxon_P_Value": wilcoxon_p,
        "Paired_T_Statistic": t_stat,
        "Paired_T_P_Value": t_p,
        "Bootstrap_CI_Lower": ci_lower,
        "Bootstrap_CI_Upper": ci_upper
    })

# =====================================================
# 4. HOLM MULTIPLE-TEST CORRECTION
# =====================================================

p_values = np.array([
    row["Wilcoxon_P_Value"]
    for row in statistical_results
])

order = np.argsort(p_values)

adjusted = np.ones(len(p_values))
running_max = 0

for rank, index in enumerate(order):

    adjusted_p = (
        len(p_values) - rank
    ) * p_values[index]

    running_max = max(running_max, adjusted_p)

    adjusted[index] = min(running_max, 1.0)

for i, row in enumerate(statistical_results):

    row["Holm_Adjusted_P_Value"] = adjusted[i]

    row["Significant_After_Holm"] = (
        adjusted[i] < 0.05
    )

# =====================================================
# 5. SAVE RESULTS
# =====================================================

stats_df = pd.DataFrame(statistical_results)

output_file = os.path.join(
    REPORT_DIR,
    "V7_statistical_significance_report.csv"
)

stats_df.to_csv(output_file, index=False)

# =====================================================
# 6. DISPLAY REPORT
# =====================================================

print("=" * 75)
print("GLOBALSTOCK AI V7 — STATISTICAL SIGNIFICANCE REPORT")
print("=" * 75)

print("\nPAIRED MODEL COMPARISONS")

display_columns = [
    "Horizon",
    "Model",
    "Assets",
    "Mean_Model_Accuracy",
    "Mean_Baseline_Accuracy",
    "Mean_Accuracy_Difference",
    "Assets_Beat_Baseline",
    "Wilcoxon_P_Value",
    "Holm_Adjusted_P_Value",
    "Significant_After_Holm"
]

print(
    stats_df[display_columns].to_string(
        index=False,
        float_format=lambda x: f"{x:.5f}"
    )
)

print("\nBOOTSTRAP 95% CONFIDENCE INTERVALS")

for _, row in stats_df.iterrows():

    print(
        f"{row['Horizon']} {row['Model']}: "
        f"[{row['Bootstrap_CI_Lower']:.5f}, "
        f"{row['Bootstrap_CI_Upper']:.5f}]"
    )

print("\nInterpretation threshold: 0.05")
print("Multiple-testing correction: Holm")

print("\nReport saved:", output_file)

print("\nV7 STEP 14 COMPLETE")


# In[ ]:


import os
import numpy as np
import pandas as pd

# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

RESULT_DIR = os.path.join(BASE_DIR, "results")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

INPUT_FILE = os.path.join(
    RESULT_DIR,
    "V7_walk_forward_results.csv"
)

os.makedirs(REPORT_DIR, exist_ok=True)

# =====================================================
# 2. LOAD RESULTS
# =====================================================

df = pd.read_csv(INPUT_FILE)

required_columns = [
    "Ticker",
    "Horizon",
    "Model",
    "Fold",
    "Accuracy",
    "Balanced_Accuracy",
    "ROC_AUC"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

print("=" * 75)
print("GLOBALSTOCK AI V7 — MODEL STABILITY ANALYSIS")
print("=" * 75)

# =====================================================
# 3. PER-ASSET STABILITY
# =====================================================

asset_stability = (
    df.groupby(["Ticker", "Horizon", "Model"])
    .agg(
        Mean_Accuracy=("Accuracy", "mean"),
        Accuracy_Std=("Accuracy", "std"),
        Min_Accuracy=("Accuracy", "min"),
        Max_Accuracy=("Accuracy", "max"),
        Mean_Balanced_Accuracy=("Balanced_Accuracy", "mean"),
        Balanced_Accuracy_Std=("Balanced_Accuracy", "std"),
        Mean_ROC_AUC=("ROC_AUC", "mean"),
        Fold_Count=("Fold", "nunique")
    )
    .reset_index()
)

# =====================================================
# 4. COMPARE EACH MODEL WITH BASELINE
# =====================================================

baseline = asset_stability[
    asset_stability["Model"] == "Majority_Baseline"
][
    ["Ticker", "Horizon", "Mean_Accuracy"]
].rename(
    columns={
        "Mean_Accuracy": "Baseline_Accuracy"
    }
)

asset_stability = asset_stability.merge(
    baseline,
    on=["Ticker", "Horizon"],
    how="left"
)

asset_stability["Accuracy_Difference"] = (
    asset_stability["Mean_Accuracy"]
    - asset_stability["Baseline_Accuracy"]
)

asset_stability["Beat_Baseline"] = (
    asset_stability["Accuracy_Difference"] > 0
)

# =====================================================
# 5. OVERALL MODEL STABILITY SUMMARY
# =====================================================

summary = (
    asset_stability
    .groupby(["Horizon", "Model"])
    .agg(
        Assets=("Ticker", "nunique"),
        Average_Accuracy=("Mean_Accuracy", "mean"),
        Average_Accuracy_Std=("Accuracy_Std", "mean"),
        Average_Balanced_Accuracy=(
            "Mean_Balanced_Accuracy", "mean"
        ),
        Average_ROC_AUC=("Mean_ROC_AUC", "mean"),
        Average_Accuracy_Difference=(
            "Accuracy_Difference", "mean"
        ),
        Assets_Beating_Baseline=("Beat_Baseline", "sum"),
        Average_Min_Accuracy=("Min_Accuracy", "mean"),
        Average_Max_Accuracy=("Max_Accuracy", "mean"),
        Average_Fold_Count=("Fold_Count", "mean")
    )
    .reset_index()
)

summary["Assets_Beating_Baseline_Percent"] = (
    summary["Assets_Beating_Baseline"]
    / summary["Assets"] * 100
)

# =====================================================
# 6. FOLD-LEVEL CONSISTENCY
# =====================================================

fold_pivot = df.pivot_table(
    index=["Ticker", "Horizon", "Fold"],
    columns="Model",
    values="Accuracy"
).reset_index()

fold_comparisons = []

for model_name in [
    "LogisticRegression",
    "RandomForest"
]:

    if model_name not in fold_pivot.columns:
        continue

    comparison = fold_pivot[
        ["Ticker", "Horizon", "Fold",
         "Majority_Baseline", model_name]
    ].dropna().copy()

    comparison["Beat_Baseline"] = (
        comparison[model_name]
        > comparison["Majority_Baseline"]
    )

    comparison["Model"] = model_name

    fold_comparisons.append(comparison)

if fold_comparisons:

    fold_comparisons_df = pd.concat(
        fold_comparisons,
        ignore_index=True
    )

    fold_consistency = (
        fold_comparisons_df
        .groupby(["Horizon", "Model"])
        .agg(
            Total_Comparisons=("Beat_Baseline", "count"),
            Folds_Beating_Baseline=("Beat_Baseline", "sum")
        )
        .reset_index()
    )

    fold_consistency["Percent_Folds_Beating_Baseline"] = (
        fold_consistency["Folds_Beating_Baseline"]
        / fold_consistency["Total_Comparisons"] * 100
    )

else:
    fold_consistency = pd.DataFrame()

# =====================================================
# 7. SAVE REPORTS
# =====================================================

asset_file = os.path.join(
    REPORT_DIR,
    "V7_model_stability_by_asset.csv"
)

summary_file = os.path.join(
    REPORT_DIR,
    "V7_model_stability_summary.csv"
)

fold_file = os.path.join(
    REPORT_DIR,
    "V7_fold_consistency_report.csv"
)

asset_stability.to_csv(asset_file, index=False)
summary.to_csv(summary_file, index=False)
fold_consistency.to_csv(fold_file, index=False)

# =====================================================
# 8. DISPLAY RESULTS
# =====================================================

print("\nOVERALL MODEL STABILITY SUMMARY")

print(
    summary.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)

print("\nFOLD-LEVEL BASELINE COMPARISON")

if not fold_consistency.empty:
    print(
        fold_consistency.to_string(
            index=False,
            float_format=lambda x: f"{x:.2f}"
        )
    )

print("\nREPORTS SAVED:")
print(asset_file)
print(summary_file)
print(fold_file)

print("\nV7 STEP 15 COMPLETE")


# In[ ]:


import os
import numpy as np
import pandas as pd

# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

CLEAN_DIR = os.path.join(BASE_DIR, "cleaned_data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

HORIZONS = ["Target_1D", "Target_5D"]

# =====================================================
# 2. METRIC FUNCTIONS
# =====================================================

def calculate_metrics(y_true, y_pred):

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    accuracy = np.mean(y_true == y_pred)

    recalls = []

    for class_value in [0, 1]:

        mask = y_true == class_value

        if mask.sum() > 0:
            recalls.append(
                np.mean(y_pred[mask] == class_value)
            )

    balanced_accuracy = np.mean(recalls)

    return accuracy, balanced_accuracy


# =====================================================
# 3. LOAD DATASETS
# =====================================================

files = sorted([
    f for f in os.listdir(CLEAN_DIR)
    if f.endswith(".csv")
])

results = []

print("=" * 75)
print("GLOBALSTOCK AI V7 — BASELINE ROBUSTNESS ANALYSIS")
print("=" * 75)

print("Datasets found:", len(files))

# =====================================================
# 4. PROCESS EACH ASSET
# =====================================================

for file_number, filename in enumerate(files, start=1):

    ticker = filename.replace(".csv", "")

    path = os.path.join(CLEAN_DIR, filename)

    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.sort_values("Date").reset_index(drop=True)

    print(f"[{file_number}/{len(files)}] {ticker}")

    for horizon in HORIZONS:

        # Keep rows with valid target and previous-day return
        valid = df.dropna(
            subset=[horizon, "Return_1D"]
        ).reset_index(drop=True)

        n = len(valid)

        initial_train_size = int(n * 0.50)

        remaining = n - initial_train_size

        test_sizes = [
            len(x)
            for x in np.array_split(
                np.arange(remaining), 5
            )
        ]

        test_start = initial_train_size

        for fold_number, test_size in enumerate(
            test_sizes, start=1
        ):

            # Purge 5 observations before test fold
            train_end = test_start - 5

            if train_end <= 0 or test_size == 0:
                test_start += test_size
                continue

            train = valid.iloc[:train_end]

            test = valid.iloc[
                test_start:test_start + test_size
            ]

            y_train = train[horizon].astype(int).to_numpy()
            y_test = test[horizon].astype(int).to_numpy()

            # -------------------------------------------------
            # BASELINE 1: TRAINING MAJORITY
            # -------------------------------------------------

            majority_class = int(
                pd.Series(y_train).mode().iloc[0]
            )

            majority_predictions = np.full(
                len(y_test),
                majority_class
            )

            # -------------------------------------------------
            # BASELINE 2: ALWAYS UP
            # -------------------------------------------------

            always_up = np.ones(len(y_test), dtype=int)

            # -------------------------------------------------
            # BASELINE 3: ALWAYS DOWN
            # -------------------------------------------------

            always_down = np.zeros(len(y_test), dtype=int)

            # -------------------------------------------------
            # BASELINE 4: PREVIOUS-DAY DIRECTION
            # -------------------------------------------------

            previous_direction = (
                test["Return_1D"].to_numpy() > 0
            ).astype(int)

            baselines = {
                "Training_Majority": majority_predictions,
                "Always_Up": always_up,
                "Always_Down": always_down,
                "Previous_Day_Direction": previous_direction
            }

            for baseline_name, predictions in baselines.items():

                accuracy, balanced_accuracy = calculate_metrics(
                    y_test,
                    predictions
                )

                results.append({
                    "Ticker": ticker,
                    "Horizon": horizon.replace("Target_", ""),
                    "Fold": fold_number,
                    "Baseline": baseline_name,
                    "Accuracy": accuracy,
                    "Balanced_Accuracy": balanced_accuracy,
                    "Train_Size": len(train),
                    "Test_Size": len(test)
                })

            test_start += test_size

# =====================================================
# 5. CREATE RESULTS DATAFRAME
# =====================================================

results_df = pd.DataFrame(results)

# =====================================================
# 6. OVERALL BASELINE SUMMARY
# =====================================================

summary = (
    results_df
    .groupby(["Horizon", "Baseline"])
    .agg(
        Experiments=("Accuracy", "count"),
        Average_Accuracy=("Accuracy", "mean"),
        Accuracy_Std=("Accuracy", "std"),
        Average_Balanced_Accuracy=(
            "Balanced_Accuracy", "mean"
        ),
        Balanced_Accuracy_Std=(
            "Balanced_Accuracy", "std"
        )
    )
    .reset_index()
)

# =====================================================
# 7. SAVE REPORTS
# =====================================================

detailed_file = os.path.join(
    REPORT_DIR,
    "V7_baseline_robustness_detailed.csv"
)

summary_file = os.path.join(
    REPORT_DIR,
    "V7_baseline_robustness_summary.csv"
)

results_df.to_csv(detailed_file, index=False)
summary.to_csv(summary_file, index=False)

# =====================================================
# 8. DISPLAY RESULTS
# =====================================================

print("\n" + "=" * 75)
print("BASELINE ROBUSTNESS SUMMARY")
print("=" * 75)

print(
    summary.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)

print("\nTotal baseline experiments:", len(results_df))

print("\nDETAILED REPORT:")
print(detailed_file)

print("\nSUMMARY REPORT:")
print(summary_file)

print("\nV7 STEP 16 COMPLETE")


# In[ ]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import calibration_curve
from sklearn.metrics import brier_score_loss, log_loss

# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

CLEAN_DIR = os.path.join(BASE_DIR, "cleaned_data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
VIS_DIR = os.path.join(REPORT_DIR, "visualizations")

os.makedirs(VIS_DIR, exist_ok=True)

HORIZONS = ["Target_1D", "Target_5D"]

EXCLUDED = [
    "Date", "Open", "High", "Low",
    "Close", "Volume", "Adj Close",
    "Target_1D", "Target_5D"
]

# =====================================================
# 2. MODEL DEFINITIONS
# =====================================================

def create_models():

    return {
        "LogisticRegression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(
                class_weight="balanced",
                max_iter=2000,
                random_state=42
            ))
        ]),

        "RandomForest": RandomForestClassifier(
            n_estimators=300,
            max_depth=8,
            min_samples_leaf=5,
            max_features="sqrt",
            class_weight="balanced_subsample",
            random_state=42,
            n_jobs=-1
        )
    }

# =====================================================
# 3. PROCESS DATASETS
# =====================================================

files = sorted([
    f for f in os.listdir(CLEAN_DIR)
    if f.endswith(".csv")
])

results = []

print("=" * 70)
print("GLOBALSTOCK AI V7 — PROBABILITY CALIBRATION")
print("=" * 70)

for file_number, filename in enumerate(files, start=1):

    ticker = filename.replace("_clean.csv", "")

    path = os.path.join(CLEAN_DIR, filename)

    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    feature_columns = [
        c for c in df.columns
        if c not in EXCLUDED
    ]

    X = df[feature_columns].apply(
        pd.to_numeric,
        errors="coerce"
    )

    print(f"[{file_number}/{len(files)}] {ticker}")

    for horizon in HORIZONS:

        valid = df.dropna(
            subset=[horizon]
        ).reset_index(drop=True)

        X_valid = X.loc[valid.index].reset_index(drop=True)

        y = valid[horizon].astype(int).reset_index(drop=True)

        n = len(valid)

        initial_train_size = int(n * 0.50)
        remaining = n - initial_train_size

        test_sizes = [
            len(x)
            for x in np.array_split(
                np.arange(remaining), 5
            )
        ]

        test_start = initial_train_size

        for fold, test_size in enumerate(test_sizes, start=1):

            train_end = test_start - 5

            if train_end <= 0 or test_size == 0:
                test_start += test_size
                continue

            X_train = X_valid.iloc[:train_end]
            y_train = y.iloc[:train_end]

            X_test = X_valid.iloc[
                test_start:test_start + test_size
            ]

            y_test = y.iloc[
                test_start:test_start + test_size
            ]

            for model_name, model in create_models().items():

                model.fit(X_train, y_train)

                probabilities = model.predict_proba(
                    X_test
                )[:, 1]

                predictions = (
                    probabilities >= 0.5
                ).astype(int)

                results.append({
                    "Ticker": ticker,
                    "Horizon": horizon.replace("Target_", ""),
                    "Fold": fold,
                    "Model": model_name,
                    "Brier_Score": brier_score_loss(
                        y_test, probabilities
                    ),
                    "Log_Loss": log_loss(
                        y_test,
                        probabilities,
                        labels=[0, 1]
                    ),
                    "Mean_Predicted_Probability": np.mean(
                        probabilities
                    ),
                    "Actual_Positive_Frequency": np.mean(
                        y_test
                    ),
                    "Accuracy": np.mean(
                        predictions == y_test
                    )
                })

            test_start += test_size

# =====================================================
# 4. CREATE REPORT
# =====================================================

results_df = pd.DataFrame(results)

summary = (
    results_df
    .groupby(["Horizon", "Model"])
    .agg(
        Experiments=("Brier_Score", "count"),
        Average_Brier_Score=("Brier_Score", "mean"),
        Average_Log_Loss=("Log_Loss", "mean"),
        Mean_Predicted_Probability=(
            "Mean_Predicted_Probability", "mean"
        ),
        Actual_Positive_Frequency=(
            "Actual_Positive_Frequency", "mean"
        ),
        Average_Accuracy=("Accuracy", "mean")
    )
    .reset_index()
)

# =====================================================
# 5. SAVE REPORTS
# =====================================================

results_file = os.path.join(
    REPORT_DIR,
    "V7_probability_calibration_detailed.csv"
)

summary_file = os.path.join(
    REPORT_DIR,
    "V7_probability_calibration_summary.csv"
)

results_df.to_csv(results_file, index=False)
summary.to_csv(summary_file, index=False)

# =====================================================
# 6. CALIBRATION CURVES
# =====================================================

for horizon in ["1D", "5D"]:

    plt.figure(figsize=(8, 6))

    for model_name in [
        "LogisticRegression",
        "RandomForest"
    ]:

        subset = results_df[
            (results_df["Horizon"] == horizon) &
            (results_df["Model"] == model_name)
        ]

        # This summary is descriptive across folds/assets.
        # It is not a pooled independent-observation estimate.
        probability = subset[
            "Mean_Predicted_Probability"
        ].to_numpy()

        actual = subset[
            "Actual_Positive_Frequency"
        ].to_numpy()

        plt.scatter(
            probability,
            actual,
            label=model_name,
            alpha=0.7
        )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        label="Perfect Calibration"
    )

    plt.xlabel("Mean Predicted Probability")
    plt.ylabel("Actual Positive Frequency")
    plt.title(f"V7 {horizon} Probability Calibration")
    plt.legend()
    plt.grid(True)

    plot_file = os.path.join(
        VIS_DIR,
        f"V7_{horizon}_calibration.png"
    )

    plt.savefig(plot_file, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()

# =====================================================
# 7. DISPLAY RESULTS
# =====================================================

print("\nPROBABILITY CALIBRATION SUMMARY")

print(
    summary.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)

print("\nTotal experiments:", len(results_df))

print("\nReports saved:")
print(results_file)
print(summary_file)

print("\nV7 STEP 17 COMPLETE")


# In[ ]:


import os
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

BASE_DIR = "/content/drive/MyDrive/GlobalStock_AI_V7"

print("=" * 65)
print("V7 PROJECT DIRECTORY CHECK")
print("=" * 65)

if os.path.exists(BASE_DIR):

    print("\nV7 project folder FOUND!")

    print("\nFolders and files:")
    for item in sorted(os.listdir(BASE_DIR)):
        path = os.path.join(BASE_DIR, item)

        if os.path.isdir(path):
            print(f"[FOLDER] {item}")

        else:
            print(f"[FILE]   {item}")

    print("\nSearching for cleaned CSV files:")

    for root, dirs, files in os.walk(BASE_DIR):

        csv_files = [
            f for f in files
            if f.endswith(".csv")
        ]

        if csv_files:
            print("\nLocation:", root)
            print("CSV files:", len(csv_files))
            print("Examples:", csv_files[:5])

else:
    print("\nV7 project folder NOT FOUND!")
    print("Check Google Drive mounting and folder location.")


# In[ ]:


import os

print("=" * 60)
print("GOOGLE DRIVE MOUNT CHECK")
print("=" * 60)

if os.path.ismount("/content/drive"):
    print("Google Drive is already mounted.")

else:
    print("Google Drive is not mounted.")

print("\nChecking MyDrive:")

MYDRIVE = "/content/drive/MyDrive"

if os.path.exists(MYDRIVE):

    print("MyDrive found!")

    print("\nAvailable folders:")

    for item in sorted(os.listdir(MYDRIVE)):
        if "GlobalStock" in item:
            print(item)

else:
    print("MyDrive not accessible at this location.")


# In[ ]:


import os
from google.colab import drive

# Mount Drive at an alternative location
drive.mount('/content/gdrive')

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

print("\n" + "=" * 60)
print("GLOBALSTOCK AI V7 — DIRECTORY CHECK")
print("=" * 60)

if os.path.exists(BASE_DIR):

    print("V7 PROJECT FOUND!")

    for item in sorted(os.listdir(BASE_DIR)):
        path = os.path.join(BASE_DIR, item)

        if os.path.isdir(path):
            print("[FOLDER]", item)

    print("\nSearching for cleaned datasets...")

    for root, dirs, files in os.walk(BASE_DIR):

        csv_files = [
            f for f in files
            if f.endswith(".csv")
        ]

        if csv_files:
            print("\nLocation:", root)
            print("CSV count:", len(csv_files))
            print("Examples:", csv_files[:5])

else:
    print("V7 project not found at the new mount location.")


# In[ ]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import brier_score_loss, log_loss

# =====================================================
# 1. PROJECT PATHS
# =====================================================

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

CLEAN_DIR = os.path.join(BASE_DIR, "cleaned_data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
VIS_DIR = os.path.join(REPORT_DIR, "visualizations")

os.makedirs(VIS_DIR, exist_ok=True)

HORIZONS = ["Target_1D", "Target_5D"]

EXCLUDED = [
    "Date", "Open", "High", "Low",
    "Close", "Volume", "Adj Close",
    "Target_1D", "Target_5D"
]

# Verify the directory
if not os.path.isdir(CLEAN_DIR):
    raise FileNotFoundError(
        f"Cleaned data folder not found: {CLEAN_DIR}"
    )

# =====================================================
# 2. MODEL DEFINITIONS
# =====================================================

def create_models():

    return {
        "LogisticRegression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(
                class_weight="balanced",
                max_iter=2000,
                random_state=42
            ))
        ]),

        "RandomForest": RandomForestClassifier(
            n_estimators=300,
            max_depth=8,
            min_samples_leaf=5,
            max_features="sqrt",
            class_weight="balanced_subsample",
            random_state=42,
            n_jobs=-1
        )
    }

# =====================================================
# 3. FIND DATASETS
# =====================================================

files = sorted([
    f for f in os.listdir(CLEAN_DIR)
    if f.endswith(".csv")
])

if len(files) == 0:
    raise ValueError("No cleaned CSV datasets found.")

results = []

print("=" * 70)
print("GLOBALSTOCK AI V7 — PROBABILITY CALIBRATION")
print("=" * 70)

print("Datasets found:", len(files))

# =====================================================
# 4. PROCESS DATASETS
# =====================================================

for file_number, filename in enumerate(files, start=1):

    ticker = filename.replace("_clean.csv", "")

    path = os.path.join(CLEAN_DIR, filename)

    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    feature_columns = [
        c for c in df.columns
        if c not in EXCLUDED
    ]

    X = df[feature_columns].apply(
        pd.to_numeric,
        errors="coerce"
    )

    print(f"[{file_number}/{len(files)}] {ticker}")

    for horizon in HORIZONS:

        # Preserve original row alignment
        valid_mask = df[horizon].notna()

        valid = df.loc[valid_mask].copy().reset_index(drop=True)

        X_valid = X.loc[valid_mask].reset_index(drop=True)

        y = valid[horizon].astype(int).reset_index(drop=True)

        # Check feature quality
        if X_valid.isna().any().any():
            raise ValueError(
                f"Missing feature values in {ticker}, {horizon}"
            )

        if not np.isfinite(X_valid.to_numpy()).all():
            raise ValueError(
                f"Infinite feature values in {ticker}, {horizon}"
            )

        n = len(valid)

        initial_train_size = int(n * 0.50)
        remaining = n - initial_train_size

        test_sizes = [
            len(x)
            for x in np.array_split(
                np.arange(remaining), 5
            )
        ]

        test_start = initial_train_size

        for fold, test_size in enumerate(test_sizes, start=1):

            train_end = test_start - 5

            if train_end <= 0 or test_size == 0:
                test_start += test_size
                continue

            X_train = X_valid.iloc[:train_end]
            y_train = y.iloc[:train_end]

            X_test = X_valid.iloc[
                test_start:test_start + test_size
            ]

            y_test = y.iloc[
                test_start:test_start + test_size
            ]

            for model_name, model in create_models().items():

                model.fit(X_train, y_train)

                probabilities = model.predict_proba(
                    X_test
                )[:, list(model.classes_).index(1)]

                predictions = (
                    probabilities >= 0.5
                ).astype(int)

                results.append({
                    "Ticker": ticker,
                    "Horizon": horizon.replace("Target_", ""),
                    "Fold": fold,
                    "Model": model_name,

                    "Brier_Score": brier_score_loss(
                        y_test, probabilities
                    ),

                    "Log_Loss": log_loss(
                        y_test,
                        probabilities,
                        labels=[0, 1]
                    ),

                    "Mean_Predicted_Probability": np.mean(
                        probabilities
                    ),

                    "Actual_Positive_Frequency": np.mean(
                        y_test
                    ),

                    "Accuracy": np.mean(
                        predictions == y_test
                    ),

                    "Test_Size": len(y_test)
                })

            test_start += test_size

# =====================================================
# 5. CREATE SUMMARY
# =====================================================

results_df = pd.DataFrame(results)

if results_df.empty:
    raise ValueError("No probability calibration results generated.")

summary = (
    results_df
    .groupby(["Horizon", "Model"])
    .agg(
        Experiments=("Brier_Score", "count"),
        Average_Brier_Score=("Brier_Score", "mean"),
        Average_Log_Loss=("Log_Loss", "mean"),
        Mean_Predicted_Probability=(
            "Mean_Predicted_Probability", "mean"
        ),
        Actual_Positive_Frequency=(
            "Actual_Positive_Frequency", "mean"
        ),
        Average_Accuracy=("Accuracy", "mean")
    )
    .reset_index()
)

# =====================================================
# 6. SAVE REPORTS
# =====================================================

results_file = os.path.join(
    REPORT_DIR,
    "V7_probability_calibration_detailed.csv"
)

summary_file = os.path.join(
    REPORT_DIR,
    "V7_probability_calibration_summary.csv"
)

results_df.to_csv(results_file, index=False)
summary.to_csv(summary_file, index=False)

# =====================================================
# 7. CALIBRATION DIAGNOSTIC PLOTS
# =====================================================

for horizon in ["1D", "5D"]:

    plt.figure(figsize=(8, 6))

    for model_name in [
        "LogisticRegression",
        "RandomForest"
    ]:

        subset = results_df[
            (results_df["Horizon"] == horizon) &
            (results_df["Model"] == model_name)
        ]

        plt.scatter(
            subset["Mean_Predicted_Probability"],
            subset["Actual_Positive_Frequency"],
            label=model_name,
            alpha=0.7
        )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        label="Perfect Calibration"
    )

    plt.xlabel("Mean Predicted Probability")
    plt.ylabel("Actual Positive Frequency")
    plt.title(f"V7 {horizon} Calibration Diagnostic")
    plt.legend()
    plt.grid(True)

    plot_file = os.path.join(
        VIS_DIR,
        f"V7_{horizon}_calibration.png"
    )

    plt.savefig(plot_file, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()

# =====================================================
# 8. DISPLAY RESULTS
# =====================================================

print("\n" + "=" * 70)
print("PROBABILITY CALIBRATION SUMMARY")
print("=" * 70)

print(
    summary.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)

print("\nTotal experiments:", len(results_df))

print("\nReports saved:")
print(results_file)
print(summary_file)

print("\nCalibration plots saved in:")
print(VIS_DIR)

print("\nV7 STEP 17 COMPLETE")


# In[ ]:


import os
import pandas as pd
import numpy as np

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

RESULT_DIR = os.path.join(BASE_DIR, "results")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

print("=" * 65)
print("GLOBALSTOCK AI V7 — STEP 19")
print("PER-ASSET PERFORMANCE ANALYSIS")
print("=" * 65)

# ============================================================
# 1. LOAD WALK-FORWARD RESULTS
# ============================================================

path = os.path.join(
    RESULT_DIR,
    "V7_walk_forward_results.csv"
)

df = pd.read_csv(path)

# Verify required columns
required = [
    "Ticker",
    "Horizon",
    "Fold",
    "Model",
    "Accuracy"
]

missing = [col for col in required if col not in df.columns]

if missing:
    raise ValueError(
        f"Missing columns: {missing}\n"
        f"Available columns: {list(df.columns)}"
    )

print("\nDATA LOADED SUCCESSFULLY")
print("Total experiments:", len(df))
print("Unique assets:", df["Ticker"].nunique())

# ============================================================
# 2. CALCULATE PER-ASSET AVERAGE PERFORMANCE
# ============================================================

asset_results = (
    df.groupby(
        ["Ticker", "Horizon", "Model"],
        as_index=False
    )
    .agg(
        Average_Accuracy=("Accuracy", "mean"),
        Average_Balanced_Accuracy=("Balanced_Accuracy", "mean"),
        Average_ROC_AUC=("ROC_AUC", "mean"),
        Fold_Count=("Fold", "nunique")
    )
)

# ============================================================
# 3. EXTRACT MAJORITY BASELINE
# ============================================================

baseline = asset_results[
    asset_results["Model"] == "Majority_Baseline"
][
    ["Ticker", "Horizon", "Average_Accuracy"]
].rename(
    columns={
        "Average_Accuracy": "Baseline_Accuracy"
    }
)

# ============================================================
# 4. COMPARE MACHINE LEARNING MODELS
# ============================================================

models = asset_results[
    asset_results["Model"].isin(
        ["LogisticRegression", "RandomForest"]
    )
].copy()

comparison = models.merge(
    baseline,
    on=["Ticker", "Horizon"],
    how="left"
)

if comparison["Baseline_Accuracy"].isna().any():
    raise ValueError(
        "Some assets do not have a matching majority baseline."
    )

comparison["Difference_pp"] = (
    comparison["Average_Accuracy"]
    - comparison["Baseline_Accuracy"]
) * 100

comparison["Beat_Baseline"] = (
    comparison["Difference_pp"] > 0
)

comparison["Performance"] = np.where(
    comparison["Beat_Baseline"],
    "Beat Baseline",
    "Did Not Beat Baseline"
)

# ============================================================
# 5. SAVE DETAILED PER-ASSET REPORT
# ============================================================

comparison_path = os.path.join(
    REPORT_DIR,
    "V7_per_asset_performance.csv"
)

comparison.to_csv(
    comparison_path,
    index=False
)

# ============================================================
# 6. CREATE MODEL SUMMARY
# ============================================================

summary = (
    comparison.groupby(
        ["Horizon", "Model"]
    )
    .agg(
        Assets=("Ticker", "nunique"),
        Average_Accuracy=("Average_Accuracy", "mean"),
        Average_Baseline=("Baseline_Accuracy", "mean"),
        Average_Difference_pp=("Difference_pp", "mean"),
        Assets_Beating_Baseline=("Beat_Baseline", "sum")
    )
    .reset_index()
)

summary["Beat_Baseline_Percent"] = (
    summary["Assets_Beating_Baseline"]
    / summary["Assets"]
) * 100

summary_path = os.path.join(
    REPORT_DIR,
    "V7_per_asset_performance_summary.csv"
)

summary.to_csv(
    summary_path,
    index=False
)

# ============================================================
# 7. IDENTIFY BEST AND WEAKEST RELATIVE RESULTS
# ============================================================

best = (
    comparison.sort_values(
        "Difference_pp",
        ascending=False
    )
    .groupby("Horizon")
    .head(5)
)

weakest = (
    comparison.sort_values(
        "Difference_pp",
        ascending=True
    )
    .groupby("Horizon")
    .head(5)
)

best_path = os.path.join(
    REPORT_DIR,
    "V7_best_relative_asset_results.csv"
)

weakest_path = os.path.join(
    REPORT_DIR,
    "V7_weakest_relative_asset_results.csv"
)

best.to_csv(best_path, index=False)
weakest.to_csv(weakest_path, index=False)

# ============================================================
# 8. DISPLAY RESULTS
# ============================================================

print("\nMODEL-LEVEL SUMMARY")
print("-" * 65)

print(
    summary.round(4).to_string(index=False)
)

print("\nTOP 5 RELATIVE RESULTS PER HORIZON")
print("-" * 65)

print(
    best[
        ["Ticker", "Horizon", "Model", "Difference_pp"]
    ].round(3).to_string(index=False)
)

print("\nBOTTOM 5 RELATIVE RESULTS PER HORIZON")
print("-" * 65)

print(
    weakest[
        ["Ticker", "Horizon", "Model", "Difference_pp"]
    ].round(3).to_string(index=False)
)

# ============================================================
# 9. COMPLETION REPORT
# ============================================================

print("\n" + "=" * 65)
print("STEP 19 COMPLETE")
print("=" * 65)

print("\nFILES SAVED:")

print(comparison_path)
print(summary_path)
print(best_path)
print(weakest_path)

print("\nTotal assets analysed:", comparison["Ticker"].nunique())
print("Total model comparisons:", len(comparison))

print("\nAll reports saved successfully.")


# In[ ]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

REPORT_DIR = os.path.join(BASE_DIR, "reports")
VIS_DIR = os.path.join(REPORT_DIR, "visualizations")

os.makedirs(VIS_DIR, exist_ok=True)

print("=" * 65)
print("GLOBALSTOCK AI V7 — STEP 20")
print("PERFORMANCE VISUALISATION")
print("=" * 65)

# ============================================================
# LOAD REPORTS
# ============================================================

comparison = pd.read_csv(
    os.path.join(REPORT_DIR, "V7_per_asset_performance.csv")
)

summary = pd.read_csv(
    os.path.join(
        REPORT_DIR,
        "V7_per_asset_performance_summary.csv"
    )
)

# ============================================================
# CHART 1 — MODEL ACCURACY VS BASELINE
# ============================================================

labels = summary["Horizon"] + " " + summary["Model"]

x = np.arange(len(summary))
width = 0.35

plt.figure(figsize=(12, 6))

plt.bar(
    x - width / 2,
    summary["Average_Accuracy"] * 100,
    width,
    label="ML Model"
)

plt.bar(
    x + width / 2,
    summary["Average_Baseline"] * 100,
    width,
    label="Majority Baseline"
)

plt.xticks(x, labels, rotation=20, ha="right")
plt.ylabel("Accuracy (%)")
plt.title("V7 Model Accuracy vs Baseline")
plt.legend()
plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "V7_accuracy_vs_baseline.png"),
    dpi=300
)

plt.show()
plt.close()

# ============================================================
# CHART 2 — MODEL COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    data=summary,
    x="Horizon",
    y="Average_Accuracy",
    hue="Model"
)

plt.ylabel("Average Accuracy")
plt.title("Logistic Regression vs Random Forest")
plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "V7_model_comparison.png"),
    dpi=300
)

plt.show()
plt.close()

# ============================================================
# CHART 3 — PER-ASSET PERFORMANCE HEATMAP
# ============================================================

for horizon in ["1D", "5D"]:

    subset = comparison[
        comparison["Horizon"] == horizon
    ].copy()

    heatmap_data = subset.pivot(
        index="Ticker",
        columns="Model",
        values="Difference_pp"
    )

    plt.figure(figsize=(9, 12))

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".1f",
        center=0,
        cmap="RdYlGn",
        linewidths=0.5
    )

    plt.title(
        f"{horizon} Per-Asset Improvement vs Baseline (pp)"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            VIS_DIR,
            f"V7_{horizon}_asset_heatmap.png"
        ),
        dpi=300
    )

    plt.show()
    plt.close()

# ============================================================
# CHART 4 — ASSETS BEATING BASELINE
# ============================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    data=summary,
    x="Horizon",
    y="Beat_Baseline_Percent",
    hue="Model"
)

plt.ylabel("Assets Beating Baseline (%)")
plt.title("Percentage of Assets Beating Majority Baseline")
plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    os.path.join(
        VIS_DIR,
        "V7_assets_beating_baseline.png"
    ),
    dpi=300
)

plt.show()
plt.close()

# ============================================================
# CHART 5 — PERFORMANCE DIFFERENCE
# ============================================================

plt.figure(figsize=(12, 6))

sns.barplot(
    data=summary,
    x="Horizon",
    y="Average_Difference_pp",
    hue="Model"
)

plt.axhline(0, linestyle="--")
plt.ylabel("Difference from Baseline (percentage points)")
plt.title("Average Model Improvement or Decline vs Baseline")

plt.tight_layout()

plt.savefig(
    os.path.join(
        VIS_DIR,
        "V7_average_baseline_difference.png"
    ),
    dpi=300
)

plt.show()
plt.close()

# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("STEP 20 COMPLETE")
print("=" * 65)

print("\nVISUALISATIONS SAVED:")

for file in sorted(os.listdir(VIS_DIR)):
    if file.startswith("V7_") and file.endswith(".png"):
        print(file)

print("\nLOCATION:")
print(VIS_DIR)


# In[ ]:


import os
from datetime import date
import pandas as pd

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

summary = pd.read_csv(
    os.path.join(
        REPORT_DIR,
        "V7_per_asset_performance_summary.csv"
    )
)

calibration = pd.read_csv(
    os.path.join(
        REPORT_DIR,
        "V7_probability_calibration_summary.csv"
    )
)

stats = pd.read_csv(
    os.path.join(
        REPORT_DIR,
        "V7_statistical_significance_report.csv"
    )
)

def get_row(horizon, model):
    row = summary[
        (summary["Horizon"] == horizon) &
        (summary["Model"] == model)
    ].iloc[0]
    return row

def pct(value):
    return f"{value * 100:.2f}%"

lines = []

lines.append("# GLOBALSTOCK AI V7")
lines.append("## Research Findings and Limitations Report")
lines.append(f"\nReport date: {date.today()}")
lines.append("\n---\n")

lines.append("## 1. Executive Summary\n")
lines.append(
    "GlobalStock AI V7 is an experimental machine-learning "
    "research project investigating historical price-direction "
    "classification across 34 financial assets."
)
lines.append(
    "The experiments compare Logistic Regression and Random "
    "Forest against a training-majority baseline across 1-day "
    "and 5-day prediction horizons."
)
lines.append(
    "The overall results do not demonstrate that either machine-"
    "learning model consistently improves on the baseline."
)

lines.append("\n## 2. Experimental Scope\n")
lines.append("- Assets analysed: 34")
lines.append("- Prediction horizons: 1-day and 5-day")
lines.append("- Models: Logistic Regression and Random Forest")
lines.append("- Validation: 5-fold expanding-window walk-forward validation")
lines.append("- Initial training proportion: 50%")
lines.append("- Purge gap: 5 observations")
lines.append("- Walk-forward experiments: 1,020")

lines.append("\n## 3. Model Performance\n")
lines.append(
    "| Horizon | Model | Accuracy | Baseline | Difference |"
)
lines.append("|---|---|---:|---:|---:|")

for horizon in ["1D", "5D"]:
    for model in ["LogisticRegression", "RandomForest"]:
        row = get_row(horizon, model)

        lines.append(
            f"| {horizon} | {model} | "
            f"{pct(row['Average_Accuracy'])} | "
            f"{pct(row['Average_Baseline'])} | "
            f"{row['Average_Difference_pp']:.2f} pp |"
        )

lines.append("\n## 4. Statistical Significance\n")
lines.append(
    "Paired asset-level statistical tests compared average "
    "model accuracy with the majority baseline. Holm correction "
    "was applied to account for multiple comparisons."
)

for _, row in stats.iterrows():
    lines.append(
        f"- {row['Horizon']} {row['Model']}: "
        f"mean difference {row['Mean_Accuracy_Difference'] * 100:.2f} "
        f"percentage points; Holm-adjusted p-value "
        f"{row['Holm_Adjusted_P_Value']:.5f}."
    )

lines.append("\n## 5. Probability Calibration\n")
lines.append(
    "Brier Score and Log Loss were used to examine the quality "
    "of predicted probabilities. Lower values indicate better "
    "probabilistic performance."
)

for _, row in calibration.iterrows():
    lines.append(
        f"- {row['Horizon']} {row['Model']}: "
        f"Brier Score {row['Average_Brier_Score']:.4f}; "
        f"Log Loss {row['Average_Log_Loss']:.4f}."
    )

lines.append("\n## 6. Per-Asset Analysis\n")
lines.append(
    "Per-asset comparisons identified variation across assets. "
    "Some individual experiments exceeded the baseline, while "
    "many performed below it. These isolated results are "
    "exploratory and do not establish future predictive ability."
)

lines.append("\n## 7. Important Limitations\n")
lines.append("- Historical results do not guarantee future performance.")
lines.append("- Accuracy is close to chance-level in many experiments.")
lines.append("- Asset returns may be correlated.")
lines.append("- Market regimes can change over time.")
lines.append("- Transaction costs and slippage were not modelled.")
lines.append("- Probability calibration requires further validation.")
lines.append("- The project has not established a reliable predictive edge.")
lines.append(
    "- The results are not suitable for real-money trading decisions."
)

lines.append("\n## 8. Future Research\n")
lines.append("- Test on a completely untouched future time period.")
lines.append("- Investigate changing market regimes.")
lines.append("- Study feature importance and feature stability.")
lines.append("- Evaluate probability calibration on independent data.")
lines.append("- Improve reproducibility and experiment tracking.")
lines.append("- Document computational and methodological limitations.")

lines.append("\n## 9. Conclusion\n")
lines.append(
    "GlobalStock AI V7 demonstrates a structured research workflow "
    "covering data preparation, feature engineering, walk-forward "
    "validation, statistical testing, stability analysis, baseline "
    "robustness, calibration and visualisation."
)
lines.append(
    "The current evidence does not support a claim that the tested "
    "machine-learning models outperform simple baselines. This "
    "negative result is an important part of the project's research "
    "contribution."
)

report = "\n".join(lines)

output_path = os.path.join(
    REPORT_DIR,
    "V7_research_findings_and_limitations.md"
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(report)

print("=" * 65)
print("STEP 21 COMPLETE")
print("=" * 65)
print("\nResearch report created:")
print(output_path)
print("\nReport characters:", len(report))
print("\nSections created:", report.count("\n## "))


# In[ ]:


import os
import pandas as pd

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

print("=" * 70)
print("GLOBALSTOCK AI V7 — STEP 22")
print("REPRODUCIBILITY AND PROJECT AUDIT")
print("=" * 70)

# Expected project directories
folders = [
    "data",
    "features",
    "cleaned_data",
    "models",
    "results",
    "reports",
    "reports/visualizations",
    "reports/final_report",
    "validation",
    "logs"
]

print("\n1. DIRECTORY AUDIT")
print("-" * 70)

for folder in folders:
    path = os.path.join(BASE_DIR, folder)
    status = "PASS" if os.path.isdir(path) else "MISSING"
    print(f"{folder:<30} {status}")

# Dataset audit
print("\n2. DATASET AUDIT")
print("-" * 70)

clean_dir = os.path.join(BASE_DIR, "cleaned_data")

clean_files = [
    f for f in os.listdir(clean_dir)
    if f.endswith("_clean.csv")
]

print("Cleaned datasets:", len(clean_files))
print("Expected datasets: 34")
print("Dataset status:", "PASS" if len(clean_files) == 34 else "REVIEW")

# Report audit
expected_reports = [
    "V7_walk_forward_summary.csv",
    "V7_statistical_significance_report.csv",
    "V7_model_stability_summary.csv",
    "V7_baseline_robustness_summary.csv",
    "V7_probability_calibration_summary.csv",
    "V7_final_research_scorecard.xlsx",
    "V7_research_status.csv",
    "V7_per_asset_performance.csv",
    "V7_per_asset_performance_summary.csv",
    "V7_best_relative_asset_results.csv",
    "V7_weakest_relative_asset_results.csv",
    "V7_research_findings_and_limitations.md"
]

print("\n3. RESEARCH REPORT AUDIT")
print("-" * 70)

report_results = []

for filename in expected_reports:
    path = os.path.join(BASE_DIR, "reports", filename)
    exists = os.path.isfile(path)

    report_results.append({
        "File": filename,
        "Status": "PASS" if exists else "MISSING"
    })

    print(f"{filename:<55} {'PASS' if exists else 'MISSING'}")

# Visualisation audit
print("\n4. VISUALISATION AUDIT")
print("-" * 70)

vis_dir = os.path.join(
    BASE_DIR, "reports", "visualizations"
)

visualisations = [
    "V7_accuracy_vs_baseline.png",
    "V7_model_comparison.png",
    "V7_1D_asset_heatmap.png",
    "V7_5D_asset_heatmap.png",
    "V7_assets_beating_baseline.png",
    "V7_average_baseline_difference.png"
]

visual_results = []

for filename in visualisations:
    path = os.path.join(vis_dir, filename)
    exists = os.path.isfile(path)

    visual_results.append({
        "File": filename,
        "Status": "PASS" if exists else "MISSING"
    })

    print(f"{filename:<45} {'PASS' if exists else 'MISSING'}")

# Save audit report
all_results = report_results + visual_results

audit = pd.DataFrame(all_results)

audit_path = os.path.join(
    BASE_DIR,
    "reports",
    "V7_reproducibility_audit.csv"
)

audit.to_csv(audit_path, index=False)

# Final status
passed = sum(x["Status"] == "PASS" for x in all_results)
total = len(all_results)

print("\n" + "=" * 70)
print("STEP 22 AUDIT SUMMARY")
print("=" * 70)

print("Reports and visualisations passed:", passed)
print("Total checked:", total)
print("Missing:", total - passed)

print("\nAudit saved:")
print(audit_path)

print("\nSTEP 22 COMPLETE")


# In[17]:


import os
import sys
import json
import hashlib
import platform
import pandas as pd
from datetime import datetime, timezone
from importlib.metadata import version, PackageNotFoundError

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

print("=" * 70)
print("GLOBALSTOCK AI V7 — STEP 23")
print("REPRODUCIBILITY MANIFEST")
print("=" * 70)

# ============================================================
# 1. FILE INVENTORY AND SHA-256 CHECKSUMS
# ============================================================

def calculate_sha256(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


manifest = []

for root, dirs, files in os.walk(BASE_DIR):

    # Avoid including temporary/cache directories
    dirs[:] = [
        d for d in dirs
        if d not in ["__pycache__", ".ipynb_checkpoints"]
    ]

    for filename in files:

        filepath = os.path.join(root, filename)

        relative_path = os.path.relpath(
            filepath, BASE_DIR
        )

        if relative_path in [
            "reports/V7_file_manifest.csv",
            "reports/V7_environment.json"
        ]:
            continue

        try:
            manifest.append({
                "Relative_Path": relative_path,
                "File_Size_Bytes": os.path.getsize(filepath),
                "SHA256": calculate_sha256(filepath)
            })

        except Exception as e:
            print("Could not process:", relative_path, str(e))


manifest_df = pd.DataFrame(manifest)

manifest_path = os.path.join(
    REPORT_DIR,
    "V7_file_manifest.csv"
)

manifest_df.to_csv(manifest_path, index=False)

print("\nFILE INVENTORY COMPLETE")
print("Files recorded:", len(manifest_df))

# ============================================================
# 2. CAPTURE SOFTWARE ENVIRONMENT
# ============================================================

packages = [
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "scipy",
    "yfinance",
    "openpyxl"
]

package_versions = {}

for package in packages:
    try:
        package_versions[package] = version(package)
    except PackageNotFoundError:
        package_versions[package] = "Not installed"

environment = {
    "Project": "GlobalStock AI V7",
    "Generated_UTC": datetime.now(timezone.utc).isoformat(),
    "Python_Version": sys.version,
    "Platform": platform.platform(),
    "Package_Versions": package_versions,
    "Project_Configuration": {
        "Assets": 34,
        "Prediction_Horizons": ["1D", "5D"],
        "Walk_Forward_Folds": 5,
        "Initial_Training_Proportion": 0.50,
        "Purge_Gap": 5,
        "Models": [
            "LogisticRegression",
            "RandomForest",
            "Majority_Baseline"
        ]
    }
}

environment_path = os.path.join(
    REPORT_DIR,
    "V7_environment.json"
)

with open(environment_path, "w", encoding="utf-8") as f:
    json.dump(environment, f, indent=4)

print("\nENVIRONMENT CAPTURE COMPLETE")

for package, package_version in package_versions.items():
    print(f"{package:<20} {package_version}")

# ============================================================
# 3. CREATE REQUIREMENTS FILE
# ============================================================

requirements_path = os.path.join(
    BASE_DIR,
    "requirements.txt"
)

with open(requirements_path, "w", encoding="utf-8") as f:

    for package, package_version in package_versions.items():

        if package_version != "Not installed":
            f.write(
                f"{package}=={package_version}\n"
            )

print("\nDEPENDENCY FILE CREATED")
print(requirements_path)

# ============================================================
# 4. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("STEP 23 COMPLETE")
print("=" * 70)

print("Files recorded:", len(manifest_df))
print("Manifest:", manifest_path)
print("Environment:", environment_path)
print("Requirements:", requirements_path)

print("\nAll reproducibility records saved successfully.")


# In[18]:


import os
import glob
import shutil
import nbformat
from nbconvert import PythonExporter

BASE_DIR = "/content/gdrive/MyDrive/GlobalStock_AI_V7"

print("=" * 70)
print("GLOBALSTOCK AI V7 — STEP 24")
print("SOURCE CODE ORGANISATION")
print("=" * 70)

# 1. Create organised source folders
folders = [
    "src",
    "src/features",
    "src/models",
    "src/validation",
    "notebooks",
    "scripts",
    "docs"
]

for folder in folders:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

print("\nPROJECT FOLDERS CREATED")

# 2. Locate the V7 notebook
notebook_candidates = glob.glob(
    "/content/gdrive/MyDrive/**/GlobalStock_AI_V7.ipynb",
    recursive=True
)

if not notebook_candidates:
    raise FileNotFoundError(
        "GlobalStock_AI_V7.ipynb was not found in Google Drive. "
        "Please check the notebook filename."
    )

NOTEBOOK_PATH = notebook_candidates[0]

print("\nNOTEBOOK FOUND:")
print(NOTEBOOK_PATH)

# 3. Preserve a copy in the organised notebooks folder
notebook_copy = os.path.join(
    BASE_DIR, "notebooks", "GlobalStock_AI_V7.ipynb"
)

if os.path.abspath(NOTEBOOK_PATH) != os.path.abspath(notebook_copy):
    shutil.copy2(NOTEBOOK_PATH, notebook_copy)

# 4. Read notebook and export code cells to Python
with open(NOTEBOOK_PATH, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

exporter = PythonExporter()
python_script, _ = exporter.from_notebook_node(notebook)

source_path = os.path.join(
    BASE_DIR, "src", "globalstock_ai_v7.py"
)

with open(source_path, "w", encoding="utf-8") as f:
    f.write(python_script)

# 5. Create package initialisation files
init_files = [
    "src/__init__.py",
    "src/features/__init__.py",
    "src/models/__init__.py",
    "src/validation/__init__.py"
]

for file_path in init_files:
    full_path = os.path.join(BASE_DIR, file_path)
    if not os.path.exists(full_path):
        with open(full_path, "w", encoding="utf-8") as f:
            f.write('"""GlobalStock AI V7 source package."""\n')

# 6. Create a source organisation guide
guide = """# GlobalStock AI V7 — Source Code Structure

## Folder organisation

- src/ — Exported Python source code
- src/features/ — Feature engineering module location
- src/models/ — Model development module location
- src/validation/ — Validation module location
- notebooks/ — Original research notebook
- scripts/ — Supporting execution scripts
- docs/ — Project documentation

## Main source file

`src/globalstock_ai_v7.py` is an exported Python version
of the research notebook.

The original notebook is preserved in `notebooks/`.

The existing research data, results, reports and models
remain in their original project folders.
"""

guide_path = os.path.join(BASE_DIR, "docs", "SOURCE_CODE_STRUCTURE.md")

with open(guide_path, "w", encoding="utf-8") as f:
    f.write(guide)

# 7. Verify generated files
required_files = [
    "src/globalstock_ai_v7.py",
    "src/__init__.py",
    "notebooks/GlobalStock_AI_V7.ipynb",
    "docs/SOURCE_CODE_STRUCTURE.md"
]

print("\n" + "=" * 70)
print("SOURCE ORGANISATION AUDIT")
print("=" * 70)

passed = 0

for relative_path in required_files:
    full_path = os.path.join(BASE_DIR, relative_path)

    if os.path.isfile(full_path):
        print("PASS:", relative_path)
        passed += 1
    else:
        print("MISSING:", relative_path)

print("\n" + "=" * 70)

if passed == len(required_files):
    print("STEP 24 COMPLETE")
    print("Files verified:", passed, "/", len(required_files))
    print("Python source size:", os.path.getsize(source_path), "bytes")
else:
    print("STEP 24 NEEDS ATTENTION")
    print("Files verified:", passed, "/", len(required_files))

print("=" * 70)

