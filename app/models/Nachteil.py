from pydantic import BaseModel


class Nachteil(BaseModel):
    id: int
    name: str
