import logging
from typing import List

from src.app.engine.engine import Engine
from src.app.engine.exceptions import HeroInvalidError
from src.app.models.hero import Hero
from src.app.models.hero_validation_warning import HeroValidationWarning
from src.app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class HeroService:

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> List[HeroValidationWarning]:
        """
        Check whenever the given hero comply under given rulebooks.
        :returns: when validation passed (hero is valid) a list of warnings
        :raises HeroInvalidError: whenever hero breaks a rule
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

    def save(self, hero: Hero, rulebooks: List[Rulebook]) -> bool:
        # TODO implement me
        raise NotImplementedError("Function 'save' is not yet implemented.")

    def export(self, hero_name: str) -> bool:
        # TODO implement me
        raise NotImplementedError("Function 'export' is not yet implemented.")

    def delete(self, hero_name: str) -> bool:
        # TODO implement me
        raise NotImplementedError("Function 'delete' is not yet implemented.")
