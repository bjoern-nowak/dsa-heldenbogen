from __future__ import annotations  # required till PEP 563

from fastapi.encoders import jsonable_encoder

from app.models.basemodel import BaseModel


# reason for 'jsonable_encoder': nested models, see
# https://stackoverflow.com/questions/72092365/fastapi-using-nested-model-gives-json-serialization-error

class ExceptionDetails(BaseModel):
    type: str
    message: str


class ServerError(BaseModel):
    detail: str | ExceptionDetails

    @staticmethod
    def by(e: Exception) -> ServerError:
        return jsonable_encoder(ServerError(detail=ExceptionDetails(type=type(e).__name__, message=f"{e}")))


class ClientError(BaseModel):
    detail: str | ExceptionDetails

    @staticmethod
    def by(e: Exception) -> ClientError:
        return jsonable_encoder(ClientError(detail=ExceptionDetails(type=type(e).__name__, message=f"{e}")))
