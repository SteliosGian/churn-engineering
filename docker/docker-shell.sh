#!/usr/bin/env bash

#####################################################
#########       DEPRECATED - Don't use!        ######
######### Use docker-compose-shell.sh instead! ######
#####################################################

# Get argument for either training/prediction/both (default: both)
ARG=${1-both}

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
docker build -t churn -f docker/Dockerfile .

# Run docker train/predict/both
if [[ $ARG == "train" ]]
then
  echo "Running training"
  docker run \
  -v ${PWD}/src/python/src/trained_models:/usr/src/app/src/trained_models \
  churn \
  /bin/bash \
  ./docker-entrypoint-training.sh
elif [[ $ARG == 'predict' ]]
 then
   echo "Running prediction"
   docker run \
   -v ${PWD}/src/python/src/trained_models:/usr/src/app/src/trained_models \
   -v ${PWD}/src/python/src/data:/usr/src/app/src/predictions \
   churn \
   /bin/bash \
   ./docker-entrypoint-prediction.sh
elif [[ $ARG == 'both' ]]
 then
   echo "Running both training and prediction"
   echo "Running training"
   docker run \
   -v ${PWD}/src/python/src/trained_models:/usr/src/app/src/trained_models \
   churn \
   /bin/bash \
   ./docker-entrypoint-training.sh
   echo "Running prediction"
   docker run \
   -v ${PWD}/src/python/src/trained_models:/usr/src/app/src/trained_models \
   -v ${PWD}/src/python/src/data:/usr/src/app/src/predictions \
   churn \
   /bin/bash ./docker-entrypoint-prediction.sh
else
  usage
fi
