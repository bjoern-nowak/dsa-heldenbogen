from __future__ import annotations  # required till PEP 563

from app.models.feature import Feature


class RulebookProgram():
    # main programs
    USABLE = "usable"

    # list programs
    LIST_SPEZIES = "list_spezies"
    LIST_CULTURES = "list_kulturen"

    @staticmethod
    def list(merkmal: Feature) -> str:
        match merkmal:
            case Feature.Spezies:
                return RulebookProgram.LIST_SPEZIES
            case Feature.Kultur:
                return RulebookProgram.LIST_CULTURES
            case _:
                raise NotImplementedError(f"Das Feature '{merkmal}' ist der Engine nicht bekannt.")
