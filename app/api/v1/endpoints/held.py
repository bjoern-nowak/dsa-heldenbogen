from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema.server_fehler import ServerFehler
from app.models import Held
from app.models.rulebook import Rulebook
from app.service import RegelEngine

router = APIRouter()


@router.post(
    "/validate",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "model": ServerFehler,
            "description": "Bei unerwarteten Fehlern."
        }
    }
)
def validate(held: Held, rulebooks: List[Rulebook] = Query()) -> bool:
    try:
        return RegelEngine(rulebooks).check(held)
    except Exception as e:
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail={
                "type": type(e).__name__,
                "message": f"{e}"}
        )
