import logging
from typing import List

from app.engine.engine import Engine
from app.models.feature import Feature
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class MetaService:

    def list(self, feature: Feature, rulebooks: List[Rulebook]) -> List[str]:
        engine = Engine(rulebooks)
        known_values = engine.list(feature)
        logger.debug(f"Value list of '{feature}' with rulebooks {[str(r) for r in rulebooks]}: {known_values}")
        return known_values
