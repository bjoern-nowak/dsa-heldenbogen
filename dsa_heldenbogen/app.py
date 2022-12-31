from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/{name}")
def greeting(name: str):
    return {"Hello": name}
