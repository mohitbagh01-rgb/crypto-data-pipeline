from pathlib import Path
from datetime import datetime

def save_data(df):
    # timestamped filename
    filename = f"market_{datetime.now().date()}.parquet"

    output_path = Path(f"data/processed_data/{filename}")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(output_path, index=False)

    print("data saved successfully:", output_path)