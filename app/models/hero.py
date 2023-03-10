from typing import List

from app.models.base_model import BaseModel
from app.models.dis_advantage import DisAdvantage
from app.models.experience_level import ExperienceLevel
from app.models.skill import Skill


class Hero(BaseModel):
    name: str
    experience_level: ExperienceLevel

    species: str
    culture: str

    profession: str
    talents: List[Skill]
    combat_techniques: List[Skill]
    advantages: List[DisAdvantage]
    disadvantages: List[DisAdvantage]
