from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import NegativeInt
from pydantic import PositiveInt


class Nachteil(BaseModel):
    id: int
    name: str
    stufen: PositiveInt = 1
    beschreibung: str
    voraussetzung: str
    kosten: NegativeInt = Field(metadata={'unit': 'Abenteuerpunkte'})
    reichweite: Optional[str]
