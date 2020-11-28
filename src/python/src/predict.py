import argparse
import pandas as pd
from config import config
from preprocessing import preprocessor as pp
from utils import utils


def predict_pipeline(path):
    df = utils.read_dataset(path)

    df = pp.load_and_transform_encoder(df, cat_cols=config.CAT_VARS, encodings_path=config.ENCODINGS_PATH)

    df = pp.convert_empty_lines_to_na(df, cols=['TotalCharges'])

    df = pp.remove_na(df)

    df = pp.encode_target(df, target=config.TARGET)
    return df


def run_prediction(opts):
    df = predict_pipeline(opts.source)
    lr = utils.load_model(opts.model_source)
    preds = lr.predict(df[config.FEATURES])
    df = pd.concat([df, pd.Series(preds)], axis=1).rename({0: 'preds'}, axis=1)
    df.to_csv(f'{opts.destination}predictions.csv', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict phase', prog='predict', usage='%(prog) [options]')
    parser.add_argument('--source', required=True, type=str, help="Source path of the prediction dataset")
    parser.add_argument('--model_source', required=True, type=str, help="Source path of the trained model")
    parser.add_argument('--destination', required=True, type=str, help="Destination folder of the predictions")
    args = parser.parse_args()
    run_prediction(args)
