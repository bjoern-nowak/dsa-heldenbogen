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

    def any_of_has_minimum_level(self, choices: Symbol, feature: Symbol, selection: Symbol, minimum_level: Symbol) -> Symbol:
        """
        can be read as: any <number of choices> <feature> of <selection> has a minimum level of <minimum_level>
        like: any two talents of <talent selection list> has a minimum level of 10
        """
        feature_elements: dict[str, int]
        match feature.name:
            case 'talent':
                feature_elements = self.__hero.talents
            case 'combat_technique':
                feature_elements = self.__hero.combat_techniques
            case _:
                raise RuntimeError(f"HeroWrappers 'any_has_minimum_level' method called with an unsupported feature '{feature.name}'.")

        passed = 0
        for option in selection.arguments:
            if option.string in feature_elements and minimum_level.number <= feature_elements[option.string]:
                passed += 1

        # TODO find out how to return a boolean to clingo
        return Number(1) if passed >= choices.number else Number(0)
