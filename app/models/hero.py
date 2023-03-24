from typing import List

from app.models.base_model import BaseModel
from app.models.dis_advantage import DisAdvantage
from app.models.skill import Skill


class Hero(BaseModel):
    """Represents an actual hero/character"""
    name: str
    experience_level: str

    species: str
    culture: str

    profession: str
    talents: List[Skill]
    combat_techniques: List[Skill]
    advantages: List[DisAdvantage]
    disadvantages: List[DisAdvantage]
