#!/usr/bin/env bash

cd "$(dirname $0)"

set -e

. ./settings.sh

cd "$APP_DIR"

sbt assembly

spark-submit --class spark.sparkDriver "${JAR_FILE_PATH}"