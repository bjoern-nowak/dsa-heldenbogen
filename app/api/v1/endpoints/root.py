from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/")
def index():
    # TODO we shall not must use the api prefix manually
    return RedirectResponse(url='/api/v1/docs')
