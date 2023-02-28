from typing import List

from clingo import Model
from clingo import Symbol


class Collector:

    @staticmethod
    def functions_first_string(found: List[str], model: Model, by_name: str = None) -> None:
        """
        Collects all first arguments as a string of all functions
        :param found: list to be filled
        :param by_name: (optional) filter functions by given name
        :return:
        """
        # print(model)
        for sym in model.symbols(atoms=True):
            if not sym.name or not sym.arguments:
                # skip non function symbols like tuples and constants
                continue
            if not by_name or (by_name == sym.name):
                found.append(sym.arguments[0].string)

    @staticmethod
    def symbols(found: List[Symbol], model: Model) -> None:
        # print(model)
        for sym in model.symbols(atoms=True):
            found.append(sym)
