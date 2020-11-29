import pandas as pd
from sklearn.model_selection import train_test_split
from models.logistic_model import LogisticModel


def model_train(df: pd.DataFrame, features: list, target: str,
                split: bool, params: dict, path: str = None):
    df = df.copy()
    if split:
        X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
        model = LogisticModel(**params)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        return preds
    elif not split:
        model = LogisticModel(**params)
        model.fit(df[features], df[target])
        model.save_model(path)
    else:
        raise Exception('Split needs to be True/False')
