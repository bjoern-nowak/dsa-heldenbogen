import functools
import io

import yaml
from fastapi import FastAPI
from fastapi.responses import Response
from starlette.responses import RedirectResponse

from . import api

app = FastAPI()


@app.get('/', tags=['root'])
def index():
    return RedirectResponse(url='/docs')


# Author: https://github.com/hjoukl
# Source: https://github.com/tiangolo/fastapi/issues/1140
@app.get('/openapi.yaml', include_in_schema=True, tags=['root'])
@functools.lru_cache()  # TODO: is this required only for async?
def read_openapi_yaml():
    openapi_json = app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s, sort_keys=False, allow_unicode=True)
    return Response(yaml_s.getvalue(), media_type='text/yaml')


app.include_router(api.router, prefix='/api')
