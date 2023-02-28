from __future__ import annotations  # required till PEP 563

from enum import Enum

from app.models.feature import Feature


class RulebookFunction(str, Enum):
    # meta
    RULEBOOK_UNUSABLE = 'rulebook_unusable'

    # base
    SPEZIES = 'spezies'
    CULTURE = 'kultur'
    PROFESSION = "profession"
    VORTEIL = "vorteil"
    NACHTEIL = "nachteil"
    FERTIGKEIT = "fertigkeit"

    @staticmethod
    def of(feature: Feature) -> str:
        match feature:
            case Feature.SPEZIES:
                return RulebookFunction.SPEZIES
            case Feature.CULTURE:
                return RulebookFunction.CULTURE
            case Feature.PROFESSION:
                return RulebookFunction.PROFESSION
            case Feature.VORTEIL:
                return RulebookFunction.VORTEIL
            case Feature.NACHTEIL:
                return RulebookFunction.NACHTEIL
            case Feature.FERTIGKEIT:
                return RulebookFunction.FERTIGKEIT
            case _:
                raise NotImplementedError(f"Feature '{feature}' has no associated LP function.")
