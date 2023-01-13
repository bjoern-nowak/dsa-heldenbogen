from fastapi import FastAPI

from app.api.v1.endpoints import held
from app.api.v1.endpoints import root

api = FastAPI()
api.include_router(root.router, tags=["root"])
api.include_router(held.router, prefix="/held", tags=["held"])
