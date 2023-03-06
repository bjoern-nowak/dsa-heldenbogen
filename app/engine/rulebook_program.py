from typing import Sequence

from clingo import Symbol

from app.models.base_enum import BaseEnum

_VALIDATE_HERO_STEP = 'validate_hero_step'


class RulebookProgram(tuple[str, Sequence[Symbol]], BaseEnum):
    BASE = ('base', [])
    RULEBOOK_USABLE = ('rulebook_usable', [])
    META = ('meta', [])
    HERO_FACTS = ('hero_facts', [])
    VALIDATE_HERO_STEP_100 = (f"{_VALIDATE_HERO_STEP}_100", [])
    """Validates hero species usable"""
    VALIDATE_HERO_STEP_150 = (f"{_VALIDATE_HERO_STEP}_150", [])
    """Validates hero species requirements"""
    VALIDATE_HERO_STEP_200 = (f"{_VALIDATE_HERO_STEP}_200", [])
    """Validates hero culture usable"""
    VALIDATE_HERO_STEP_250 = (f"{_VALIDATE_HERO_STEP}_250", [])
    """Validates hero culture requirements"""
    VALIDATE_HERO_STEP_300 = (f"{_VALIDATE_HERO_STEP}_300", [])
    """Validates hero profession usable"""
    VALIDATE_HERO_STEP_350 = (f"{_VALIDATE_HERO_STEP}_350", [])
    """Validates hero profession requirements"""

    @staticmethod
    def hero_validation_step_for(number: int) -> tuple[str, Sequence[Symbol]]:
        return f"{_VALIDATE_HERO_STEP}_{number}", []
