import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.schemas.errors import ClientError
from app.api.schemas.errors import ServerError
from app.engine.exceptions import UnusableRulebookError
from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.services.meta_service import MetaService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    '/rulebook/list',
    description="Get list of available rulebooks.",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def list_known_rulebooks() -> List[str]:
    try:
        logger.trace(f"(Request) list available rulebooks")
        return MetaService().list_known_rulebooks()
    except Exception as e:
        logger.exception("Some exception occurred.")
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )


@router.get(
    '/feature/list',
    description="Get list of possible values for a feature under given context (like active rulebooks).",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def list_known_feature_values(feature: Feature, rulebooks: List[str] = Query(example=['dsa5'])) -> List[str] | ClientError:
    try:
        logger.trace(f"(Request) list feature value\nrulebooks: {rulebooks}\nfeature: {feature}")
        return MetaService().list_known_feature_values(feature, Rulebook.list_by(rulebooks))
    except UnusableRulebookError as e:
        # TODO this is not a client error :D
        return ClientError.by(e)
    except Exception as e:
        logger.exception("Some exception occurred.")
        # TODO [1] not a good practise to catch any error and publish its message
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(e)
        )
