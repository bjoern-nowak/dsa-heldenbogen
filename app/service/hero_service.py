import logging
from typing import List

from app.engine.engine import Engine
from app.models import Hero
from app.models.rulebook import Rulebook


class HeroService:

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> List[str]:
        engine = Engine(rulebooks)
        errors: List[str] = engine.validate(hero)
        return errors
