from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt


class Vorteil(BaseModel):
    id: int
    name: str
    stufen: PositiveInt = 1
    beschreibung: str
    voraussetzung: str
    kosten: PositiveInt = Field(description='in Abenteuerpunkte')
    reichweite: Optional[str]
