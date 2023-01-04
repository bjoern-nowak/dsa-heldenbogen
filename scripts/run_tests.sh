#!/bin/bash

## load environment
source "${BASH_SOURCE%/*}/env.sh"

## run tests
poetry run python -m unittest discover --start-directory "$TESTS_DIR" --top-level-directory "$ROOT_DIR"
