from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from app.api.v1.schema.held import Held
from app.engine import RegelSet
from app.engine import Regelwerk

router = APIRouter()


@router.post("/validate")
def validate(held: Held) -> Held:
    regelwerk = Regelwerk([RegelSet.DSA5_GRUND, RegelSet.DSA5_OPTIONAL])
    is_valid = regelwerk.check(held.to_model())
    if is_valid is True:
        return held
    elif is_valid is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Held konnte nicht geprüft werden.")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Held ist invalide.")
