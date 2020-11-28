import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def fit_and_save_encodings(df: pd.DataFrame, cat_cols: list, encodings_path: str) -> None:
    """
    Fit and save the encodings of the categories
    :param df: Dataframe
    :param cat_cols: List of categorical columns
    :param encodings_path: Path of the .npy encodings
    :return: None
    """
    df = df.copy()
    for col in cat_cols:
        encoder = LabelEncoder()
        encoder.fit(df[col])
        np.save(f"{encodings_path}/{col}_encoder.npy", encoder.classes_)


def load_and_transform_encoder(df: pd.DataFrame, cat_cols: list, encodings_path: str) -> pd.DataFrame:
    """
    Load the encoder and transform the categorical columns
    :param df: Dataframe
    :param cat_cols: List of categorical columns
    :param encodings_path: Path of the .npy encodings
    :return: Dataframe with encoded categorical column
    """
    df = df.copy()
    for col in cat_cols:
        encoder = LabelEncoder()
        encoder.classes_ = np.load(f"{encodings_path}/{col}_encoder.npy", allow_pickle=True)
        df[col] = encoder.transform(df[col])
    return df


def load_and_invert_transform_encoder(df: pd.DataFrame, cat_cols: list, encodings_path: str) -> pd.DataFrame:
    """
    Load the encoder and transform the categorical columns
    :param df: Dataframe
    :param cat_cols: List of categorical columns
    :param encodings_path: Path of the .npy encodings
    :return: Dataframe with encoded categorical column
    """
    df = df.copy()
    for col in cat_cols:
        encoder = LabelEncoder()
        encoder.classes_ = np.load(f"{encodings_path}/{col}_encoder.npy", allow_pickle=True)
        df[col] = encoder.inverse_transform(df[col])
    return df


def convert_empty_lines_to_na(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    df[cols] = np.where(df[cols] == " ", np.nan, df[cols]).astype(float)
    return df


def remove_na(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna()
    return df


def encode_target(df: pd.DataFrame, target: str) -> pd.DataFrame:
    df = df.copy()
    df[target] = np.where(df[target] == 'Yes', True, False)
    return df
