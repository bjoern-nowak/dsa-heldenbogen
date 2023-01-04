#!/bin/bash

## load environment
source "${BASH_SOURCE%/*}/env.sh"

## start server
(cd "$SRC_DIR" && poetry run python main.py)
