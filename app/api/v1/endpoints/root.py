from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index() -> str:
    return "This is the API v1."
