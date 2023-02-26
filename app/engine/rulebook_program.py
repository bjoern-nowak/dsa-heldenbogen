from __future__ import annotations  # required till PEP 563

from app.models.feature import Feature


class RulebookProgram():

    @classmethod
    def list(cls, merkmal: Feature) -> str:
        match merkmal:
            case Feature.Spezies:
                return "list_spezies"
            case Feature.Kultur:
                return "list_kulturen"
            case _:
                raise NotImplementedError(f"Das Feature '{merkmal}' ist der Engine nicht bekannt.")
