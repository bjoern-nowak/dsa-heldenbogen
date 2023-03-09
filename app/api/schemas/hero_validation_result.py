from __future__ import annotations  # required till PEP 563

from typing import List

from app.models.base_model import BaseModel
from app.models.hero_validation_error import HeroValidationError
from app.models.hero_validation_warning import HeroValidationWarning


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
