from __future__ import annotations  # required till PEP 563

from typing import List
from typing import Sequence

from clingo import Control
from clingo import SolveResult
from clingo import Symbol

from dsaheldenbogen.app.logger import getLogger
from dsaheldenbogen.app.models.hero import Hero
from dsaheldenbogen.infrastructure.hero_wrapper import HeroWrapper

logger = getLogger(__name__)


class ClingoExecutor:
    """
    This class is the engines last-mile to call/run clingo.
    """

    lp_files: List[str]
    default_programs: List[tuple[str, Sequence[Symbol]]]

    def __init__(self, lp_files: List[str], default_programs: List[tuple[str, Sequence[Symbol]]] = None) -> None:
        self.lp_files = lp_files
        self.default_programs = default_programs if default_programs else []

    def run(self,
            programs: List[tuple[str, Sequence[Symbol]]],
            context: Hero = None,
            on_fail: Exception = None) -> List[Symbol]:
        """
        Do a clean clingo solve run
        :param programs: to ground
        :param context: hero to use
        :param on_fail: called on unsatisfiable run
        :returns: all clingo symbols (even not shown ones) when run was satisfied
        """
        ctl = self._create_control(self.default_programs + programs, context)
        symbols: List[Symbol] = []
        result: SolveResult = ctl.solve(on_model=lambda m: symbols.extend(m.symbols(atoms=True)))
        if not result.satisfiable:
            raise on_fail if on_fail else RuntimeError(f"Could not execute clingo programs: {[p[0] for p in programs]}")
        return symbols

    def _create_control(self, programs: List[tuple[str, Sequence[Symbol]]], context: Hero = None) -> Control:
        """
        Creates a fresh clingo control for predefined logic program file
        :param programs: to be grounded
        :param context: hero to be used
        """
        ctl = Control()
        for lp_file in self.lp_files:
            ctl.load(lp_file)
        ctl.ground(programs, HeroWrapper(context) if isinstance(context, Hero) else context)
        return ctl
