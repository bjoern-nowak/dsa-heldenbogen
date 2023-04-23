from __future__ import annotations  # required till PEP 563

from fastapi.encoders import jsonable_encoder

from dsaheldenbogen.app.models.base_model import BaseModel


# reason for 'jsonable_encoder': nested models, see
# https://stackoverflow.com/questions/72092365/fastapi-using-nested-model-gives-json-serialization-error

class BaseError(BaseModel):
    type: str
    message: str
    details: dict


class ServerError(BaseError):

    @staticmethod
    def by(ex: Exception) -> ServerError:
        return jsonable_encoder(ServerError(type=type(ex).__name__, message=f"{ex}", details=vars(ex)))


class ClientError(BaseError):

    @staticmethod
    def by(ex: Exception) -> ClientError:
        return jsonable_encoder(ClientError(type=type(ex).__name__, message=f"{ex}", details=vars(ex)))
