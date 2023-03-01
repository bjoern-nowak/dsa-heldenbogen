from __future__ import annotations  # required till PEP 563

from typing import Callable

from clingo import String
from clingo import Symbol

from app.models import Hero


class HeroWrapper(Hero):
    """
    redefine fields to make them callable for clingo
    """
    species: Callable[[], Symbol]
    culture: Callable[[], Symbol]

    @classmethod
    def wrap(cls, held: Hero) -> HeroWrapper:
        return HeroWrapper(
            name=held.name,
            species=lambda: String(held.species),
            culture=lambda: String(held.culture)
        )
