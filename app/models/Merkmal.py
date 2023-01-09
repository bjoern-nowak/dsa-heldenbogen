from abc import ABC

from app.models.BaseModel import BaseModel


class Merkmal(BaseModel, ABC):
    id: str
