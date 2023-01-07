from pydantic import BaseModel


class Fertigkeit(BaseModel):
    id: int
    name: str
