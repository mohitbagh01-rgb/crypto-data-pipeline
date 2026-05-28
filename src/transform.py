import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)

    df = df.drop_duplicates()

    # drop high null columns
    threshold = 0.7
    null_ratio = df.isnull().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index
    df = df.drop(columns=cols_to_drop)

    # numeric conversion (SAFE)
    numeric_cols = [
        "marketsing", "volumeEx", "volumeQt", 
        "pricechange", "quickTradePrice",
        "volume", "quickTradePriceChange"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # fill nulls
    df = df.fillna(0)

    print("data transformed successfully")

    return df