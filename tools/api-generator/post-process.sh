#!/bin/sh -e

## fix imports since openapi v5.4.0 generator python-fastapi is still beta and does not correctly handle modelNameSuffix
sed --in-place "s|_dto_dto import|_dto import|" "$@"

## generator model package can not be set
sed --in-place "s|from api.models.|from api.model.|" "$@"
