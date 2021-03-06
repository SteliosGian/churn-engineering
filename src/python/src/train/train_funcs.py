import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mlflow
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_validate, cross_val_predict
from models.logistic_model import LogisticModel


def model_create(params: dict):
    """
    Create the Logistic Regression model.
    :param params: Params dictionary
    :return: Model (LogisticModel)
    """
    model = LogisticModel(**params)
    return model


def model_evaluate(df: pd.DataFrame, features: list, target: str, metrics: dict, model, cv_rounds: int = 5):
    """
    Evaluate the model's performance with cross-validation.
    :param df: Dataframe
    :param features: Features list
    :param target: Target variable
    :param metrics: Metrics dictionary
    :param model: Model from 'model_create" function
    :param cv_rounds: Cross-validation rounds
    :return: Scores, probability predictions, and binary predictions
    """
    df = df.copy()
    scores = cross_validate(estimator=model.model,
                            X=df[features],
                            y=df[target],
                            scoring=metrics,
                            cv=cv_rounds,
                            return_train_score=True)

    preds_proba = cross_val_predict(estimator=model.model,
                                    X=df[features],
                                    y=df[target],
                                    cv=cv_rounds,
                                    method="predict_proba")[:, 1]
    preds = cross_val_predict(estimator=model.model,
                              X=df[features],
                              y=df[target],
                              cv=cv_rounds,
                              method="predict")
    return scores, preds_proba, preds


def model_train(model, df: pd.DataFrame, features: list, target: str, path: str = None) -> None:
    """
    Train and save the model.
    :param model: Model from 'model_create' function
    :param df: Dataframe
    :param features: Features list
    :param target: Target variable
    :param path: Path to save the model
    :return: None
    """
    df = df.copy()
    model.fit(df[features], df[target])
    model.save_model(path)


def plot_prob_hist(predictions: np.ndarray, plot_path: str) -> None:
    """
    Saves the histogram of the predicted probabilities.
    :param predictions: Predictions array
    :param plot_path: Path to save the plot
    :return: None
    """
    sns.histplot(predictions, kde=True)
    plt.savefig(f'{plot_path}/probs_histogram.png', dpi=400)


def plot_conf_matrix(df: pd.DataFrame, target: str, predictions: np.ndarray, plot_path: str) -> None:
    """
    Saves the confusion matrix
    :param df: Dataframe
    :param target: Target variable
    :param predictions: Predictions array
    :param plot_path: Path to save the plot
    :return: None
    """
    df = df.copy()
    conf_mat = confusion_matrix(df[target], predictions)
    df_cm = pd.DataFrame(conf_mat)
    sns.set(font_scale=1.4)
    sns.heatmap(df_cm / np.sum(df_cm), annot=True,
                fmt='.2%', cmap='Blues')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.savefig(f'{plot_path}/confusion.png', dpi=400)


def log_metrics(metrics: dict, params: dict, tracking_uri: str,
                plot_path: str, models_path: str, round_dec: int = 3) -> None:
    """
    Logs model metrics, hyperparameters, plots, and model instance.
    :param metrics: Metrics dictionary
    :param params: Parameter dictionary to use
    :param tracking_uri: The tracking uri. If local, it is the tracking folder to use
    :param plot_path: Path of the saved plots
    :param models_path: Path of the saved trained model
    :param round_dec: Number of decimals to round the float numbers
    :return: None
    """
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("Test experiment")
    with mlflow.start_run():
        for name, value_list in metrics.items():
            mlflow.log_metric(name, round(value_list.mean(), round_dec))
        mlflow.log_params(params)
        mlflow.log_artifact(f'{plot_path}/probs_histogram.png')
        mlflow.log_artifact(f'{plot_path}/confusion.png')
        mlflow.log_artifact(f'{models_path}/model')
