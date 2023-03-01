from __future__ import annotations  # required till PEP 563

from enum import Enum

from app.models.feature import Feature


class RulebookFunction(str, Enum):
    # meta
    RULEBOOK_UNUSABLE = 'rulebook_unusable'

    # base
    SPECIES = 'species'
    CULTURE = 'culture'
    PROFESSION = "profession"
    ADVANTAGE = "advantage"
    DISADVANTAGE = "disadvantage"
    SKILL = "skill"

    @staticmethod
    def of(feature: Feature) -> RulebookFunction:
        match feature:
            case Feature.SPECIES:
                return RulebookFunction.SPECIES
            case Feature.CULTURE:
                return RulebookFunction.CULTURE
            case Feature.PROFESSION:
                return RulebookFunction.PROFESSION
            case Feature.ADVANTAGE:
                return RulebookFunction.ADVANTAGE
            case Feature.DISADVANTAGE:
                return RulebookFunction.DISADVANTAGE
            case Feature.SKILL:
                return RulebookFunction.SKILL
            case _:
                raise NotImplementedError(f"Feature '{feature}' has no associated LP function.")
