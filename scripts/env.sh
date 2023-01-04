#!/bin/bash

CURRENT_SCRIPT_DIR="$(dirname $(readlink --canonicalize $0))"
ROOT_DIR="$CURRENT_SCRIPT_DIR/.."
SRC_DIR="$ROOT_DIR/dsa_heldenbogen"
TESTS_DIR="$ROOT_DIR/tests"
