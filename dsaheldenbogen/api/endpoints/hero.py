import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter
from fastapi import Body
from fastapi import HTTPException
from fastapi import Query

from dsaheldenbogen.api.schemas.exceptions import ClientError
from dsaheldenbogen.api.schemas.exceptions import ServerError
from dsaheldenbogen.api.schemas.hero import Hero
from dsaheldenbogen.api.schemas.hero_validation_result import HeroValidationResult
from dsaheldenbogen.app.engine.exceptions import HeroInvalidError
from dsaheldenbogen.app.models.exceptions import UnknownRulebookError
from dsaheldenbogen.app.models.hero_validation_warning import HeroValidationWarning
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.services.hero_service import HeroService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    '/validate',
    description="Validates hero against given rulebooks.",
    responses={
        HTTPStatus.OK: {
            'content': {
                'application/json': {
                    'examples': HeroValidationResult.Config.schema_extra["examples"]
                }
            },
        },
        HTTPStatus.BAD_REQUEST: {
            'model': ClientError,
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'model': ServerError,
            'description': "Unexpected server error"
        }
    }
)
def validate(hero: Hero = Body(examples=Hero.Config.schema_extra["examples"]),
             rulebooks: List[str] = Query(example=['dsa5'])) -> HeroValidationResult:
    try:
        logger.trace(f"(Request) validate\nrulebooks {rulebooks}\nhero: {hero}")
        warnings: List[HeroValidationWarning] = HeroService().validate(hero.to_model(), Rulebook.map(rulebooks))
        return HeroValidationResult.passed(warnings)
    except HeroInvalidError as ex:
        return HeroValidationResult.failed(ex.errors, ex.warnings)
    except UnknownRulebookError as ex:
        # pylint: disable-next=raise-missing-from
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=ClientError.by(ex)
        )


@router.put(
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
    except UnknownRulebookError as ex:
        # pylint: disable-next=raise-missing-from
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=ClientError.by(ex)
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
