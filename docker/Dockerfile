FROM python:3.7-buster

WORKDIR usr/src/app

# Install pipenv python packaging tool
RUN pip install pipenv

# Copy project files
COPY ./src/python/ .

# Copy and install dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system
