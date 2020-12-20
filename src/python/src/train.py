import argparse
from config import config
from preprocessing import preprocessor as pp
from utils import utils
from train import train_funcs as tf


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

    model = tf.model_create(config.PARAMS_LOGISTIC)

    scores = tf.model_evaluate(df, features=config.FEATURES, target=config.TARGET, metrics=config.SCORING_CV, model=model, cv_rounds=5)

    tf.log_metrics(metrics=scores, tracking_uri=config.TRACKING_URI)

    tf.model_train(model=model, df=df, features=config.FEATURES, target=config.TARGET, path=opts.destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training phase', prog='train', usage='%(prog) [options]')
    parser.add_argument('--source', required=True, type=str, help="Source path of the training dataset")
    parser.add_argument('--destination', required=True, type=str, help="Destination folder of the trained model")
    args = parser.parse_args()
    run_training(args)
