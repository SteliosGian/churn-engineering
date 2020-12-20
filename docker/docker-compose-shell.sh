#!/usr/bin/env bash

# Get argument for either training/prediction/both (default: both)
ARG=${1-both}

usage ()
{
  echo -e "\nUsage: $0 [arguments] \n"
  echo "Argument should be either 'train', 'predict', or 'both'."
  echo "train: Run the training pipeline and save the trained model."
  echo "predict: Run the predict pipeline and save the predictions.csv."
  echo "both: Run both the training and the predictions pipeline. This saves the model and the predictions.csv."
  echo "NOTE: To run the 'train', the trained model needs to exist in the 'trained_models' directory."
  exit
}

# Build docker
docker-compose -f docker/docker-compose.yml build

# Start mlflow server
docker-compose -f docker/docker-compose.yml run -d mlflow-server

# Run docker train/predict/both
if [[ $ARG == "train" ]]
then
  echo "Running training"
  docker-compose \
  -f docker/docker-compose.yml \
  run ml-model \
  /bin/bash ./docker-entrypoint-training.sh
elif [[ $ARG == 'predict' ]]
 then
   echo "Running prediction"
   docker-compose \
   -f docker/docker-compose.yml \
   run ml-model \
   /bin/bash ./docker-entrypoint-prediction.sh
elif [[ $ARG == 'both' ]]
 then
   echo "Running both training and prediction"
   echo "Running training"
   docker-compose \
   -f docker/docker-compose.yml \
   run ml-model \
   /bin/bash ./docker-entrypoint-training.sh
   echo "Running prediction"
   docker-compose \
   -f docker/docker-compose.yml \
   run ml-model \
   /bin/bash ./docker-entrypoint-prediction.sh
else
  usage
fi
