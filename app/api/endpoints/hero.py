import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.schema.errors import ServerError
from app.api.schema.hero import Hero
from app.api.schema.validation_result import HeroValidationResult
from app.engine.exceptions import HeroInvalidError
from app.engine.hero_validation_warning import HeroValidationWarning
from app.models.rulebook import Rulebook
from app.service.hero_service import HeroService

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
def validate(hero: Hero, rulebooks: List[Rulebook] = Query()) -> HeroValidationResult:
    try:
        logger.trace(f"(Request) validate\nrulebooks {rulebooks}\nhero: {hero}")
        warnings: List[HeroValidationWarning] = HeroService().validate(hero.to_model(), rulebooks)
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
