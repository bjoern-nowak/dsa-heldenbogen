from pydantic import NonNegativeInt

from .basemodel import BaseModel


class Hero(BaseModel):
    name: str

    species: str
    culture: str

    profession: str
    # characteristics: dict[Characteristic, NonNegativeInt]
    talents: dict[str, NonNegativeInt]
    # advantages: List[str]
    # disadvantages: List[str]
