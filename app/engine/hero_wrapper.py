from __future__ import annotations  # required till PEP 563

from typing import Callable
from typing import List

from clingo import Function
from clingo import Number
from clingo import String
from clingo import Tuple_

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
    hero_talents: Callable[[], List[Function]]
    hero_combat_techniques: Callable[[], List[Function]]

    @classmethod
    def wrap(cls, hero: Hero) -> HeroWrapper:
        return HeroWrapper(
            hero_species=lambda: String(hero.species),
            hero_culture=lambda: String(hero.culture),
            hero_profession=lambda: String(hero.profession),
            hero_talents=lambda: [Tuple_([String(key), Number(hero.talents[key])]) for key in hero.talents],
            hero_combat_techniques=lambda: [Tuple_([String(key), Number(hero.combat_techniques[key])]) for key in
                                            hero.combat_techniques],
        )
