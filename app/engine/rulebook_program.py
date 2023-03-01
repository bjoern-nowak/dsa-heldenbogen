from __future__ import annotations  # required till PEP 563

from enum import Enum

from app.models.feature import Feature


class RulebookProgram(str, Enum):
    # meta
    IS_USABLE = "is_usable"

    # meta: list programs
    LIST_SPEZIES = "list_species"
    LIST_CULTURES = "list_cultures"
    LIST_PROFESSIONS = "list_professions"
    LIST_ADVANTAGES = "list_advantages"
    LIST_DISADVANTAGES = "list_disadvantages"
    LIST_SKILLS = "list_skills"

    @staticmethod
    def list(feature: Feature) -> RulebookProgram:
        match feature:
            case Feature.SPECIES:
                return RulebookProgram.LIST_SPEZIES
            case Feature.CULTURE:
                return RulebookProgram.LIST_CULTURES
            case Feature.PROFESSION:
                return RulebookProgram.LIST_PROFESSIONS
            case Feature.ADVANTAGE:
                return RulebookProgram.LIST_ADVANTAGES
            case Feature.DISADVANTAGE:
                return RulebookProgram.LIST_DISADVANTAGES
            case Feature.SKILL:
                return RulebookProgram.LIST_SKILLS
            case _:
                raise NotImplementedError(f"There is no 'list program' for feature '{feature}'.")
