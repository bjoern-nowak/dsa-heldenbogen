from __future__ import annotations  # required till PEP 563

from clingo import Symbol
from clingo import SymbolType

from dsaheldenbogen.app.models.base_enum import BaseEnum
from dsaheldenbogen.app.models.feature import Feature


# TODO may add information about parameters
class RulebookFunction(str, BaseEnum):
    """Collection of some explicitly used LP function names"""

    # meta
    RULEBOOK = 'rulebook'
    RULEBOOK_MISSING = 'rulebook_missing'
    EXTRA_HERO_VALIDATION_STEP = 'extra_hero_validation_step'
    # hero facts
    ADVANTAGE = 'advantage'
    DISADVANTAGE = 'disadvantage'

    @staticmethod
    def is_dis_advantage(sym: Symbol) -> bool:
        return sym.type == SymbolType.Function and sym.name in [RulebookFunction.ADVANTAGE, RulebookFunction.DISADVANTAGE]

    @staticmethod
    def known(feature: Feature) -> str:
        """
        Map heros/characters fields/features to corresponding 'known' facts
        # TODO may should be determined dynamically by given rulebooks
        """
        match feature:
            case Feature.EXPERIENCE_LEVEL:
                return 'known_experience_level'
            case Feature.RACE:
                return 'known_race'
            case Feature.CULTURE:
                return 'known_culture'
            case Feature.PROFESSION:
                return 'known_profession'
            case Feature.ADVANTAGE:
                return 'known_advantage'
            case Feature.DISADVANTAGE:
                return 'known_disadvantage'
            case Feature.TALENT:
                return 'known_talent'
            case Feature.COMBAT_TECHNIQUE:
                return 'known_combat_technique'
            case _:
                raise NotImplementedError(f"Feature '{feature}' has no associated LP 'known' function.")
