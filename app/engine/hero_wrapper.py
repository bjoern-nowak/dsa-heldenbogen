from __future__ import annotations  # required till PEP 563

from typing import Callable

from clingo import String
from clingo import Symbol

from app.models import Hero


# TODO may provide a method which returns a list of literals instead of using a extra LP asking each feature
class HeroWrapper(Hero):
    """
    redefine fields to make them callable for clingo
    """
    species: Callable[[], Symbol]
    culture: Callable[[], Symbol]
    profession: Callable[[], Symbol]

    @classmethod
    def wrap(cls, held: Hero) -> HeroWrapper:
        return HeroWrapper(
            name=held.name,
            species=lambda: String(held.species),
            culture=lambda: String(held.culture),
            profession=lambda: String(held.profession),
        )
