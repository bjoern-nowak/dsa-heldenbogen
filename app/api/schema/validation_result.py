from __future__ import annotations  # required till PEP 563

from typing import List

from app.engine.hero_validation_error import HeroValidationError
from app.engine.hero_validation_warning import HeroValidationWarning
from app.models.basemodel import BaseModel


# TODO rename file/module to reflect class name
class HeroValidationResult(BaseModel):
    valid: bool
    errors: List[HeroValidationError]
    warnings: List[HeroValidationWarning]

    @staticmethod
    def passed(warnings: List[HeroValidationWarning] = None) -> HeroValidationResult:
        return HeroValidationResult(valid=True, errors=[], warnings=warnings if warnings else [])

    @staticmethod
    def failed(errors: List[HeroValidationError], warnings: List[HeroValidationWarning] = None) -> HeroValidationResult:
        return HeroValidationResult(valid=False, errors=errors, warnings=warnings if warnings else [])
