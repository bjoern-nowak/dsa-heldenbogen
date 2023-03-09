from __future__ import annotations  # required till PEP 563

from typing import Optional

from clingo import Symbol
from clingo import SymbolType

from app.engine.rulebook_function import RulebookFunction
from app.models import BaseModel
from app.models.base_enum import BaseEnum


class HeroValidationErrorType(str, BaseEnum):
    UNKNOWN = 'unknown'
    UNUSABLE_BY = 'unusable_by'
    MISSING_LEVEL = 'missing_level'


class HeroValidationErrorAddon(str, BaseEnum):
    # TODO may add (dis)advantages as addon for clarification
    ANY_OF = 'any_of'

    def matches(self, symbol: Symbol) -> bool:
        return symbol.type == SymbolType.Function and symbol.name == self.value


class HeroValidationError(BaseModel):
    """
    Represents a single hero validation error.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """
    type: HeroValidationErrorType
    addon: Optional[HeroValidationErrorAddon]
    message: str
    parameter: dict[str, str]

    # TODO reduce step count but also implement an error filtering to root causes
    @staticmethod
    def from_(error: Symbol) -> HeroValidationError:
        caused_feature = error.arguments[0]
        caused_feature_value = caused_feature.arguments[0].string
        match error.name:
            case HeroValidationErrorType.UNKNOWN:
                if RulebookFunction.is_dis_advantage(caused_feature):
                    caused_feature_level = caused_feature.arguments[1].number
                    caused_feature_using = caused_feature.arguments[2].string
                    return HeroValidationError(
                        type=HeroValidationErrorType.UNKNOWN,
                        message=f"Heros '{caused_feature.name}' value of '{caused_feature_value}'"
                                f" at level '{caused_feature_level}' using '{caused_feature_using}' is not known.",
                        parameter={
                            'caused_feature': caused_feature.name,
                            'caused_feature_value': caused_feature_value,
                            'caused_feature_level': caused_feature_level,
                            'caused_feature_using': caused_feature_using,
                        },
                    )
                else:
                    return HeroValidationError(
                        type=HeroValidationErrorType.UNKNOWN,
                        message=f"Heros '{caused_feature.name}' value of '{caused_feature_value}' is not known.",
                        parameter={
                            'caused_feature': caused_feature.name,
                            'caused_feature_value': caused_feature_value,
                        },
                    )
            case HeroValidationErrorType.UNUSABLE_BY:
                referred_feature = error.arguments[1]
                referred_feature_value = referred_feature.arguments[0].string
                return HeroValidationError(
                    type=HeroValidationErrorType.UNUSABLE_BY,
                    message=f"Heros '{caused_feature.name}' is unusable for heros '{referred_feature.name}'.",
                    parameter={
                        'caused_feature': caused_feature.name,
                        'caused_feature_value': caused_feature_value,
                        'referred_feature': referred_feature.name,
                        'referred_feature_value': referred_feature_value,
                    },
                )
            case HeroValidationErrorType.MISSING_LEVEL:
                referred_feature = error.arguments[1]
                referred_feature_sym = referred_feature.arguments[0]
                required_level = referred_feature.arguments[1]
                if HeroValidationErrorAddon.ANY_OF.matches(referred_feature_sym):
                    # referred_feature_sym is the addon
                    choices = referred_feature_sym.arguments[0]
                    selection = [a.string for a in referred_feature_sym.arguments[1].arguments]
                    return HeroValidationError(
                        type=HeroValidationErrorType.MISSING_LEVEL,
                        addon=HeroValidationErrorAddon.ANY_OF,
                        message=f"Heros '{caused_feature.name}' is missing minimum level '{required_level}'"
                                f" for '{choices}' '{referred_feature.name}'"
                                f" of '{selection}'.",
                        parameter={
                            'caused_feature': caused_feature.name,
                            'caused_feature_value': caused_feature_value,
                            'referred_feature': referred_feature.name,
                            'referred_feature_value_selection': str(selection),
                            'referred_feature_value_minimum_level': required_level.number,
                            'referred_feature_value_selection_minium_choices': choices.number,
                        },
                    )
                else:
                    # referred_feature_sym is the actual referred feature value (String)
                    return HeroValidationError(
                        type=HeroValidationErrorType.MISSING_LEVEL,
                        message=f"Heros '{caused_feature.name}' is missing minimum level '{required_level}'"
                                f" for '{referred_feature.name}'"
                                f" of '{referred_feature_sym.string}'.",
                        parameter={
                            'caused_feature': caused_feature.name,
                            'caused_feature_value': caused_feature_value,
                            'referred_feature': referred_feature.name,
                            'referred_feature_value': referred_feature_sym.string,
                            'referred_feature_value_minimum_level': required_level.number,
                        },
                    )
            case _:
                raise NotImplementedError(f"Found hero validation error without parsing definition.\n"
                                          f"Error name: {error.name}\n"
                                          f"Error parameters: {[str(a) for a in error.arguments]}.")

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
