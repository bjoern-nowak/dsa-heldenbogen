from __future__ import annotations  # required till PEP 563

from typing import List

from clingo import Number
from clingo import String
from clingo import Symbol
from clingo import Tuple_

from app.models import Hero


# TODO may provide a method which returns a list of literals instead of using a extra LP asking each feature
class HeroWrapper():
    """
    provide callables returning hero attributes as clingo symbols
    """
    __hero: Hero

    def __init__(self, hero: Hero) -> None:
        super().__init__()
        self.__hero = hero

    def species(self) -> Symbol:
        return String(self.__hero.species)

    def culture(self) -> Symbol:
        return String(self.__hero.culture)

    def profession(self) -> Symbol:
        return String(self.__hero.profession)

    def talents(self) -> List[Symbol]:
        return [Tuple_([String(key), Number(self.__hero.talents[key])]) for key in self.__hero.talents]

    def combat_techniques(self) -> List[Symbol]:
        return [Tuple_([String(key), Number(self.__hero.combat_techniques[key])]) for key in self.__hero.combat_techniques]

    # TODO find out how to return a boolean to clingo
    def one_combat_technique_at_minimum(self, ct_tuple: Symbol, minimum: Symbol) -> Symbol:
        for ct in ct_tuple.arguments:
            if ct.string in self.__hero.combat_techniques and minimum.number <= self.__hero.combat_techniques[ct.string]:
                return Number(1)
        return Number(0)
