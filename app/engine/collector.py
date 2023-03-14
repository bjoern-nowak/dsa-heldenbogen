import logging
from typing import List

from clingo import Model
from clingo import Symbol

from app.engine import hero_validation_interpreter
from app.engine.rulebook_function import RulebookFunction
from app.models.feature import Feature

logger = logging.getLogger(__name__)


class Collector:

    @classmethod
    def unusable_rulebooks(cls, model: Model, unusables: List[List[str]]):
        unusables.extend(cls._functions_strings(model, RulebookFunction.RULEBOOK_MISSING))

    @classmethod
    def extra_hero_validation_steps(cls, model: Model, steps: List[Symbol]):
        steps.extend(cls._functions(model, [RulebookFunction.EXTRA_HERO_VALIDATION_STEP]))

    @classmethod
    def hero_validation_errors_and_warnings(cls, model: Model, errors: List[Symbol], warnings: List[Symbol]):
        errors.extend(cls._functions(model, hero_validation_interpreter.ErrorAtom.list()))
        warnings.extend(cls._functions(model, hero_validation_interpreter.WarningAtom.list()))
        if errors:
            logger.trace(f"Model of failed hero validation:\n{model.symbols(shown=True)}")

    @classmethod
    def known_feature_values(cls, model: Model, known_values: List[str], feature: Feature):
        known_values.extend(cls._functions_first_string(model, RulebookFunction.known(feature)))

    @classmethod
    def _functions_first_string(cls, model: Model, by_name: str = None) -> List[str]:
        """
        Collects all first arguments as a string of all functions
        """
        found = []
        for func in cls._functions(model):
            if not by_name or (by_name == func.name):
                found.append(func.arguments[0].string)
        return found

    @classmethod
    def _functions_strings(cls, model: Model, by_name: RulebookFunction = None) -> List[List[str]]:
        """
        Collects all arguments as a string of all functions
        """
        found = []
        for func in cls._functions(model):
            if not by_name or (by_name == func.name):
                found.append([arg.string for arg in func.arguments])
        return found

    @staticmethod
    def _functions(model: Model, name_whitelist: List[str] = None) -> List[Symbol]:
        """
        Collects all functions, may filtering by given name whitelist
        :return:
        """
        found = []
        for sym in model.symbols(atoms=True):
            if not sym.name:  # use 'or not sym.arguments:' to skip constants
                # skip tuples but keep constants
                continue
            if not name_whitelist or sym.name in name_whitelist:
                found.append(sym)
        return found

    @staticmethod
    def _symbols(model: Model) -> List[Symbol]:
        return [sym for sym in model.symbols(atoms=True)]
