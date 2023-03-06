from clingo import Symbol

from app.models.base_enum import BaseEnum


class HeroValidationError(str, BaseEnum):
    UNKNOWN = 'unknown'
    UNUSABLE_BY = 'unusable_by'
    MISSING_LEVEL = 'missing_level'


class HeroValidationErrorArgument(str, BaseEnum):
    ANY_OF = 'any_of'


class HeroValidationInterpreter:

    # TODO return an error object which also holds an error type and each reason argument, usable in frontend and testcases
    @staticmethod
    def str(error: Symbol) -> str:
        feature = error.arguments[0]
        match error.name:
            case HeroValidationError.UNKNOWN:
                return f"Heros '{feature.name}' value of '{feature.arguments[0].string}' is not known."
            case HeroValidationError.UNUSABLE_BY:
                return f"Heros '{feature.name}' is unusable for heros '{error.arguments[1].name}'."
            case HeroValidationError.MISSING_LEVEL:
                required_feature_type = error.arguments[1]
                required_feature = required_feature_type.arguments[0]
                required_level = required_feature_type.arguments[1]
                if required_feature.name == HeroValidationErrorArgument.ANY_OF:
                    # hence it is a function (or constant), not an actual feature (String)
                    choices = required_feature.arguments[0]
                    selection = [a.string for a in required_feature.arguments[1].arguments]
                    return f"Heros '{feature.name}' is missing minimum level {required_level} for {choices} '{required_feature_type.name}' of {selection}."
                else:
                    return f"Heros '{feature.name}' is missing '{required_feature_type.name}' of '{required_feature.string}' on minimum level {required_level}."
            case _:
                return f"Unspecified error '{error.name}' for '{error.arguments}'."
