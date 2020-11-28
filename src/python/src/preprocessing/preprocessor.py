from pandas import pd
from numpy import np
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
