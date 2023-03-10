import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.schemas.errors import ServerError
from app.api.schemas.hero import Hero
from app.api.schemas.hero_validation_result import HeroValidationResult
from app.engine.exceptions import HeroInvalidError
from app.models.hero_validation_warning import HeroValidationWarning
from app.models.rulebook import Rulebook
from app.services.hero_service import HeroService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    '/validate',
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def validate(hero: Hero, rulebooks: List[str] = Query(example=['dsa5'])) -> HeroValidationResult:
    try:
        logger.trace(f"(Request) validate\nrulebooks {rulebooks}\nhero: {hero}")
        warnings: List[HeroValidationWarning] = HeroService().validate(hero.to_model(), Rulebook.list_by(rulebooks))
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
