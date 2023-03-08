from __future__ import annotations  # required till PEP 563

from typing import List
from typing import Optional

from clingo import Symbol

from app.models import BaseModel
from app.models.base_enum import BaseEnum


class HeroValidationErrorType(str, BaseEnum):
    UNKNOWN = 'unknown'
    UNUSABLE_BY = 'unusable_by'
    MISSING_LEVEL = 'missing_level'


class HeroValidationErrorAddon(str, BaseEnum):
    ANY_OF = 'any_of'


class HeroValidationError(BaseModel):
    """
    Represents a single hero validation error.

    Field 'type' is only 'None' on an unspecified error
    Optional field 'addon' is an addon to field 'type',
    Field 'message' should single quote used 'parameters'
    Field 'parameters' should reflect order of usage in 'message'.
    """
    type: HeroValidationErrorType | None
    addon: Optional[HeroValidationErrorAddon]
    message: str
    parameter: List[str]

    # TODO reduce step count but also implement an error filtering to root causes
    @staticmethod
    def from_(error: Symbol) -> HeroValidationError:
        feature = error.arguments[0]
        match error.name:
            case HeroValidationErrorType.UNKNOWN:
                return HeroValidationError(
                    type=HeroValidationErrorType.UNKNOWN,
                    message=f"Heros '{feature.name}' value of '{feature.arguments[0].string}' is not known.",
                    parameter=[feature.name, feature.arguments[0].string],
                )
            case HeroValidationErrorType.UNUSABLE_BY:
                return HeroValidationError(
                    type=HeroValidationErrorType.UNUSABLE_BY,
                    message=f"Heros '{feature.name}' is unusable for heros '{error.arguments[1].name}'.",
                    parameter=[feature.name, error.arguments[1].name],
                )
            case HeroValidationErrorType.MISSING_LEVEL:
                required_feature_type = error.arguments[1]
                required_feature = required_feature_type.arguments[0]
                required_level = required_feature_type.arguments[1]
                if required_feature.name == HeroValidationErrorAddon.ANY_OF:
                    # hence it is a function (or constant), not an actual feature (String)
                    choices = required_feature.arguments[0]
                    selection = [a.string for a in required_feature.arguments[1].arguments]
                    return HeroValidationError(
                        type=HeroValidationErrorType.MISSING_LEVEL,
                        addon=HeroValidationErrorAddon.ANY_OF,
                        message=f"Heros '{feature.name}' is missing minimum level '{required_level}' for '{choices}' '{required_feature_type.name}' of '{selection}'.",
                        parameter=[feature.name, required_level.number, choices.number, required_feature_type.name,
                                   str(selection)],
                    )
                else:
                    return HeroValidationError(
                        type=HeroValidationErrorType.MISSING_LEVEL,
                        message=f"Heros '{feature.name}' is missing minimum level '{required_level}' for '{required_feature_type.name}' of '{required_feature.string}'.",
                        parameter=[feature.name, required_level.number, required_feature_type.name, required_feature.string],
                    )
            case _:
                return HeroValidationError(
                    message=f"Unspecified error '{error.name}' with parameters '{error.arguments}'.",
                    type=None,
                    parameter=[error.name, error.arguments],
                )

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
