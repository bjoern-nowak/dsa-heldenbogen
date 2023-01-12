from app.models import BaseModel
from app.models import Held as AppHeld


class Held(BaseModel):
    name: str

    spezies: str
    kultur: str

    def to_model(self) -> AppHeld:
        return AppHeld(
            name=self.name,
            spezies=self.spezies,
            kultur=self.kultur,
        )
