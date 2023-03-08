import logging
from typing import List

from clingo import Model
from clingo import Symbol

from app.engine.hero_validation_interpreter import HeroValidationErrorType
from app.engine.rulebook_function import RulebookFunction
from app.models import Feature

logger = logging.getLogger(__name__)


class Collector:

    @classmethod
    def unusable_rulebooks(cls, model: Model, unusables: List[List[str]]):
        cls._functions_strings(unusables, model, RulebookFunction.RULEBOOK_UNUSABLE)

    @classmethod
    def extra_hero_validation_steps(cls, model: Model, steps: List[Symbol]):
        cls._functions(steps, model, [RulebookFunction.EXTRA_HERO_VALIDATION_STEP])

    @classmethod
    def hero_validation_errors(cls, model: Model, errors: List[Symbol]):
        cls._functions(errors, model, HeroValidationErrorType.list())
        if errors:
            logger.trace(f"Model of failed hero validation:\n{model}")

    @classmethod
    def known_feature_values(cls, model: Model, known_values: List[str], feature: Feature):
        cls._functions_first_string(known_values, model, RulebookFunction.known(feature))

    @classmethod
    def _functions_first_string(cls, found: List[str], model: Model, by_name: str = None) -> None:
        """
        Collects all first arguments as a string of all functions
        :param found: list to be filled
        :param model: to search in
        :param by_name: (optional) filter functions by given name
        :return:
        """
        functions_args: List[List[str]] = []
        cls._functions_strings(functions_args, model, by_name)
        for func_args in functions_args:
            found.append(func_args[0])

    @classmethod
    def _functions_strings(cls, found: List[List[str]], model: Model, by_name: RulebookFunction = None) -> None:
        """
        Collects all arguments as a string of all functions
        :param found: list to be filled
        :param model: to search in
        :param by_name: (optional) filter functions by given name
        :return:
        """
        functions: List[Symbol] = []
        cls._functions(functions, model)
        for func in functions:
            if not by_name or (by_name == func.name):
                found.append([arg.string for arg in func.arguments])

    @staticmethod
    def _functions(found: List[Symbol], model: Model, suffixes: List[RulebookFunction] = None) -> None:
        """
        Collects all functions having given suffix in name
        :param found: list to be filled
        :param model: to search in
        :param suffixes: to filter function names by
        :return:
        """
        for sym in model.symbols(atoms=True):
            if not sym.name:  # use 'or not sym.arguments:' to skip constants
                # skip tuples but keep constants
                continue
            if not suffixes or sym.name.endswith(tuple(suffixes)):
                found.append(sym)

    @staticmethod
    def _symbols(found: List[Symbol], model: Model) -> None:
        for sym in model.symbols(atoms=True):
            found.append(sym)
