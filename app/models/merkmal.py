from abc import ABC

from . import BaseModel


class Merkmal(BaseModel, ABC):
    id: str
