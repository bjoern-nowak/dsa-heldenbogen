from typing import List

from app.engine.engine import Engine
from app.error import UnexpectedResultError
from app.models.feature import Feature
from app.models.rulebook import Rulebook


class MetaService:

    def list(self, feature: Feature, rulebooks: List[Rulebook]) -> List[str]:
        engine = Engine(rulebooks)
        features = engine.list(feature)
        if features is None:
            raise UnexpectedResultError(f"List of possible values for feature '{feature}' has not been generated.")
        return features
