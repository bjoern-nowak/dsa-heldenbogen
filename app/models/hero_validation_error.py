from __future__ import annotations  # required till PEP 563

from typing import Optional

from app.models.base_enum import BaseEnum
from app.models.base_model import BaseModel


class HeroValidationError(BaseModel):
    """
    Represents a single hero validation error.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """
    type: Type
    addon: Optional[Addon]
    message: str
    parameter: dict[str, str]

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message

    class Type(str, BaseEnum):
        UNKNOWN = 'unknown'
        UNUSABLE_BY = 'unusable_by'
        MISSING_LEVEL = 'missing_level'

    class Addon(str, BaseEnum):
        ANY_OF = 'any_of'
