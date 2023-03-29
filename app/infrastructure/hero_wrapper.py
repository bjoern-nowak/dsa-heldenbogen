from __future__ import annotations  # required till PEP 563

from typing import List

from clingo import Number
from clingo import String
from clingo import Symbol
from clingo import Tuple_

from app.models.dis_advantage import DisAdvantage
from app.models.hero import Hero
from app.models.skill import Skill


def _map_skills(skills: List[Skill]) -> List[Symbol]:
    return [Tuple_([String(skill.name), Number(skill.level)]) for skill in skills]


def _map_dis_advantages(dis_advantages: List[DisAdvantage]) -> List[Symbol]:
    return [Tuple_([String(d_a.name), String(d_a.uses), Number(d_a.level)]) for d_a in dis_advantages]


# TODO may provide a method which returns a list of literals instead of using a extra LP asking each feature
class HeroWrapper:
    """
    provide callables returning hero attributes as clingo symbols
    """
    _hero: Hero

    def __init__(self, hero: Hero) -> None:
        super().__init__()
        self._hero = hero

    def experience_level(self) -> Symbol:
        return String(self._hero.experience_level)

    def race(self) -> Symbol:
        return String(self._hero.race)

    def culture(self) -> Symbol:
        return String(self._hero.culture)

    def profession(self) -> Symbol:
        return String(self._hero.profession)

    def talents(self) -> List[Symbol]:
        return _map_skills(self._hero.talents)

    def combat_techniques(self) -> List[Symbol]:
        return _map_skills(self._hero.combat_techniques)

    def advantages(self) -> List[Symbol]:
        return _map_dis_advantages(self._hero.advantages)

    def disadvantages(self) -> List[Symbol]:
        return _map_dis_advantages(self._hero.disadvantages)

    def any_of_has_minimum_level(self, choices: Symbol, feature: Symbol, selection: Symbol, minimum_level: Symbol) -> Symbol:
        """
        can be read as: any <number of choices> <feature> of <selection> has a minimum level of <minimum_level>
        like: any two talents of <talent selection list> has a minimum level of 10
        """
        feature_values_with_level: dict[str, int]
        match feature.name:
            case 'talent':
                feature_values_with_level = {t.name: t.level for t in self._hero.talents}
            case 'combat_technique':
                feature_values_with_level = {ct.name: ct.level for ct in self._hero.combat_techniques}
            case _:
                raise RuntimeError(f"HeroWrappers 'any_has_minimum_level' method called with an unsupported feature '{feature.name}'.")

        passed = 0
        for option in selection.arguments:
            if option.string in feature_values_with_level and minimum_level.number <= feature_values_with_level[option.string]:
                passed += 1

        # TODO find out how to return a boolean to clingo
        return Number(1) if passed >= choices.number else Number(0)
