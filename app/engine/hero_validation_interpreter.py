from enum import Enum

from clingo import Symbol

from app.engine.rulebook_function import RulebookFunction


class HeroValidationErrors(str, Enum):
    TALENT = 'talent'
    COMBAT_TECHNIQUE = 'combat_technique'


class HeroValidationInterpreter:

    # TODO return an error object which also holds an error type and each reason argument, usable in frontend and testcases
    @staticmethod
    def str(error: Symbol) -> str:
        reason = error.arguments[0]
        match error.name:
            case RulebookFunction.SPECIES_UNKNOWN:
                return f"Species '{reason.string}' is unknown."
            case RulebookFunction.CULTURE_UNKNOWN:
                return f"Culture '{reason.string}' is unknown."
            case RulebookFunction.CULTURE_UNUSABLE:
                return f"Culture is unusable for {reason.name}."
            case RulebookFunction.PROFESSION_UNKNOWN:
                return f"Profession '{reason.string}' is unknown."
            case RulebookFunction.PROFESSION_UNUSABLE:
                return f"Profession is unusable for {reason.name}."
            case RulebookFunction.PROFESSION_MISSING:
                match reason.name:
                    case HeroValidationErrors.TALENT:
                        return f"Profession is missing talent '{reason.arguments[0].string}' on minimum level {reason.arguments[1]}."
                    case HeroValidationErrors.COMBAT_TECHNIQUE:
                        return f"Profession is missing combat technique '{reason.arguments[0].string}' on minimum level {reason.arguments[1]}."
                    case _:
                        return f"(Generic; non pre-defined)" \
                               f"Profession is missing {reason.name} with '{reason.arguments}'."
            case _:
                return f"Unspecified error '{error.name}' for '{error.arguments}'."
