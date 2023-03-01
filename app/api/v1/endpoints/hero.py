from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema import HeroValidationResult
from app.api.v1.schema import ServerError
from app.models import Hero
from app.models import Rulebook
from app.service import HeroService

router = APIRouter()


@router.post(
    "/validate",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "model": ServerError,
            "description": "Unexpected server error"
        }
    }
)
def validate(hero: Hero, rulebooks: List[Rulebook] = Query()) -> HeroValidationResult:
    try:
        errors: List[str] = HeroService().validate(hero, rulebooks)
        if errors:
            return HeroValidationResult.bad(errors=errors)
        else:
            return HeroValidationResult.good()
    except Exception as e:
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
