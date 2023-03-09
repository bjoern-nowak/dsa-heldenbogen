import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import Body
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema import HeroValidationResult
from app.api.v1.schema import ServerError
from app.engine.exceptions import HeroInvalidError
from app.engine.hero_validation_warning import HeroValidationWarning
from app.models import Hero
from app.models import Rulebook
from app.service import HeroService

logger = logging.getLogger(__name__)
router = APIRouter()

HERO_EXAMPLE = {
    "name": "UncleBob",
    "species": "Elfen",
    "culture": "Auelfen",
    "profession": "Söldner",
    "talents": {"Körperbeherrschung": 3, "Kraftakt": 3, "Selbstbeherrschung": 4, "Zechen": 5, "Menschenkenntnis": 3,
                "Überreden": 3, "Orientierung": 4, "Wildnisleben": 3, "Götter & Kulte": 3, "Kriegskunst": 6,
                "Sagen & Legenden": 5, "Handel": 3, "Heilkunde Wunden": 4},
    "combat_techniques": {"Armbrüste": 10, "Raufen": 10, "Stangenwaffen": 9, "Zweihandschwerter": 10},
    "advantages": [("Begabung", "Singen", 1), ("Begabung", "Musizieren", 1), ("Beidhändig", "", 1),
                   ("Dunkelsicht", "", 2)],
    "disadvantages": [("Körpergebundene Kraft", "", 1), ("Lästige Mindergeister", "", 1), ("Wahrer Name", "", 1),
                      ("Blutrausch", "", 1)]
}


@router.post(
    '/validate',
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def validate(hero: Hero = Body(example=HERO_EXAMPLE), rulebooks: List[Rulebook] = Query()) -> HeroValidationResult:
    try:
        logger.trace(f"(Request) validate\nrulebooks {rulebooks}\nhero: {hero}")
        warnings: List[HeroValidationWarning] = HeroService().validate(hero, rulebooks)
        return HeroValidationResult.passed(warnings)
    except HeroInvalidError as e:
        return HeroValidationResult.failed(e.errors, e.warnings)
    except Exception as e:
        logger.exception("Some exception occurred.")
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
