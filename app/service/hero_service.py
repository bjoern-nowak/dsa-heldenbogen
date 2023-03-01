from typing import List

from app.engine.engine import Engine
from app.error import UnexpectedResultError
from app.models import Hero
from app.models.rulebook import Rulebook


class HeroService:

    def validate(self, hero: Hero, rulebooks: List[Rulebook]) -> List[str]:
        engine = Engine(rulebooks)
        errors: List[str] = engine.validate(hero)
        if errors is None:
            raise UnexpectedResultError("Hero has not been validated.")
        return errors
