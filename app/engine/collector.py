from typing import List

from clingo import Model
from clingo import Symbol

from app.engine.rulebook_function import RulebookFunction


class Collector:

    @staticmethod
    def functions_first_string(found: List[str], model: Model, by_name: str = None) -> None:
        """
        Collects all first arguments as a string of all functions
        :param found: list to be filled
        :param model: to search in
        :param by_name: (optional) filter functions by given name
        :return:
        """
        functions_args: List[List[str]] = []
        Collector.functions_strings(functions_args, model, by_name)
        for func_args in functions_args:
            found.append(func_args[0])

    @staticmethod
    def functions_strings(found: List[List[str]], model: Model, by_name: RulebookFunction = None) -> None:
        """
        Collects all arguments as a string of all functions
        :param found: list to be filled
        :param model: to search in
        :param by_name: (optional) filter functions by given name
        :return:
        """
        functions: List[Symbol] = []
        Collector.functions(functions, model)
        for func in functions:
            if not by_name or (by_name == func.name):
                found.append([arg.string for arg in func.arguments])

    @staticmethod
    def functions(found: List[Symbol], model: Model, suffixes: List[RulebookFunction] = None) -> None:
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
    def symbols(found: List[Symbol], model: Model) -> None:
        for sym in model.symbols(atoms=True):
            found.append(sym)
