from __future__ import annotations  # required till PEP 563

import logging
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Sequence

from clingo import Control
from clingo import Function
from clingo import Model
from clingo import SolveResult
from clingo import String
from clingo import Symbol
from clingo import SymbolType

from app.engine.exceptions import UnexpectedResultError
from app.engine.rulebook_program import RulebookProgram
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class TestEngine:
    """This does not test the engine, it is an engine for testing"""
    FUNCTION_PROGRAM = 'program'

    def __init__(self, rulebook: Rulebook) -> None:
        self.rulebooks = [rulebook]

    def has_programs(self, programs: List[RulebookProgram]) -> List[str]:
        """
        :return: List of not found programs
        TODO how to test program existence without having an pseudo atom representing it: then remove these from rulebooks
        """
        functions: List[Symbol] = []
        self._execute(programs, on_model=lambda m: TestEngine._collect_functions(m, functions, TestEngine.FUNCTION_PROGRAM))
        if functions:
            return list(set([p[0] for p in programs]) - set([f.arguments[0].string for f in functions]))
        else:
            return [p[0] for p in programs]

    def has_only_function(self, programs: List[RulebookProgram], name: str, value: str) -> tuple[bool, List[str]]:
        """
        :return: tuple of (<has function with value>, <other found values>
        """
        functions: List[Symbol] = []
        self._execute(programs, on_model=lambda m: TestEngine._collect_functions(m, functions, name))
        if functions:
            only = Function(name, [String(value)])
            if only in functions:
                functions.remove(only)
                return True, [f.arguments[0].string for f in functions]
            else:
                return False, [f.arguments[0].string for f in functions]
        else:
            return False, []

    def _execute(self,
                 programs: List[tuple[str, Sequence[Symbol]]],
                 context: Any = None,
                 on_model: Optional[Callable[[Model], Optional[bool]]] = None,
                 on_fail_raise: Exception = None):
        ctl = self._create_control()
        ctl.ground(programs, context)
        result: SolveResult = ctl.solve(on_model=on_model)
        if not result.satisfiable:
            raise UnexpectedResultError(f"Could not execute clingo programs: {programs}")

    def _create_control(self) -> Control:
        ctl = Control()
        ctl.load(Rulebook.common_file())
        for rulebook in self.rulebooks:
            ctl.load(rulebook.entrypoint())
        return ctl

    @staticmethod
    def _collect_functions(model: Model, functions: List[Symbol], name: str):
        for sym in model.symbols(atoms=True):
            if sym.type == SymbolType.Function and sym.name == name:
                functions.append(sym)
