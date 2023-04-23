import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from dsaheldenbogen.api.schemas.exceptions import ClientError
from dsaheldenbogen.api.schemas.exceptions import ServerError
from dsaheldenbogen.app.engine.exceptions import UnusableRulebookError
from dsaheldenbogen.app.models.exceptions import UnknownRulebookError
from dsaheldenbogen.app.models.feature import Feature
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.services.meta_service import MetaService

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
    logger.trace("(Request) list available rulebooks")
    return [r.name for r in MetaService().list_usable_rulebooks()]


@router.get(
    '/feature/list',
    description="Get list of possible values for a feature under given context (like active rulebooks).",
    responses={
        HTTPStatus.BAD_REQUEST: {
            'model': ClientError,
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def list_known_feature_values(
        feature: Feature,
        rulebooks: List[str] = Query(example=['dsa5'])) -> List[tuple[str, str, int]] | List[str]:
    try:
        logger.trace(f"(Request) list feature value\nrulebooks: {rulebooks}\nfeature: {feature}")
        return MetaService().list_known_feature_values(feature, Rulebook.map(rulebooks))
    except UnusableRulebookError as ex:
        # pylint: disable-next=raise-missing-from
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=ServerError.by(ex)
        )
    except UnknownRulebookError as ex:
        # pylint: disable-next=raise-missing-from
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=ClientError.by(ex)
        )
