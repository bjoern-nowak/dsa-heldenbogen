from typing import List

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from .v1.api import api as api_v1

app = FastAPI()


@app.get("/")
def index():
    return RedirectResponse(url='/docs')


@app.get("/apis")
def index() -> List[str]:
    """List all available apis"""
    return ["/api/v1"]


app.mount("/api/v1", api_v1)
