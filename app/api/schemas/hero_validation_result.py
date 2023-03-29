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

    class Config:
        schema_extra = {
            "examples": {
                "valid_with_warnings": {
                    "summary": "[VALID] OK but having warnings",
                    "value": {
                        "valid": True,
                        "errors": [],
                        "warnings": [
                            {
                                "type": "missing_typical",
                                "message": "Heros 'race' is missing typical 'advantage' of 'Schlangenmensch' using '' at level '1'.",
                                "parameter": {
                                    "caused_feature": "race",
                                    "caused_feature_value": "Elfen",
                                    "referred_feature": "advantage",
                                    "referred_feature_value": "Schlangenmensch",
                                    "referred_feature_level": 1,
                                    "referred_feature_using": ""
                                }
                            },
                            {
                                "type": "missing_typical",
                                "message": "Heros 'race' is missing typical 'advantage' of 'Verbesserte Regeneration' using 'Astralenergie' at level '1'.",
                                "parameter": {
                                    "caused_feature": "race",
                                    "caused_feature_value": "Elfen",
                                    "referred_feature": "advantage",
                                    "referred_feature_value": "Verbesserte Regeneration",
                                    "referred_feature_level": 1,
                                    "referred_feature_using": "Astralenergie"
                                }
                            },
                        ]
                    }
                },
                "invalid_unknown_value": {
                    "summary": "[INVALID] Unknown race value",
                    "value": {
                        "valid": False,
                        "errors": [
                            {
                                "type": "unknown",
                                "addon": None,
                                "message": "Heros 'profession' value of 'Söldnera' is not known.",
                                "parameter": {
                                    "caused_feature": "profession",
                                    "caused_feature_value": "Söldnera"
                                }
                            }
                        ],
                        "warnings": []
                    }
                },
                "invalid_missing_level": {
                    "summary": "[INVALID] Talent not an required minimum level",
                    "value": {
                        "valid": False,
                        "errors": [
                            {
                                "type": "missing_level",
                                "addon": None,
                                "message": "Heros 'profession' is missing minimum level '3' for 'talent' of 'Körperbeherrschung'.",
                                "parameter": {
                                    "caused_feature": "profession",
                                    "caused_feature_value": "Söldner",
                                    "referred_feature": "talent",
                                    "referred_feature_value": "Körperbeherrschung",
                                    "min_level": 3
                                }
                            }
                        ],
                        "warnings": []
                    }
                }
            }
        }
