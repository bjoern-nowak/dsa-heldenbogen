from typing import List

from app.engine.clingo_engine import ClingoEngine
from app.models import Held
from app.models.feature import Feature
from app.models.rulebook import Rulebook


class UnexpectedResultError(Exception):
    """A result was not expected, since there was no other error the reason seems yet to be unknown/handled"""


class RegelEngine:

    def __init__(self, rulebooks: List[Rulebook]) -> None:
        self.engine = ClingoEngine(rulebooks)

    def list(self, feature: Feature) -> List[str]:
        features = self.engine.list(feature)
        if not features:
            raise UnexpectedResultError("List of possible values for feature has not been generated.")
        return features

    def check(self, held: Held, is_print_model: bool = False) -> bool:
        valid = self.engine.check(held, is_print_model)
        if valid is None:
            raise UnexpectedResultError("Hero has not been checked.")
        return valid
