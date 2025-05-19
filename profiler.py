import pandas as pd

def summarize_data(df):
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numerical_summary": df.describe(include='number').T.to_dict(),
        "categorical_summary": df.describe(include='object').T.to_dict()
    }
    return summary