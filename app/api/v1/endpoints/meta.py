import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.v1.schema import ClientError
from app.api.v1.schema import ServerError
from app.engine.exceptions import UnusableRulebookError
from app.models import Feature
from app.models import Rulebook
from app.service import MetaService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    '/list',
    description="Get list of possible values for a feature under given context (like active rulebooks).",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def list_feature(feature: Feature, rulebooks: List[Rulebook] = Query()) -> List[str] | ClientError:
    try:
        logger.trace(f"(Request) feature value list\nrulebooks: {rulebooks}\nfeature: {feature}")
        return MetaService().list(feature, rulebooks)
    except UnusableRulebookError as e:
        return ClientError.by(e)
    except Exception as e:
        logger.exception("Some exception occurred.")
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
