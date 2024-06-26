from typing import List

from dsaheldenbogen.app.engine.engine import Engine
from dsaheldenbogen.app.engine.exceptions import HeroInvalidError
from dsaheldenbogen.app.logger import getLogger
from dsaheldenbogen.app.models.hero import Hero
from dsaheldenbogen.app.models.hero_validation_warning import HeroValidationWarning
from dsaheldenbogen.app.models.rulebook import Rulebook

logger = getLogger(__name__)


class HeroService:

    def __init__(self, engine_clz: type = Engine) -> None:
        self.engine_clz = engine_clz

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> List[HeroValidationWarning]:
        """
        Check whenever the given hero comply under given rulebooks.
        :returns: when validation passed (hero is valid) a list of warnings
        :raises HeroInvalidError: whenever hero breaks a rule
        """
        engine = self.engine_clz(rulebooks)
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
