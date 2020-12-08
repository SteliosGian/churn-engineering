#!/usr/bin/env bash

cd "$(dirname $0)"

set -e

. ./settings.sh

echo "Running training pipeline"

cd "$APP_DIR"

echo "Creating models directory"
mkdir -p "${MODELS_DIR}"

echo "Executing training"
python src/train.py \
       --source ${TRAINING_DATA_PATH} \
       --destination ${MODELS_DIR}

echo "Training executed successfully!"