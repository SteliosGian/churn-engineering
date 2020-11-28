import argparse
from config import config
from preprocessing import preprocessor as pp
from models.logistic_model import LogisticModel
from utils import utils


def predict_pipeline(path):
    pass


def run_prediction(opts):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Predict phase', prog='predict', usage='%(prog) [options]')
    parser.add_argument('--source', required=True, type=str, help="Source path of the prediction dataset")
    parser.add_argument('--model_source', required=True, type=str, help="Source path of the trained model")
    parser.add_argument('--destination', required=True, type=str, help="Destination folder of the predictions")
    args = parser.parse_args()
    run_prediction(args)
