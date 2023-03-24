import logging
from typing import List

from clingo import Model
from clingo import Symbol

from app.engine import hero_validation_interpreter
from app.engine.rulebook_function import RulebookFunction
from app.models.feature import Feature

logger = logging.getLogger(__name__)


class Collector:
    """Collects specific facts (clingo functions) from clingo model"""

    @classmethod
    def unusable_rulebooks(cls, model: Model) -> List[List[str]]:
        unusables: List[List[str]] = []
        for func in cls._functions(model, [RulebookFunction.RULEBOOK_MISSING]):
            unusables.append([arg.string for arg in func.arguments])
        return unusables

    @classmethod
    def extra_hero_validation_steps(cls, model: Model) -> List[Symbol]:
        return cls._functions(model, [RulebookFunction.EXTRA_HERO_VALIDATION_STEP])

    @classmethod
    def hero_validation_errors(cls, model: Model) -> List[Symbol]:
        errors: List[Symbol] = cls._functions(model, hero_validation_interpreter.ErrorAtom.list())
        if errors:
            logger.trace(f"Model of failed hero validation:\n{model.symbols(shown=True)}")
        return errors

    @classmethod
    def hero_validation_warnings(cls, model: Model) -> List[Symbol]:
        return cls._functions(model, hero_validation_interpreter.WarningAtom.list())

    @classmethod
    def known_feature_values(cls, model: Model, feature: Feature) -> List[Symbol]:
        return cls._functions(model, [RulebookFunction.known(feature)])

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
