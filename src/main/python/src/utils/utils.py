import pandas as pd
import pickle
import os


# def read_dataset(path: str):
#     """
#     Read dataset
#     :param path: Path of the dataset
#     :return: Dataframe
#     """
#     df = pd.read_csv(path)
#     return df

def read_dataset(path: str):
    """
    Read dataset
    :param path: Path of the dataset
    :return: Dataframe
    """
    for file in os.listdir(path):
        if file.endswith(".parquet"):
            df = pd.read_parquet(os.path.join(path, file), engine='pyarrow')
            return df


def load_model(path: str):
    """
    Load serialized model
    :param path: Model path
    :return: Model instance
    """
    model = pickle.load(open(f'{path}', 'rb'))
    return model
