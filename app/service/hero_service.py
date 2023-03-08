import logging
from typing import List

from app.engine.engine import Engine
from app.engine.exceptions import HeroInvalidError
from app.engine.hero_validation_warning import HeroValidationWarning
from app.models import Hero
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class HeroService:

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> List[HeroValidationWarning]:
        """
        Check whenever the given hero comply under given rulebooks else it raises errors.
        :returns: list of warnings, when validation passed (hero is valid)
        """
        engine = Engine(rulebooks)
        try:
            warnings: List[HeroValidationWarning] = engine.validate(hero)
            logger.trace(f"Hero validation passed.\n"
                         f"Hero: {hero}\n"
                         f"Warnings: {warnings}")
            return warnings
        except HeroInvalidError as ex:
            logger.debug(
                f"{ex.message}\n"
                f"Hero: {hero}\n"
                f"Errors: {ex.errors}\n"
                f"Warnings: {ex.warnings}"
            )
            raise ex
