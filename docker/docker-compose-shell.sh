#!/usr/bin/env bash

# Get argument for either training/prediction/both (default: both)
ARG=${1-both}

echo "Running ${ARG}"

# File paths
TRAINING_ENTRYPOINT=./docker-entrypoint-training.sh
PREDICTION_ENTRYPOINT=./docker-entrypoint-prediction.sh
SPARK_ENTRYPOINT=./docker-entrypoint-spark.sh
DOCKER_COMPOSE_PATH=docker/docker-compose.yml

usage ()
{
  echo -e "\nUsage: $0 [arguments] \n"
  echo "Argument should be either 'train', 'predict', or 'both'."
  echo "train: Run the training pipeline and save the trained model."
  echo "predict: Run the predict pipeline and save the predictions.csv."
  echo "both: Run both the training and the predictions pipeline. This saves the model and the predictions.csv."
  echo "NOTE: To run the 'predict', the trained model needs to exist in the 'trained_models' directory."
  exit
}

# Build docker
docker-compose -f ${DOCKER_COMPOSE_PATH} build

# Start mlflow server
docker-compose -f ${DOCKER_COMPOSE_PATH} up -d mlflow-server


echo "Running Spark"
docker-compose \
  -f ${DOCKER_COMPOSE_PATH} \
  run spark \
  /bin/bash ${SPARK_ENTRYPOINT}

# Run docker train/predict/both
if [[ $ARG == "train" ]]
then
  echo "Running training"
  docker-compose \
  -f ${DOCKER_COMPOSE_PATH} \
  run ml-model \
  /bin/bash ${TRAINING_ENTRYPOINT}
elif [[ $ARG == 'predict' ]]
 then
   echo "Running prediction"
   docker-compose \
   -f ${DOCKER_COMPOSE_PATH} \
   run ml-model \
   /bin/bash ${PREDICTION_ENTRYPOINT}
elif [[ $ARG == 'both' ]]
 then
   echo "Running both training and prediction"
   echo "Running training"
   docker-compose \
   -f ${DOCKER_COMPOSE_PATH} \
   run ml-model \
   /bin/bash ${TRAINING_ENTRYPOINT}
   echo "Running prediction"
   docker-compose \
   -f ${DOCKER_COMPOSE_PATH} \
   run ml-model \
   /bin/bash ${PREDICTION_ENTRYPOINT}
else
  usage
fi
