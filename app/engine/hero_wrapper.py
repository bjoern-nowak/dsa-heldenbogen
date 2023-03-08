from __future__ import annotations  # required till PEP 563

from typing import List
from typing import Tuple

from clingo import Number
from clingo import String
from clingo import Symbol
from clingo import Tuple_
from pydantic import NonNegativeInt

from app.models import Hero


def _map_feature_with_level(d: dict[str, NonNegativeInt]) -> List[Symbol]:
    return [Tuple_([String(key), Number(d[key])]) for key in d]


def _map_feature_with_level_and_using(d: dict[str, Tuple[NonNegativeInt, str]]) -> List[Symbol]:
    """
    :return: list of three-element tuples of '(<feature>,<level>,<feature_using>)'
    """
    return [Tuple_([String(key), Number(d[key][0]), String(d[key][1])]) for key in d]


# TODO may provide a method which returns a list of literals instead of using a extra LP asking each feature
class HeroWrapper():
    """
    provide callables returning hero attributes as clingo symbols
    """
    _hero: Hero

    def __init__(self, hero: Hero) -> None:
        super().__init__()
        self._hero = hero

    def species(self) -> Symbol:
        return String(self._hero.species)

    def culture(self) -> Symbol:
        return String(self._hero.culture)

    def profession(self) -> Symbol:
        return String(self._hero.profession)

    def talents(self) -> List[Symbol]:
        return _map_feature_with_level(self._hero.talents)

    def combat_techniques(self) -> List[Symbol]:
        return _map_feature_with_level(self._hero.combat_techniques)

    def advantages(self) -> List[Symbol]:
        return _map_feature_with_level_and_using(self._hero.advantages)

    def disadvantages(self) -> List[Symbol]:
        return _map_feature_with_level_and_using(self._hero.disadvantages)

    def any_of_has_minimum_level(self, choices: Symbol, feature: Symbol, selection: Symbol, minimum_level: Symbol) -> Symbol:
        """
        can be read as: any <number of choices> <feature> of <selection> has a minimum level of <minimum_level>
        like: any two talents of <talent selection list> has a minimum level of 10
        """
        feature_elements: dict[str, int]
        match feature.name:
            case 'talent':
                feature_elements = self._hero.talents
            case 'combat_technique':
                feature_elements = self._hero.combat_techniques
            case _:
                raise RuntimeError(f"HeroWrappers 'any_has_minimum_level' method called with an unsupported feature '{feature.name}'.")

        passed = 0
        for option in selection.arguments:
            if option.string in feature_elements and minimum_level.number <= feature_elements[option.string]:
                passed += 1

        # TODO find out how to return a boolean to clingo
        return Number(1) if passed >= choices.number else Number(0)
