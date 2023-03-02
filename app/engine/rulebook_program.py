from enum import Enum
from typing import Sequence

from clingo import Symbol


class RulebookProgram(tuple[str, Sequence[Symbol]], Enum):
    BASE = ("base", [])
    RULEBOOK_USABLE = ("rulebook_usable", [])
    VALIDATE_HERO = ("validate_hero", [])
    VALIDATE_HERO_STEP1 = ("validate_hero_step1", [])
    VALIDATE_HERO_STEP2 = ("validate_hero_step2", [])
    VALIDATE_HERO_STEP3 = ("validate_hero_step3", [])
