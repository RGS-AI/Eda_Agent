import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Loaded dataset with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return None