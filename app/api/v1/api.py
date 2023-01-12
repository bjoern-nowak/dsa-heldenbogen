from fastapi import APIRouter

from app.api.v1.endpoints import held
from app.api.v1.endpoints import root

router = APIRouter()
router.include_router(root.router, tags=["v1_root"])
router.include_router(held.router, prefix="/held", tags=["v1_held"])
