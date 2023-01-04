#!/bin/sh

CURRENT_SCRIPT_DIR="$(dirname $(readlink --canonicalize $0))"
PROJECT_ROOT="$CURRENT_SCRIPT_DIR/../../"

## delete previous output
rm -rf $PROJECT_ROOT/out/dsa_heldenbogen

## generate new; using a docker
## see https://github.com/OpenAPITools/openapi-generator#3---usage
## see https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/python-fastapi.md
## see https://github.com/OpenAPITools/openapi-generator/blob/master/docs/file-post-processing.md
docker run --rm \
    -u $(id -u):$(id -g) \
    --volume "$PROJECT_ROOT:/local/" \
    --env PYTHON_POST_PROCESS_FILE="/local/tools/api-generator/post-process.sh" \
    openapitools/openapi-generator-cli:v6.2.1 \
    generate \
    --generator-name python-fastapi \
    --input-spec /local/tools/api-generator/api-spec.yaml \
    --config /local/tools/api-generator/openapi-generator-config.yaml \
    --ignore-file-override /local/tools/api-generator/openapi-generator-ignore \
    --output /local/out/dsa_heldenbogen \
    --enable-post-process-file