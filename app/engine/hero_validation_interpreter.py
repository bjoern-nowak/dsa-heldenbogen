from clingo import Symbol

from app.engine.rulebook_function import RulebookFunction


class HeroValidationInterpreter:

    # TODO return an error object which also holds a type
    @staticmethod
    def str(error: Symbol) -> str:
        match error.name:
            case RulebookFunction.SPECIES_UNKNOWN:
                return f"Species '{error.arguments[0].string}' is unknown."
            case RulebookFunction.CULTURE_UNKNOWN:
                return f"Culture '{error.arguments[0].string}' is unknown."
            case RulebookFunction.CULTURE_UNUSABLE:
                return f"Culture is unusable for {error.arguments[0].name}."
            case RulebookFunction.PROFESSION_UNKNOWN:
                return f"Profession '{error.arguments[0].string}' is unknown."
            case RulebookFunction.PROFESSION_UNUSABLE:
                return f"Profession is unusable for {error.arguments[0].name}."
            case _:
                return f"Unspecified error '{error.name}' for '{error.arguments}'."
