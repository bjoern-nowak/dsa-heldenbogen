from clingo import Symbol

from app.engine.rulebook_function import RulebookFunction


class HeroValidationInterpreter:

    @staticmethod
    def str(error: Symbol) -> str:
        match error.name:
            case RulebookFunction.SPECIES_UNKNOWN:
                return f"Species '{error.arguments[0].string}' is unknown."
            case RulebookFunction.CULTURE_UNKNOWN:
                return f"Culture '{error.arguments[0].string}' is unknown."
            case RulebookFunction.CULTURE_UNUSABLE:
                return f"Culture is unusable for species."
            case RulebookFunction.PROFESSION_UNKNOWN:
                return f"Profession '{error.arguments[0].string}' is unknown."
            case _:
                return f"Unspecified error '{error.name}' for '{error.arguments}'."
