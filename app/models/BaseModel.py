from pydantic import BaseModel as PydanticBaseModel
from pydantic import Extra


class BaseModel(PydanticBaseModel):
    class Config:
        extra = Extra.forbid  # Does not allow additional non-model attributes
        validate_all = True  # also validate defaults
        use_enum_values = False  # use <enum>.value property instead of raw enum (for serialization)
        validate_assignment = True  # validate on attributes assignment
        underscore_attrs_are_private = True  # treat _<attr> as private
