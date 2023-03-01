from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema.error import ClientError
from app.api.v1.schema.error import ServerError
from app.engine.clingo_engine import UnusableRulebookError
from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.service import RuleEngine

router = APIRouter()


@router.get(
    "/list",
    description="Get list of possible values for a feature under given context (like active rulebooks).",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "model": ServerError,
            "description": "Unexpected server error"
        }
    }
)
def list_feature(feature: Feature, rulebooks: List[Rulebook] = Query()) -> List[str] | ClientError:
    try:
        return RuleEngine(rulebooks).list(feature)
    except UnusableRulebookError as e:
        return ClientError.by(e)
    except Exception as e:
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
