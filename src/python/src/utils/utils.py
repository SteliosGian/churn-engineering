import pandas as pd


def read_dataset(path: str):
    df = pd.read_csv(path)
    return df
