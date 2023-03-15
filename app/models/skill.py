from __future__ import annotations  # required till PEP 563

from typing import List

from app.models.base_model import BaseModel


class Skill(BaseModel):
    name: str
    level: int

    @staticmethod
    def list_by(skills: List[tuple[str, int]]) -> List[Skill]:
        return [Skill(name=s[0], level=s[1]) for s in skills]
