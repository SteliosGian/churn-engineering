# Customer Churn - Engineering

[![Build Status](https://travis-ci.com/SteliosGian/churn-engineering.svg?branch=master)](https://travis-ci.com/SteliosGian/churn-engineering)

The main purpose of this project, is to focus on the engineering 
part and not so on the modelling part. We will create efficient data pipelines and
will adhere to coding best practices using different tools, languages, and technologies like
Python, Scala, Spark, Docker, CI/CD tools, etc.

Note: This repo will be used for testing different technologies.

## Getting Started

To run the project, you need to clone this repo and run the docker/docker-compose-shell.sh script.

This script runs the train, predict, or both phases. To run only the train phase, 
include the argument "train" to the script. For the predict phase, add "predict",
and for both, either run it with no arguments or add "both".

```Bash
./docker/docker-compose-shell.sh
```
Make sure the script has the adequate permissions
```Bash
chmod +x docker/docker-compose-shell.sh
```
or run
```Bash
bash docker/docker-compose-shell.sh
```

### MLFlow Server

The project starts a local MLFlow server running in the background, which you can access at
http://127.0.0.1:5000/ <br>
With <a href="https://mlflow.org/" target="_blank">MLFlow</a>, you can track custom metrics and hyperparameters as well as log artifacts such as plots and models.

![mlflow_gif.gif](mlflow_gif.gif)

### Prerequisites

Docker must be installed in order to run the project with Docker. Otherwise, it can be ran
by running the python scripts (train.py/predict.py) individually.


### Installing

TBC

## Built With

TBC

## Roadmap
<ul>
    <li>Docker &#9745; </li>
    <li>Shell scripts &#9745; </li>
    <li>TravisCI &#9745;</li>
    <li>MLFlow &#9745;</li>
    <li>Spark  </li>
    <li>API  </li>
</ul>

