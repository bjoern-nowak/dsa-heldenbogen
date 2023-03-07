import logging
from typing import List

from app.engine.engine import Engine
from app.models import Hero
from app.models.rulebook import Rulebook

logger = logging.getLogger(__name__)


class HeroService:

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> List[str]:
        engine = Engine(rulebooks)
        errors: List[str] = engine.validate(hero)
        if errors:
            logger.debug(
                f"Hero validation failed\n"
                f"Hero: {hero}\n"
                f"Errors: {errors}"
            )
        else:
            logger.debug(f"Hero validation passed\n")
        return errors
