from typing import List

from pydantic import NonNegativeInt

from .basemodel import BaseModel


# TODO use classes instead of simple dict to provide semantics to key and value
class Hero(BaseModel):
    name: str

    species: str
    culture: str

    profession: str
    # characteristics: dict[Characteristic, NonNegativeInt]
    talents: dict[str, NonNegativeInt]
    combat_techniques: dict[str, NonNegativeInt]
    advantages: List[tuple[str, str, NonNegativeInt]]  # tuples second entry must be set but can be empty
    disadvantages: List[tuple[str, str, NonNegativeInt]]  # tuples second entry must be set but can be empty
