from __future__ import annotations  # required till PEP 563

import logging
from typing import List
from typing import Set

from clingo import Function
from clingo import String
from clingo import Symbol
from clingo import SymbolType

from app.engine.rulebook_program import RulebookProgram
from app.infrastructure.clingo_executor import ClingoExecutor
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class TestEngine:
    """This does not test the engine, it is an engine for testing"""
    FUNCTION_PROGRAM = 'program'

    def __init__(self, rulebook: Rulebook) -> None:
        self.rulebooks = [rulebook]
        self.clingo_executor = ClingoExecutor(
            [Rulebook.common_file()] + [r.entrypoint_file() for r in self.rulebooks],
            [RulebookProgram.BASE]
        )

    def has_programs(self, programs: List[RulebookProgram]) -> List[str]:
        """
        :return: List of not found programs
        TODO how to test program existence without having an pseudo atom representing it: then remove these from rulebooks
        """
        functions: List[Symbol] = TestEngine._collect_functions(self.clingo_executor.run(programs),
                                                                TestEngine.FUNCTION_PROGRAM)
        if functions:
            return list(set([p[0] for p in programs]) - set([f.arguments[0].string for f in functions]))
        else:
            return [p[0] for p in programs]

    def has_function_with_value(self, programs: List[RulebookProgram], name: str, value: str) -> tuple[bool, Set[str]]:
        """
        :return: tuple of (<has function with value>, <other found values>
        """
        functions: List[Symbol] = TestEngine._collect_functions(self.clingo_executor.run(programs), name)
        if functions:
            target = Function(name, [String(value)])
            others = set(f.arguments[0].string for f in functions if f.name == name)
            if target in functions:
                others.remove(value)
                return True, others
            else:
                return False, others
        else:
            return False, set()

    @staticmethod
    def _collect_functions(symbols: List[Symbol], name: str) -> List[Symbol]:
        functions: List[Symbol] = []
        for sym in symbols:
            if sym.type == SymbolType.Function and sym.name == name:
                functions.append(sym)
        return functions
