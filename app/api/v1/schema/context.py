from typing import List

from app.models import BaseModel
from app.service import RegelSet


class Context(BaseModel):
    regelsets: List[RegelSet]
