from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema.error import ServerError
from app.models import Hero
from app.models.rulebook import Rulebook
from app.service import RuleEngine

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
def validate(hero: Hero, rulebooks: List[Rulebook] = Query()) -> bool:
    try:
        return RuleEngine(rulebooks).check(hero)
    except Exception as e:
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
