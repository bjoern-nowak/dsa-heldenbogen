from app.models import BaseModel
from app.models import Held as AppHeld
from app.models import Kultur
from app.models import Spezies


class Held(BaseModel):
    name: str

    spezies: Spezies
    kultur: Kultur

    def to_model(self) -> AppHeld:
        return AppHeld(
            name=self.name,
            spezies=self.spezies,
            kultur=self.kultur,
        )
