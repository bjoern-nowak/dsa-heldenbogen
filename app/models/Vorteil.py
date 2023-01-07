from pydantic import BaseModel


class Vorteil(BaseModel):
    id: int
    name: str
