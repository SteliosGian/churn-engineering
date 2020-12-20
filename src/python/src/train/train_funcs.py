import pandas as pd
import mlflow
from sklearn.model_selection import cross_validate
from models.logistic_model import LogisticModel


def model_create(params: dict):
    model = LogisticModel(**params)
    return model


def model_evaluate(df: pd.DataFrame, features: list, target: str, metrics: dict, model, cv_rounds=5) -> dict:
    df = df.copy()
    scores = cross_validate(estimator=model.model,
                            X=df[features],
                            y=df[target],
                            scoring=metrics,
                            cv=cv_rounds,
                            return_train_score=True)
    return scores


def model_train(model, df: pd.DataFrame, features: list, target: str, path: str = None):
    df = df.copy()
    model.fit(df[features], df[target])
    model.save_model(path)


def log_metrics(metrics: dict, tracking_uri: str) -> None:
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("Test experiment")
    with mlflow.start_run():
        for name, value_list in metrics.items():
            mlflow.log_metric(name, round(value_list.mean(), 3))
            # mlflow.log_artifact('file_path')
            # mlflow.lightgbm.log_model(model, 'src/trained_models')
