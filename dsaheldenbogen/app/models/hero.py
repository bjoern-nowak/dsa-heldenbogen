from typing import List

from dsaheldenbogen.app.models.base_model import BaseModel
from dsaheldenbogen.app.models.dis_advantage import DisAdvantage
from dsaheldenbogen.app.models.skill import Skill


class Hero(BaseModel):
    """Represents an actual hero/character"""
    name: str
    experience_level: str

    race: str
    culture: str

    profession: str
    talents: List[Skill]
    combat_techniques: List[Skill]
    advantages: List[DisAdvantage]
    disadvantages: List[DisAdvantage]
