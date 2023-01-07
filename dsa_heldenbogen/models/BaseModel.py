# u.s. Code, bis auf die Kommentare, stammen von Jacob Hayes (https://github.com/JacobHayes)
# Quelle: https://github.com/pydantic/pydantic/issues/418#issuecomment-974980947
# aufgerufen am 04.01.2023

from typing import Any
from typing import TypeVar

from pydantic import BaseModel as PydanticBaseModel

_BaseModel = TypeVar("_BaseModel", bound="BaseModel")


class BaseModel(PydanticBaseModel):
    """
    This class extends the actual pydantic BaseModel.
    It allows pydantic validation on copy
    """

    def copy(self: _BaseModel, *, validate: bool = True, **kwargs: Any) -> _BaseModel:
        copy = super().copy(**kwargs)
        if validate:
            return self.validate(
                dict(copy._iter(to_dict=False, by_alias=False, exclude_unset=True))
            )
        return copy
