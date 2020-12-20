#!/usr/bin/env bash

cd "$(dirname $0)"

set -e

. ./settings.sh

echo "Running prediction pipeline"

cd "$APP_DIR"

echo "Creating mlflow directory"
mkdir -p "mlruns"