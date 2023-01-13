from typing import List

from clingo import Model

from app.engine.regelwerk import ClingoEngine
from app.models import Held
from app.service import RegelSet


class Regelwerk:

    def __init__(self, regelsets: List[RegelSet]) -> None:
        self.regelsets = regelsets

    def check(self, held: Held, is_print_model: bool = False) -> bool:
        return ClingoEngine(self.regelsets).check(held, is_print_model)

    def _on_model(self, m: Model, is_print_model: bool):
        if is_print_model:
            print(m)
