import functools
import io

import yaml
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.responses import Response
from starlette.responses import RedirectResponse

from app.api.v1.endpoints import hero
from app.api.v1.endpoints import meta

api = FastAPI()

router = APIRouter()


@api.get('/', tags=['root'])
def index():
    # TODO we shall not must use the api prefix manually
    return RedirectResponse(url='/api/v1/docs')


# Source: https://github.com/tiangolo/fastapi/issues/1140
@api.get('/openapi.yaml', include_in_schema=False, tags=['root'])
@functools.lru_cache()  # TODO: is this required only for async?
def read_openapi_yaml():
    openapi_json = api.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s, sort_keys=False, allow_unicode=True)
    return Response(yaml_s.getvalue(), media_type='text/yaml')


api.include_router(hero.router, prefix='/hero', tags=['hero'])
api.include_router(meta.router, prefix='/meta', tags=['meta'])
