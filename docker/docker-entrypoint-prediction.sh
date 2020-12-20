#!/usr/bin/env bash

cd "$(dirname $0)"

set -e

. ./settings.sh

echo "Running prediction pipeline"

cd "$APP_DIR"

echo "Creating predictions directory"
mkdir -p "${PREDICTION_OUTPUT_PATH}"

echo "Executing prediction"
python src/predict.py \
       --source ${TRAINING_DATA_PATH} \
       --model_source ${MODELS_DIR}model \
       --destination ${PREDICTION_OUTPUT_PATH}

echo "Prediction executed successfully!"