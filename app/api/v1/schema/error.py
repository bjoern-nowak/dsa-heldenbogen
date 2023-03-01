from __future__ import annotations  # required till PEP 563

from app.models import BaseModel


class ExceptionDetails(BaseModel):
    type: str
    message: str


class ServerError(BaseModel):
    detail: str | ExceptionDetails

    @staticmethod
    def by(e: Exception) -> ServerError:
        return ServerError(detail=ExceptionDetails(type=type(e).__name__, message=f"{e}"))


class ClientError(BaseModel):
    detail: str | ExceptionDetails

    @staticmethod
    def by(e: Exception) -> ClientError:
        return ClientError(detail=ExceptionDetails(type=type(e).__name__, message=f"{e}"))
