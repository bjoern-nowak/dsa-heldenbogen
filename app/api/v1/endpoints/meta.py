from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema.server_fehler import ServerFehler
from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.service import RegelEngine

router = APIRouter()


@router.get(
    "/list",
    description="Get list of possible values for a feature under given context (like active rulebooks).",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "model": ServerFehler,
            "description": "Bei unerwarteten Fehlern."
        }
    }
)
def list_feature(feature: Feature, rulebooks: List[Rulebook] = Query()) -> List[str]:
    try:
        return RegelEngine(rulebooks).list(feature)
    except Exception as e:
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail={
                "type": type(e).__name__,
                "message": f"{e}"}
        )
