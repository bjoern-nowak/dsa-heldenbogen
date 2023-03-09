from typing import List

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .api import api

app = FastAPI()


@app.get('/')
def index():
    return RedirectResponse(url='/docs')


@app.get('/apis')
def index() -> List[str]:
    """List all available apis"""
    return ['/api']


app.mount('/api', api)
