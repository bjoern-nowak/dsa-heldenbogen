from __future__ import annotations  # required till PEP 563

from enum import Enum

from app.models import Feature


class RulebookFunction(str, Enum):
    # meta
    RULEBOOK_UNUSABLE = 'rulebook_unusable'

    # known
    KNOWN_SPECIES = 'known_species'
    KNOWN_CULTURE = 'known_culture'
    KNOWN_PROFESSION = "known_profession"
    KNOWN_ADVANTAGE = "known_advantage"
    KNOWN_DISADVANTAGE = "known_disadvantage"
    KNOWN_SKILL = "known_skill"

    # validate errors
    UNKNOWN_SUFFIX = "_unknown"
    UNUSABLE_SUFFIX = "_unusable"
    SPECIES_UNKNOWN = "species_unknown"
    CULTURE_UNKNOWN = "culture_unknown"
    CULTURE_UNUSABLE = "culture_unusable"

    @staticmethod
    def known(feature: Feature) -> RulebookFunction:
        match feature:
            case Feature.SPECIES:
                return RulebookFunction.KNOWN_SPECIES
            case Feature.CULTURE:
                return RulebookFunction.KNOWN_CULTURE
            case Feature.PROFESSION:
                return RulebookFunction.KNOWN_PROFESSION
            case Feature.ADVANTAGE:
                return RulebookFunction.KNOWN_ADVANTAGE
            case Feature.DISADVANTAGE:
                return RulebookFunction.KNOWN_DISADVANTAGE
            case Feature.SKILL:
                return RulebookFunction.KNOWN_SKILL
            case _:
                raise NotImplementedError(f"Feature '{feature}' has no associated LP 'known' function.")
