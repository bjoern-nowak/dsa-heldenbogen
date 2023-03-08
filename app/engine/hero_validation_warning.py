from __future__ import annotations  # required till PEP 563

from clingo import Symbol

from app.models import BaseModel
from app.models.base_enum import BaseEnum


class HeroValidationWarningType(str, BaseEnum):
    UNUSUAL_FOR = 'unusual_for'


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
        caused_feature = warning.arguments[0]
        caused_feature_value = caused_feature.arguments[0].string
        referred_feature = warning.arguments[1]
        referred_feature_value = referred_feature.arguments[0].string
        match warning.name:
            case HeroValidationWarningType.UNUSUAL_FOR:
                return HeroValidationWarning(
                    type=HeroValidationWarningType.UNUSUAL_FOR,
                    message=f"Heros '{caused_feature.name}' is unusual for heros '{referred_feature.name}'.",
                    parameter={
                        'caused_feature': caused_feature.name,
                        'caused_feature_value': caused_feature_value,
                        'referred_feature': referred_feature.name,
                        'referred_feature_value': referred_feature_value,
                    },
                )
            case _:
                raise NotImplementedError(f"Found hero validation warning without parsing definition.\n"
                                          f"Warning name: {warning.name}\n"
                                          f"Warning parameters: {[str(a) for a in warning.arguments]}.")

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
