from __future__ import annotations  # required till PEP 563

from typing import List

from app.engine.hero_validation_interpreter import HeroValidationError
from app.models import BaseModel


class HeroValidationResult(BaseModel):
    valid: bool
    errors: List[HeroValidationError]

    @staticmethod
    def passed() -> HeroValidationResult:
        return HeroValidationResult(valid=True, errors=[])

    @staticmethod
    def failed(errors: List[HeroValidationError]) -> HeroValidationResult:
        return HeroValidationResult(valid=False, errors=errors)
