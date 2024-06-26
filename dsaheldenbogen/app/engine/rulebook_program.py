from typing import Sequence

from clingo import Symbol

from dsaheldenbogen.app.models.base_enum import BaseEnum

_VALIDATE_HERO_STEP = 'validate_hero_step'


class RulebookProgram(tuple[str, Sequence[Symbol]], BaseEnum):
    """
    LP program parts known/used by the engine.
    """

    BASE = ('base', [])
    """Is always executed, controls default clingo output and pre-defines possible atoms"""

    RULEBOOK_USABLE = ('rulebook_usable', [])
    """Checks whenever the rulebook requirements are met"""

    META = ('meta', [])
    """May contain information about the rulebook for processing, like extra hero validation steps"""

    WORLD_FACTS = ('world_facts', [])
    """Must contain all facts known about the worlds of the rulebook"""

    HERO_FACTS = ('hero_facts', [])
    """Must contain all facts about the hero which can be directly taken from it"""

    VALIDATE_HERO_STEP_50 = (f"{_VALIDATE_HERO_STEP}_50", [])
    """Validates hero: pre check - values known"""

    VALIDATE_HERO_STEP_100 = (f"{_VALIDATE_HERO_STEP}_100", [])
    """Validates hero race usable"""

    VALIDATE_HERO_STEP_150 = (f"{_VALIDATE_HERO_STEP}_150", [])
    """Validates hero race requirements"""

    VALIDATE_HERO_STEP_200 = (f"{_VALIDATE_HERO_STEP}_200", [])
    """Validates hero culture usable"""

    VALIDATE_HERO_STEP_250 = (f"{_VALIDATE_HERO_STEP}_250", [])
    """Validates hero culture requirements"""

    VALIDATE_HERO_STEP_300 = (f"{_VALIDATE_HERO_STEP}_300", [])
    """Validates hero profession usable"""

    VALIDATE_HERO_STEP_350 = (f"{_VALIDATE_HERO_STEP}_350", [])
    """Validates hero profession requirements"""

    VALIDATE_HERO_STEP_400 = (f"{_VALIDATE_HERO_STEP}_400", [])
    """Validates hero (dis)advantages usable"""

    VALIDATE_HERO_STEP_450 = (f"{_VALIDATE_HERO_STEP}_450", [])
    """Validates hero (dis)advantages requirements"""

    VALIDATE_HERO_STEP_500 = (f"{_VALIDATE_HERO_STEP}_500", [])
    """Validates hero skills (talents, combat techniques) usable"""

    VALIDATE_HERO_STEP_550 = (f"{_VALIDATE_HERO_STEP}_550", [])
    """Validates hero skills (talents, combat techniques) requirements"""

    @staticmethod
    def hero_validation_step_for(number: int) -> tuple[str, Sequence[Symbol]]:
        return f"{_VALIDATE_HERO_STEP}_{number}", []
