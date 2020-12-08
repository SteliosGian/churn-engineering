#!/bin/env bash

export APP_DIR=/usr/src/app

export MODELS_DIR=${APP_DIR}/src/trained_models/

export TRAINING_DATA_PATH=${APP_DIR}/src/data/

export PREDICTION_DATA_PATH=${APP_DIR}/src/data/

echo "Setting environment variables."
echo "============================="
env
echo "============================="