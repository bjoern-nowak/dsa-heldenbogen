from __future__ import annotations  # required till PEP 563

from clingo import Symbol
from clingo import SymbolType

from app.engine.rulebook_function import RulebookFunction
from app.models.base_enum import BaseEnum
from app.models.hero_validation_error import HeroValidationError
from app.models.hero_validation_warning import HeroValidationWarning


class ErrorAtom(str, BaseEnum):
    UNKNOWN = 'unknown'
    UNUSABLE_BY = 'unusable_by'
    MISSING_LEVEL = 'missing_level'
    MAX_LVL_EXCEEDED = 'max_lvl_exceeded'


class _ErrorAtomAddon(str, BaseEnum):
    ANY_OF = 'any_of'


class WarningAtom(str, BaseEnum):
    MISSING_USUAL = 'missing_usual'
    MISSING_TYPICAL = 'missing_typical'
    ATYPICAL = 'atypical'


def as_error(error: Symbol) -> HeroValidationError:
    match error.name:
        case ErrorAtom.UNKNOWN:
            return _unknown_error(error)
        case ErrorAtom.UNUSABLE_BY:
            return _unusable_by_error(error)
        case ErrorAtom.MISSING_LEVEL:
            return _missing_level_error(error)
        case ErrorAtom.MAX_LVL_EXCEEDED:
            return _max_level_exceeded_error(error)
        case _:
            raise NotImplementedError(f"Found hero validation error without parsing definition.\n"
                                      f"Error name: {error.name}\n"
                                      f"Error parameters: {[str(a) for a in error.arguments]}.")


def as_warning(warning: Symbol) -> HeroValidationWarning:
    match warning.name:
        case WarningAtom.ATYPICAL:
            return _atypical_warning(warning)
        case WarningAtom.MISSING_TYPICAL:
            return _missing_typical_warning(warning)
        case WarningAtom.MISSING_USUAL:
            return _missing_usual_warning(warning)
        case _:
            raise NotImplementedError(f"Found hero validation warning without parsing definition.\n"
                                      f"Warning name: {warning.name}\n"
                                      f"Warning parameters: {[str(a) for a in warning.arguments]}.")


def _unknown_error(error: Symbol):
    caused_feature = error.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    # TODO may add (dis)advantages as addon for clarification
    if RulebookFunction.is_dis_advantage(caused_feature):
        caused_feature_using = caused_feature.arguments[1].string
        caused_feature_level = caused_feature.arguments[2].number
        return HeroValidationError(
            type=HeroValidationError.Type.UNKNOWN,
            message=f"Heros '{caused_feature.name}' of '{caused_feature_value}' using '{caused_feature_using}'"
                    f" at level '{caused_feature_level}' is not known.",
            parameter={
                'caused_feature': caused_feature.name,
                'caused_feature_value': caused_feature_value,
                'caused_feature_level': caused_feature_level,
                'caused_feature_using': caused_feature_using,
            },
        )
    else:
        return HeroValidationError(
            type=HeroValidationError.Type.UNKNOWN,
            message=f"Heros '{caused_feature.name}' value of '{caused_feature_value}' is not known.",
            parameter={
                'caused_feature': caused_feature.name,
                'caused_feature_value': caused_feature_value,
            },
        )


def _unusable_by_error(error: Symbol):
    caused_feature = error.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    referred_feature = error.arguments[1]
    referred_feature_value = referred_feature.arguments[0].string
    return HeroValidationError(
        type=HeroValidationError.Type.UNUSABLE_BY,
        message=f"Heros '{caused_feature.name}' is unusable for heros '{referred_feature.name}'.",
        parameter={
            'caused_feature': caused_feature.name,
            'caused_feature_value': caused_feature_value,
            'referred_feature': referred_feature.name,
            'referred_feature_value': referred_feature_value,
        },
    )


