import pandas as pd
import pickle


def read_dataset(path: str):
    """
    Read dataset
    :param path: Path of the dataset
    :return: Dataframe
    """
    df = pd.read_csv(path)
    return df


def load_model(path: str):
    model = pickle.load(open(f'{path}', 'rb'))
    return model
