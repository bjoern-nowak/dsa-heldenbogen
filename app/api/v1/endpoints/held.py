from http import HTTPStatus

from fastapi import APIRouter
from fastapi import HTTPException

from app.api.v1.schema.context import Context
from app.api.v1.schema.server_fehler import ServerFehler
from app.models import Held
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
def validate(held: Held, context: Context) -> bool:
    is_valid = RegelEngine(context.regelsets).check(held)
    if is_valid is None:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Held konnte nicht geprüft werden.")
    return is_valid
