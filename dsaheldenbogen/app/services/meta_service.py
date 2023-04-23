import logging
from typing import List

from dsaheldenbogen.app.engine.engine import Engine
from dsaheldenbogen.app.models.feature import Feature
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.services.rulebook_validator import RulebookValidator

logger = logging.getLogger(__name__)


class MetaService:

    def __init__(self, engine_clz: type = Engine) -> None:
        self.engine_clz = engine_clz

    def list_usable_rulebooks(self) -> List[Rulebook]:
        """
        List all rulebooks which are ready to use
        """
        return RulebookValidator.filter(Rulebook.list_known())

    def list_known_feature_values(self, feature: Feature, rulebooks: List[Rulebook]) -> List[tuple[str, str, int]] | List[str]:
        """
        List all known feature values of given feature considering given rulebooks
        :return: List[tuple[str, str, int]] in case of DisAdvantages else List[str]
        """
        engine = self.engine_clz(rulebooks)
        known_values = engine.list_known_for(feature)
        logger.debug(f"Value list of '{feature}' with rulebooks {[str(r) for r in rulebooks]}: {known_values}")
        return known_values
