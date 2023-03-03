from __future__ import annotations  # required till PEP 563

from typing import Callable

from clingo import String

from app.models import BaseModel
from app.models import Hero


# TODO may provide a method which returns a list of literals instead of using a extra LP asking each feature
class HeroWrapper(BaseModel):
    """
    provide callables returning hero attributes as clingo symbols
    """
    hero_species: Callable[[], String]
    hero_culture: Callable[[], String]
    hero_profession: Callable[[], String]

    @classmethod
    def wrap(cls, hero: Hero) -> HeroWrapper:
        return HeroWrapper(
            hero_species=lambda: String(hero.species),
            hero_culture=lambda: String(hero.culture),
            hero_profession=lambda: String(hero.profession),
        )
