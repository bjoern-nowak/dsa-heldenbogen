from typing import List

from app.engine.clingo_engine import ClingoEngine
from app.models import Held
from app.models.feature import Feature
from app.service import Regelwerk


class RegelEngine:

    def __init__(self, rulebooks: List[Regelwerk]) -> None:
        self.engine = ClingoEngine(rulebooks)

    def list(self, merkmal: Feature) -> List[str]:
        return self.engine.list(merkmal)

    def check(self, held: Held, is_print_model: bool = False) -> bool:
        return self.engine.check(held, is_print_model)
