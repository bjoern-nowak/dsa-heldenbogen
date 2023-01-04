from fastapi import FastAPI

import openapi_util

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/{name}")
def greeting(name: str):
    return {"Hello": name}


openapi_util.use_route_names_as_operation_ids(app)
