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

    def any_of(self, choices: Symbol, feature: Symbol, options: Symbol, min_lvl: Symbol) -> Symbol:
        """
        can be read as: any <number of choices> <feature> of <selection> has a minimum level of <minimum_level>
        like: any two talents of <talent selection list> has a minimum level of 10
        :return: 1 if count of feature values passing minimum level is at least number of 'choices'
        """
        # dynamically get class field (with 'getattr') instead of manual mapping with a switch-case
        #  this requires feature.name (LP function name) to be exactly the field name of the actual hero model
        values_lvl: dict[str, int] = {fv.name: fv.level for fv in getattr(self._hero, feature.name)}
        # count all features having the minimum level
        passed = sum(1 for opt in options.arguments if min_lvl.number <= values_lvl.get(opt.string, 0))
        # Clingo-Python-API does not support returning booleans
        return Number(1) if passed >= choices.number else Number(0)
