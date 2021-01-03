#!/bin/env bash

export APP_DIR=/usr/src/app

export MODELS_DIR=${APP_DIR}/src/trained_models/

#export TRAINING_DATA_PATH=${APP_DIR}/src/data/telco_churn.csv
export TRAINING_DATA_PATH=${APP_DIR}/src/data/parquet/

export PREDICTION_DATA_PATH=${APP_DIR}/src/data/

export PREDICTION_OUTPUT_PATH=${APP_DIR}/src/predictions/

export JAR_FILE_PATH=${APP_DIR}/target/scala-2.12/customer_chur-assembly-0.1.jar

echo "Setting environment variables."
echo "============================="
env
echo "============================="