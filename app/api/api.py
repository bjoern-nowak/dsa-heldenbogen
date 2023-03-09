from fastapi import APIRouter

from app.api.endpoints import hero
from app.api.endpoints import meta

router = APIRouter()

router.include_router(meta.router, prefix='/meta', tags=['meta'])
router.include_router(hero.router, prefix='/hero', tags=['hero'])
