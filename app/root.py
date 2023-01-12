from fastapi import FastAPI

from app.api import v1_router

app = FastAPI()


@app.get("/")
def index() -> str:
    return "Current API is under /api/v1, see /docs"


app.include_router(v1_router, prefix="/api/v1")
