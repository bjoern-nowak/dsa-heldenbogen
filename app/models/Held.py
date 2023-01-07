from typing import Dict

from pydantic import NonNegativeInt

from . import BaseModel
from .Basiswert import Basiswert
from .Eigenschaft import Eigenschaft
from .Fertigkeit import Fertigkeit
from .Kultur import Kultur
from .Nachteil import Nachteil
from .Profession import Profession
from .Spezies import Spezies
from .Vorteil import Vorteil


class Held(BaseModel):
    name: str

    spezies: Spezies
    kultur: Kultur
    profession: Profession
    eigenschaften: Dict[Eigenschaft, int] = {
        Eigenschaft.MUT: 10,
        Eigenschaft.KLUGHEIT: 10,
        Eigenschaft.INTUITION: 10,
        Eigenschaft.CHARISMA: 10,
        Eigenschaft.FINGERFERTIGKEIT: 10,
        Eigenschaft.GEWANDTHEIT: 10,
        Eigenschaft.KONSTITUTION: 10,
        Eigenschaft.KORPERKRAFT: 10,
    }
    fertigkeiten: Dict[int, Fertigkeit]
    vorteile: Dict[int, Vorteil]
    nachteile: Dict[int, Nachteil]

    basiswerte: Dict[Basiswert, int] = {
        Basiswert.LEBENSENERGIE: 100,
        Basiswert.ASTRALENERGIE: 100,
        Basiswert.KARMAENERGIE: 100,
        Basiswert.SEELENKRAFT: 100,
        Basiswert.ZAEHIGKEIT: 100,
        Basiswert.AUSWEICHEN: 100,
        Basiswert.INITIATIVE: 100,
        Basiswert.GESCHWINDIGKEIT: 100,
    }

    verbrauchteAP: NonNegativeInt
    ap: NonNegativeInt
