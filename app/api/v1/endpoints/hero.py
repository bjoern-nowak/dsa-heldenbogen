import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema import HeroValidationResult
from app.api.v1.schema import ServerError
from app.engine.exceptions import HeroInvalidError
from app.models import Hero
from app.models import Rulebook
from app.service import HeroService

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
        HeroService().validate(hero, rulebooks)
        return HeroValidationResult.passed()
    except HeroInvalidError as e:
        return HeroValidationResult.failed(errors=e.errors)
    except Exception as e:
        logger.exception("Some exception occurred.")
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
