# Customer Churn - Engineering

[![Build Status](https://travis-ci.com/SteliosGian/churn-engineering.svg?branch=master)](https://travis-ci.com/SteliosGian/churn-engineering)
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#mlflow-server">MLflow Server</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#notes">Notes</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The main purpose of this project, is to focus on the engineering
part and not so on the modelling part. We will create efficient data pipelines and
will adhere to coding best practices using different tools, languages, and technologies like
Python, Scala, Spark, Docker, CI/CD tools, etc.

Note: This repo will be used for testing different technologies.

### Built With

* [Docker](https://www.docker.com/)
* [MLflow](https://mlflow.org/)
* [Travis CI](https://travis-ci.com/)
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
* [Scikit-learn](https://scikit-learn.org/stable/index.html)



## Getting Started

The dataset for this project is taken from <a href="https://www.kaggle.com/blastchar/telco-customer-churn" target="_blank">Kaggle</a>. 
It is a simple dataset regarding customer churn including
both numeric and categorical features. It is a classification task with the target variable being binary (True/False),
meaning that if a customer has left the company, the target variable is True/1, otherwise it is False/0.

It is necessary to save the csv file from Kaggle to the <b>"data"</b> (src/python/src/data/) directory
renaming it as "telco_churn.csv" in order for the pipeline to work.

To run the project, you need to clone this repo and run the docker/docker-compose-shell.sh script.

This script runs the train, predict, or both phases. To run only the train phase, 
include the argument "train" to the script. For the predict phase, add "predict",
and for both, either run it with no arguments or add "both".

Clone the repo
```Bash
git clone https://github.com/SteliosGian/churn-engineering.git
```

Run the script
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

### MLflow Server

The project starts a local MLflow server running in the background, which you can access at
http://127.0.0.1:5000/ . <br>
With <a href="https://mlflow.org/" target="_blank">MLflow</a>, you can track custom metrics and hyperparameters 
as well as log artifacts such as plots and models.

![mlflow_gif.gif](mlflow_gif.gif)

### Prerequisites

<a href="https://www.docker.com/" target="_blank">Docker</a> must be installed in order to run the project with Docker. 
Otherwise, it can be executed by running the python scripts (train.py/predict.py) individually.

### Notes
<a href="https://spark.apache.org/" target="_blank">Spark</a> is not needed for this project because the amount of data is not that large. However, a small pipeline is created in the branch "spark" using <a href="https://www.scala-lang.org/" target="_blank">Scala</a>


## Roadmap
<ul>
    <li>Docker &#9745; </li>
    <li>Shell scripts &#9745; </li>
    <li>TravisCI &#9745;</li>
    <li>MLflow &#9745;</li>
    <li>Spark &#9745;</li>
    <li>API  </li>
</ul>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-white.svg?
[linkedin-url]: https://linkedin.com/in/stelios-giannikis
