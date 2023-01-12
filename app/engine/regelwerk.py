from typing import List

from clingo import Control
from clingo import Model
from clingo import SolveResult

from app.engine import RegelSet
from app.engine.clingo_wrapper import ClingoHeld
from app.engine.resource import get_abs_path
from app.models import Held


class Regelwerk:

    def __init__(self, regelsets: List[RegelSet]) -> None:
        self.regelsets = regelsets
        self.fakten = [get_abs_path('held_fakten.lp')]

    def check(self, held: Held, is_print_model: bool = False) -> bool:
        ctl = Control()
        for lp in self.fakten + self.regelsets:
            ctl.load(lp)

        ctl.ground(context=ClingoHeld.wrap(held))
        result: SolveResult = ctl.solve(on_model=lambda m: self._on_model(m, is_print_model))
        return result.satisfiable

    def _on_model(self, m: Model, is_print_model: bool):
        if is_print_model:
            print(m)
