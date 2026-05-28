from src.ingest import get_data
from src.transform import transform_data
from src.load import save_data

def run_pipeline():
    print("Pipeline started")

    data = get_data()

    if data is None:
        print("Pipeline stopped: ingestion failed")
        return

    df = transform_data(data)

    save_data(df)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()