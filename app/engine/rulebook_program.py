from __future__ import annotations  # required till PEP 563

from app.models.feature import Feature


class RulebookProgram():
    # meta
    USABLE = "usable"

    # meta: list programs
    LIST_SPEZIES = "list_spezies"
    LIST_CULTURES = "list_kulturen"
    LIST_PROFESSION = "list_profession"
    LIST_VORTEIL = "list_vorteil"
    LIST_NACHTEIL = "list_nachteil"
    LIST_FERTIGKEIT = "list_fertigkeit"

    @staticmethod
    def list(feature: Feature) -> str:
        match feature:
            case Feature.SPEZIES:
                return RulebookProgram.LIST_SPEZIES
            case Feature.CULTURE:
                return RulebookProgram.LIST_CULTURES
            case Feature.PROFESSION:
                return RulebookProgram.LIST_PROFESSION
            case Feature.VORTEIL:
                return RulebookProgram.LIST_VORTEIL
            case Feature.NACHTEIL:
                return RulebookProgram.LIST_NACHTEIL
            case Feature.FERTIGKEIT:
                return RulebookProgram.LIST_FERTIGKEIT
            case _:
                raise NotImplementedError(f"There is no 'list program' for feature '{feature}'.")
