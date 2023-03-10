import logging
from typing import List

from app import resource
from app.engine.engine import Engine
from app.models.feature import Feature
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class MetaService:

    def list_known_rulebooks(self) -> List[str]:
        # TODO filter unusable/broken rulebooks
        return resource.list_dirs(Rulebook.res_folder_name())

    def list_known_feature_values(self, feature: Feature, rulebooks: List[Rulebook]) -> List[str]:
        engine = Engine(rulebooks)
        known_values = engine.list_known_for(feature)
        logger.debug(f"Value list of '{feature}' with rulebooks {[str(r) for r in rulebooks]}: {known_values}")
        return known_values
