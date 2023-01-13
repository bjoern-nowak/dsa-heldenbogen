from pathlib import Path
from typing import List

from clingo import Control
from clingo import Model
from clingo import SolveResult

from app.engine.clingo_held import ClingoHeld
from app.engine.clingo_logik import clingo_logik
from app.models import Held
from app.resource import get_path
from app.service import RegelSet


class ClingoEngine:

    def __init__(self, regelsets: List[RegelSet]) -> None:
        self.regelsets: List[Path] = self._map_regelsets(regelsets)
        self.fakten: List[Path] = [get_path('held_fakten.lp')]

    def _map_regelsets(self, regelsets: List[RegelSet]) -> List[Path]:
        mapped: List[Path] = []
        for regelset in regelsets:
            if regelset in clingo_logik:
                mapped.append(clingo_logik[regelset])
            else:
                raise NotImplementedError(f"Für das Regelset '{regelset}' gibt es keine Implementierung.")
        return mapped

    def check(self, held: Held, is_print_model: bool = False) -> bool:
        ctl = Control()
        for lp in self.fakten + self.regelsets:
            ctl.load(lp.as_posix())

        ctl.ground(context=ClingoHeld.wrap(held))
        result: SolveResult = ctl.solve(on_model=lambda m: self._on_model(m, is_print_model))
        return result.satisfiable

    def _on_model(self, m: Model, is_print_model: bool):
        if is_print_model:
            print(m)
