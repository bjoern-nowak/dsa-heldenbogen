from __future__ import annotations  # required till PEP 563

from app.models import Feature
from app.models.base_enum import BaseEnum


# TODO add information about parameters
class RulebookFunction(str, BaseEnum):
    # meta
    RULEBOOK_UNUSABLE = 'rulebook_unusable'
    EXTRA_HERO_VALIDATION_STEP = 'extra_hero_validation_step'

    @staticmethod
    def known(feature: Feature) -> str:
        match feature:
            case Feature.SPECIES:
                return 'known_species'
            case Feature.CULTURE:
                return 'known_culture'
            case Feature.PROFESSION:
                return 'known_profession'
            case Feature.ADVANTAGE:
                return 'known_advantage'
            case Feature.DISADVANTAGE:
                return 'known_disadvantage'
            case Feature.SKILL:
                return 'known_skill'
            case _:
                raise NotImplementedError(f"Feature '{feature}' has no associated LP 'known' function.")
