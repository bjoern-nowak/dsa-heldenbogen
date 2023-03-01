from __future__ import annotations  # required till PEP 563

from typing import List

from app.models import BaseModel


class HeroValidationResult(BaseModel):
    valid: bool
    errors: List[str]

    @staticmethod
    def good() -> HeroValidationResult:
        return HeroValidationResult(valid=True, errors=[])

    @staticmethod
    def bad(errors: List[str]) -> HeroValidationResult:
        return HeroValidationResult(valid=False, errors=errors)
