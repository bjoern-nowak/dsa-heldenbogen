from app.models.base_model import BaseModel


class Skill(BaseModel):
    name: str
    level: int
