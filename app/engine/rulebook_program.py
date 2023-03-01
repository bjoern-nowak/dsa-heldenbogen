from enum import Enum
from typing import Sequence

from clingo import Symbol


class RulebookProgram(tuple[str, Sequence[Symbol]], Enum):
    BASE = ("base", [])
    RULEBOOK_USABLE = ("rulebook_usable", [])
    VALIDATE_HERO = ("validate_hero", [])
