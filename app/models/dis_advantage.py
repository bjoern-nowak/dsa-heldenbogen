from app.models.base_model import BaseModel


class DisAdvantage(BaseModel):
    """
    Field 'uses' can be empty (meant to be optional)
    TODO make field 'uses' truly optional, handling "None" somewhere
    """
    name: str
    uses: str
    level: int
