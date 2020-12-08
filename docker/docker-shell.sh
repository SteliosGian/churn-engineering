#!/usr/bin/env bash

# Get argument for either training/prediction/both
ARG=${1: train}

# Build docker
docker build -t churn -f docker/Dockerfile .
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
   /bin/bash \
   ./docker-entrypoint-prediction.sh
fi