def _missing_level_error(error: Symbol):
    caused_feature = error.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    referred_feature = error.arguments[1]
    referred_feature_sym = referred_feature.arguments[0]
    required_level = referred_feature.arguments[1]
    if _matches(_ErrorAtomAddon.ANY_OF, referred_feature_sym):
        # referred_feature_sym is the addon
        choices = referred_feature_sym.arguments[0]
        selection = [a.string for a in referred_feature_sym.arguments[1].arguments]
        return HeroValidationError(
            type=HeroValidationError.Type.MISSING_LEVEL,
            addon=HeroValidationError.Addon.ANY_OF,
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
            type=HeroValidationError.Type.MISSING_LEVEL,
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


def _max_level_exceeded_error(error: Symbol):
    caused_feature = error.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    caused_feature_level = caused_feature.arguments[1].number
    max_level = error.arguments[1].number
    return HeroValidationError(
        type=HeroValidationError.Type.MAX_LVL_EXCEEDED,
        message=f"Heros '{caused_feature.name}' of '{caused_feature_value}' exceeds maximum level '{max_level}'.",
        parameter={
            'caused_feature': caused_feature.name,
            'caused_feature_value': caused_feature_value,
            'caused_feature_level': caused_feature_level,
            'max_level': max_level,
        },
    )


def _atypical_warning(warning: Symbol):
    caused_feature = warning.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    referred_feature = warning.arguments[1]
    referred_feature_value = referred_feature.arguments[0].string
    if RulebookFunction.is_dis_advantage(referred_feature):
        referred_feature_using = referred_feature.arguments[1].string
        return HeroValidationWarning(
            type=HeroValidationWarning.Type.ATYPICAL,
            message=f"For heros '{caused_feature.name}' is atypical: '{referred_feature.name}'"
                    f" of '{referred_feature_value}'"
                    f" using '{referred_feature_using}'.",
            parameter={
                'caused_feature': caused_feature.name,
                'caused_feature_value': caused_feature_value,
                'referred_feature': referred_feature.name,
                'referred_feature_value': referred_feature_value,
                'referred_feature_using': referred_feature_using,
            },
        )
    else:
        raise NotImplementedError("Using 'atypical' referring non (dis)advantages is yet to be implemented.")


def _missing_typical_warning(warning: Symbol):
    caused_feature = warning.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    referred_feature = warning.arguments[1]
    referred_feature_value = referred_feature.arguments[0].string
    # TODO may add (dis)advantages as addon (new field; like on error) for clarification
    if RulebookFunction.is_dis_advantage(referred_feature):
        referred_feature_using = referred_feature.arguments[1].string
        referred_feature_level = referred_feature.arguments[2].number
        # TODO only add 'referred_feature_using' to message and parameter when not empty
        return HeroValidationWarning(
            type=HeroValidationWarning.Type.MISSING_TYPICAL,
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
            type=HeroValidationWarning.Type.MISSING_TYPICAL,
            message=f"Heros '{caused_feature.name}' is missing typical '{referred_feature.name}'"
                    f" of '{referred_feature_value}'.",
            parameter={
                'caused_feature': caused_feature.name,
                'caused_feature_value': caused_feature_value,
                'referred_feature': referred_feature.name,
                'referred_feature_value': referred_feature_value,
            },
        )


def _missing_usual_warning(warning: Symbol):
    caused_feature = warning.arguments[0]
    caused_feature_value = caused_feature.arguments[0].string
    referred_feature = warning.arguments[1]
    referred_feature_value = referred_feature.arguments[0].string
    return HeroValidationWarning(
        type=HeroValidationWarning.Type.MISSING_USUAL,
        message=f"Heros '{caused_feature.name}' is missing usual '{referred_feature.name}'"
                f" of '{referred_feature_value}'.",
        parameter={
            'caused_feature': caused_feature.name,
            'caused_feature_value': caused_feature_value,
            'referred_feature': referred_feature.name,
            'referred_feature_value': referred_feature_value,
        },
    )


def _matches(function_name: str, symbol: Symbol) -> bool:
    return symbol.type == SymbolType.Function and symbol.name == function_name
