import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.api.schemas.errors import ClientError
from app.api.schemas.errors import ServerError
from app.api.schemas.hero import Hero
from app.api.schemas.hero_validation_result import HeroValidationResult
from app.engine.exceptions import HeroInvalidError
from app.models.hero_validation_warning import HeroValidationWarning
from app.models.rulebook import Rulebook
from app.models.rulebook import UnknownRulebookError
from app.services.hero_service import HeroService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    '/validate',
    description="Validates hero against given rulebooks.",
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
def validate(hero: Hero, rulebooks: List[str] = Query(example=['dsa5'])) -> HeroValidationResult:
    try:
        logger.trace(f"(Request) validate\nrulebooks {rulebooks}\nhero: {hero}")
        warnings: List[HeroValidationWarning] = HeroService().validate(hero.to_model(), Rulebook.map(rulebooks))
        return HeroValidationResult.passed(warnings)
    except HeroInvalidError as e:
        return HeroValidationResult.failed(e.errors, e.warnings)
    except UnknownRulebookError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=ClientError.by(e)
        )


@router.post(
    '/save',
    description="Save hero as new or whenever given hero name exists for user override it.",
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
def save(hero: Hero, rulebooks: List[str] = Query(example=['dsa5'])):
    try:
        logger.trace(f"(Request) save\nrulebooks {rulebooks}\nhero: {hero}")
        HeroService().save(hero.to_model(), Rulebook.map(rulebooks))
    except UnknownRulebookError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=ClientError.by(e)
        )


@router.get(
    '/export',
    description="Export hero of user by given hero name.",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def export(hero_name: str):
    logger.trace(f"(Request) export hero with name '{hero_name}' of user ''")
    HeroService().export(hero_name)


@router.delete(
    '/delete',
    description="Delete hero of user by given hero name.",
    responses={
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def delete(hero_name: str):
    logger.trace(f"(Request) delete hero with name '{hero_name}' of user ''")
    HeroService().delete(hero_name)
