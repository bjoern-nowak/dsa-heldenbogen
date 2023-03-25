import logging
from typing import List

from clingo import Symbol

from app.engine import hero_validation_interpreter
from app.engine.rulebook_function import RulebookFunction
from app.models.feature import Feature

logger = logging.getLogger(__name__)


class Collector:
    """Collection of methods to collects specific facts (clingo functions)"""

    @classmethod
    def unusable_rulebooks(cls, symbols: List[Symbol]) -> List[List[str]]:
        unusables: List[List[str]] = []
        for func in cls._functions(symbols, [RulebookFunction.RULEBOOK_MISSING]):
            unusables.append([arg.string for arg in func.arguments])
        return unusables

    @classmethod
    def extra_hero_validation_steps(cls, symbols: List[Symbol]) -> List[Symbol]:
        return cls._functions(symbols, [RulebookFunction.EXTRA_HERO_VALIDATION_STEP])

    @classmethod
    def hero_validation_errors(cls, symbols: List[Symbol]) -> List[Symbol]:
        errors: List[Symbol] = cls._functions(symbols, hero_validation_interpreter.ErrorAtom.list())
        if errors:
            logger.trace(f"Model of failed hero validation:\n{symbols}")
        return errors

    @classmethod
    def hero_validation_warnings(cls, symbols: List[Symbol]) -> List[Symbol]:
        return cls._functions(symbols, hero_validation_interpreter.WarningAtom.list())

    @classmethod
    def known_feature_values(cls, symbols: List[Symbol], feature: Feature) -> List[Symbol]:
        return cls._functions(symbols, [RulebookFunction.known(feature)])

    @staticmethod
    def _functions(symbols: List[Symbol], name_whitelist: List[str] = None) -> List[Symbol]:
        """
        Collects all functions, may filtering by given name whitelist
        :return:
        """
        found = []
        for sym in symbols:
            if not sym.name:  # use 'or not sym.arguments:' to skip constants
                # skip tuples but keep constants
                continue
            if not name_whitelist or sym.name in name_whitelist:
                found.append(sym)
        return found
