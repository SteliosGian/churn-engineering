FROM python:3.7-buster

WORKDIR usr/src/app

# Install pipenv python packaging tool
RUN pip install pipenv

# Copy and install dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system

# Copy project files
COPY ./src/python/ .

# Copy docker shell scripts
COPY ./docker/docker-entrypoint-prediction.sh .
COPY ./docker/docker-entrypoint-training.sh .
COPY ./docker/settings.sh .
