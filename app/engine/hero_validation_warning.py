from __future__ import annotations  # required till PEP 563

from clingo import Symbol

from app.models import BaseModel
from app.models.base_enum import BaseEnum


class HeroValidationWarningType(str, BaseEnum):
    pass


class HeroValidationWarning(BaseModel):
    """
    Represents a single hero validation warning.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """
    type: HeroValidationWarningType
    message: str
    parameter: dict[str, str]

    @staticmethod
    def from_(warning: Symbol) -> HeroValidationWarning:
        feature = warning.arguments[0]
        match warning.name:
            case _:
                raise NotImplementedError(f"Found hero validation warning without parsing definition.\n"
                                          f"Warning name: {warning.name}\n"
                                          f"Warning parameters: {[str(a) for a in warning.arguments]}.")

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
