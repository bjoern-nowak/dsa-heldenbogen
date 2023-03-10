from app.models.base_enum import BaseEnum
from app.models.base_model import BaseModel


class HeroValidationWarning(BaseModel):
    """
    Represents a single hero validation warning.

    Field 'message' uses single quote for used 'parameters'
    Field 'parameters' contains relevant evaluable data. May not all are used in 'message'.
    """

    class Type(str, BaseEnum):
        MISSING_USUAL = 'missing_usual'
        MISSING_TYPICAL = 'missing_typical'
        ATYPICAL = 'atypical'

    type: Type
    message: str
    parameter: dict[str, str]

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
