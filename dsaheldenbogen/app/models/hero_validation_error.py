from typing import Any
from typing import Optional

from dsaheldenbogen.app.models.base_enum import BaseEnum
from dsaheldenbogen.app.models.base_model import BaseModel
from dsaheldenbogen.app.models.hero_validation_param import HeroValidationParam


class HeroValidationError(BaseModel):
    """
    Represents a single hero validation error.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """

    class Type(str, BaseEnum):
        UNKNOWN = 'unknown'
        UNUSABLE_BY = 'unusable_by'
        MISSING = 'missing'
        MISSING_LEVEL = 'missing_level'
        MAX_LVL_EXCEEDED = 'max_lvl_exceeded'
        MAX_COUNT_EXCEEDED = 'max_count_exceeded'
        MISSING_MIN_LVL = 'missing_min_lvl'

    class Addon(str, BaseEnum):
        """Represents special cases, so that 'type' must be handled differently"""
        ANY_OF = 'any_of'

    type: Type
    addon: Optional[Addon]
    message: str
    parameter: dict[HeroValidationParam, Any]

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
