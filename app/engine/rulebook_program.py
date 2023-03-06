from typing import Sequence

from clingo import Symbol

from app.models.base_enum import BaseEnum

_VALIDATE_HERO_STEP_PREFIX = 'validate_hero_step_'


class RulebookProgram(tuple[str, Sequence[Symbol]], BaseEnum):
    BASE = ('base', [])
    RULEBOOK_USABLE = ('rulebook_usable', [])
    META = ('meta', [])
    HERO_FACTS = ('hero_facts', [])
    VALIDATE_HERO_STEP_100 = (f"{_VALIDATE_HERO_STEP_PREFIX}100", [])
    """Validates heros species"""
    VALIDATE_HERO_STEP_200 = (f"{_VALIDATE_HERO_STEP_PREFIX}200", [])
    """Validates heros culture"""
    VALIDATE_HERO_STEP_300 = (f"{_VALIDATE_HERO_STEP_PREFIX}300", [])
    """Validates heros profession"""

    @staticmethod
    def hero_validation_step_for(number: int) -> tuple[str, Sequence[Symbol]]:
        return f"{_VALIDATE_HERO_STEP_PREFIX}{number}", []
