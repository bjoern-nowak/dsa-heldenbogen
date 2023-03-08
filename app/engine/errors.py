from typing import List

from app.engine.hero_validation_interpreter import HeroValidationError


# TODO should this be in model module/package?


class UnexpectedResultError(Exception):
    """A result was not expected, since there was no other error the reason seems yet to be unknown/handled"""


class UnusableRulebookError(Exception):
    """Set of rulebooks contains at least one unusable."""


class HeroInvalidError(Exception):
    """
    Thrown if a hero validation was not passed, containing all errors.
    """

    def __init__(self, errors: List[HeroValidationError], message: str = "Hero is not valid."):
        self.errors = errors
        self.message = message
