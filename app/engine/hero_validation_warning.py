from __future__ import annotations  # required till PEP 563

from clingo import Symbol

from app.engine.rulebook_function import RulebookFunction
from app.models import BaseModel
from app.models.base_enum import BaseEnum


class HeroValidationWarningType(str, BaseEnum):
    MISSING_USUAL = 'missing_usual'
    MISSING_TYPICAL = 'missing_typical'


class HeroValidationWarning(BaseModel):
    """
    Represents a single hero validation warning.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """
    type: HeroValidationWarningType
    # TODO may add addon field for (dis)advantages for clarification
    message: str
    parameter: dict[str, str]

    @staticmethod
    def from_(warning: Symbol) -> HeroValidationWarning:
        caused_feature = warning.arguments[0]
        caused_feature_value = caused_feature.arguments[0].string
        referred_feature = warning.arguments[1]
        referred_feature_value = referred_feature.arguments[0].string
        match warning.name:
            case HeroValidationWarningType.MISSING_TYPICAL:
                if RulebookFunction.is_dis_advantage(referred_feature):
                    referred_feature_using = referred_feature.arguments[1].string
                    referred_feature_level = referred_feature.arguments[2].number
                    # TODO only add 'referred_feature_using' to message and parameter when not empty
                    return HeroValidationWarning(
                        type=HeroValidationWarningType.MISSING_TYPICAL,
                        message=f"Heros '{caused_feature.name}' is missing typical '{referred_feature.name}'"
                                f" of '{referred_feature_value}'"
                                f" using '{referred_feature_using}'"
                                f" at level '{referred_feature_level}'.",
                        parameter={
                            'caused_feature': caused_feature.name,
                            'caused_feature_value': caused_feature_value,
                            'referred_feature': referred_feature.name,
                            'referred_feature_value': referred_feature_value,
                            'referred_feature_level': referred_feature_level,
                            'referred_feature_using': referred_feature_using,
                        },
                    )
                else:
                    # TODO handle referred features having a level
                    return HeroValidationWarning(
                        type=HeroValidationWarningType.MISSING_TYPICAL,
                        message=f"Heros '{caused_feature.name}' is missing typical '{referred_feature.name}'"
                                f" of '{referred_feature_value}'.",
                        parameter={
                            'caused_feature': caused_feature.name,
                            'caused_feature_value': caused_feature_value,
                            'referred_feature': referred_feature.name,
                            'referred_feature_value': referred_feature_value,
                        },
                    )
            case HeroValidationWarningType.MISSING_USUAL:
                return HeroValidationWarning(
                    type=HeroValidationWarningType.MISSING_USUAL,
                    message=f"Heros '{caused_feature.name}' is missing usual '{referred_feature.name}'"
                            f" of '{referred_feature_value}'.",
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
