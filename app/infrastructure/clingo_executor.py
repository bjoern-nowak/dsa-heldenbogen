from __future__ import annotations  # required till PEP 563

import logging
from typing import List
from typing import Sequence

from clingo import Control
from clingo import Model
from clingo import SolveResult
from clingo import Symbol

from app.infrastructure.hero_wrapper import HeroWrapper
from app.models.hero import Hero

logger = logging.getLogger(__name__)


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
            on_fail: Exception = None) -> Model:
        """
        Do a clean clingo solve run
        :param programs: to ground
        :param context: hero to use
        :param on_fail: called on unsatisfiable run
        :returns: clingo Model when run was satisfied
        """
        ctl = self._create_control(self.default_programs + programs, context)
        model: List[Model] = []
        result: SolveResult = ctl.solve(on_model=lambda m: model.append(m))  # lambda cannot handle var assignment hence a list
        if not model or not result.satisfiable:
            raise on_fail if on_fail else RuntimeError(f"Could not execute clingo programs: {[p[0] for p in programs]}")
        return model[0]

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
