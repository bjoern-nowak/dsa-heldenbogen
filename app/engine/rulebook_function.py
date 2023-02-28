from __future__ import annotations  # required till PEP 563

from enum import Enum

from app.models.feature import Feature


class RulebookFunction(str, Enum):
    RULEBOOK_UNUSABLE = 'rulebook_unusable'
    SPEZIES = 'spezies'
    CULTURE = 'kultur'

    @staticmethod
    def of(feature: Feature) -> str:
        match feature:
            case Feature.Spezies:
                return RulebookFunction.SPEZIES
            case Feature.Kultur:
                return RulebookFunction.CULTURE
            case _:
                raise NotImplementedError(f"Feature '{feature}' has no associated LP function.")
