from app.models import BaseModel
from app.models import Held as AppHeld


class Held(BaseModel):
    spezies: str
    kultur: str

    def to_model(self) -> AppHeld:
        return AppHeld(
            spezies=self.spezies,
            kultur=self.kultur,
        )
