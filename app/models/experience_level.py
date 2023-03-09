from enum import Enum

from pydantic import NonNegativeInt

from app.models.base_model import BaseModel


class ExperienceLevelType(BaseModel):
    NAME: str
    MAX_CHARACTERISTIC_LEVEL: NonNegativeInt
    MAX_SKILL_LEVEL: NonNegativeInt
    MAX_COMBAT_TECHNIQUE_LEVEL: NonNegativeInt
    MAX_CHARACTERISTIC_POINTS: NonNegativeInt
    MAX_SPELLS_AND_LITURGIES: NonNegativeInt
    MAX_FOREIGN_SPELL: NonNegativeInt


# TODO to be used
class ExperienceLevel(ExperienceLevelType, Enum):
    INEXPERIENCED = 'Inexperienced', 12, 10, 8, 95, 8, 0
    AVERAGE = 'Average', 13, 10, 10, 98, 10, 1
    EXPERIENCED = 'Experienced', 14, 10, 12, 100, 12, 2
    COMPETENT = 'Competent', 15, 13, 14, 102, 14, 3
    MASTERFUL = 'Masterful', 16, 16, 16, 105, 16, 4
    BRILLIANT = 'Brilliant', 17, 19, 18, 109, 18, 5
    LEGENDARY = 'Legendary', 18, 20, 20, 114, 20, 6
