import logging
from typing import List

from app.engine.engine import Engine
from app.engine.errors import HeroInvalidError
from app.models import Hero
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class HeroService:

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> True:
        """
        Check whenever the given hero comply under given rulebooks else it raises errors.
        :returns: True only if no error occurred, this is just for usages in conditions
        """
        engine = Engine(rulebooks)
        try:
            engine.validate(hero)
            logger.trace(f"Hero validation passed for: {hero}")
            return True
        except HeroInvalidError as ex:
            logger.debug(
                f"{ex.message}\n"
                f"Hero: {hero}\n"
                f"Errors: {ex.errors}"
            )
            raise ex
