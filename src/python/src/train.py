import argparse
from config import config
from preprocessing import preprocessor as pp
from models.logistic_model import LogisticModel
from utils import utils
from train import train_funcs as tf
import mlflow
from sklearn.metrics import recall_score, precision_score


def training_pipeline(path):
    df = utils.read_dataset(path)

    pp.fit_and_save_encodings(df, cat_cols=config.CAT_VARS, encodings_path=config.ENCODINGS_PATH)
    df = pp.load_and_transform_encoder(df, cat_cols=config.CAT_VARS, encodings_path=config.ENCODINGS_PATH)

    df = pp.convert_empty_lines_to_na(df, cols=['TotalCharges'])

    df = pp.remove_na(df)

    df = pp.encode_target(df, target=config.TARGET)
    return df


def run_training(opts):
    df = training_pipeline(opts.source)

    preds, y_test = tf.model_train(df, features=config.FEATURES, target=config.TARGET,
                           split='true', params=config.PARAMS_LOGISTIC)
    recall = recall_score(y_test, preds)
    precision = precision_score(y_test, preds)

    print("START MLFLOW")
    mlflow.set_tracking_uri(config.TRACKING_URI)
    mlflow.set_experiment("Test experiment")

    with mlflow.start_run():
        mlflow.log_metric('recall', recall)
        mlflow.log_metric('precision', precision)
        # mlflow.log_artifact('src/plots/probability_dist_20201112_0837.png')
        # mlflow.lightgbm.log_model(model, 'src/trained_models')

    tf.model_train(df, features=config.FEATURES, target=config.TARGET,
                   split='false', params=config.PARAMS_LOGISTIC, path=opts.destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training phase', prog='train', usage='%(prog) [options]')
    parser.add_argument('--source', required=True, type=str, help="Source path of the training dataset")
    parser.add_argument('--destination', required=True, type=str, help="Destination folder of the trained model")
    args = parser.parse_args()
    run_training(args)
