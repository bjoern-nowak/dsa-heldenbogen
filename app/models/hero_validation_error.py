from typing import Optional

from app.models.base_enum import BaseEnum
from app.models.base_model import BaseModel


class HeroValidationError(BaseModel):
    """
    Represents a single hero validation error.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """

    class Type(str, BaseEnum):
        UNKNOWN = 'unknown'
        UNUSABLE_BY = 'unusable_by'
        MISSING_LEVEL = 'missing_level'
        MAX_LVL_EXCEEDED = 'max_lvl_exceeded'

    class Addon(str, BaseEnum):
        ANY_OF = 'any_of'

    type: Type
    addon: Optional[Addon]
    message: str
    parameter: dict[str, str]

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message