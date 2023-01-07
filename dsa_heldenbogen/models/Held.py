from typing import TypedDict

from pydantic import BaseModel
from pydantic import NonNegativeInt

from .Basiswert import Basiswert
from .Eigenschaft import Eigenschaft
from .Fertigkeit import Fertigkeit
from .Kultur import Kultur
from .Nachteil import Nachteil
from .Profession import Profession
from .Spezie import Spezie
from .Vorteil import Vorteil


#
# Meta-Daten für typisierung
#

class _Eigenschaften(TypedDict):
    name: Eigenschaft
    stufe: int


class _Fertigkeiten(TypedDict):
    id: int
    merkmal: Fertigkeit


class _Vorteile(TypedDict):
    id: int
    merkmal: Vorteil


class _Nachteile(TypedDict):
    id: int
    merkmal: Nachteil


class _Basiswerte(TypedDict):
    name: Basiswert
    wert: int


#
# Eigentliche Klasse
#

class Held(BaseModel):
    name: str

    spezies: Spezie
    kultur: Kultur
    profession: Profession
    eigenschaften: _Eigenschaften = {
        Eigenschaft.Mut: 10,
        Eigenschaft.Klugheit: 10,
        Eigenschaft.Intuition: 10,
        Eigenschaft.Charisma: 10,
        Eigenschaft.Fingerfertigkeit: 10,
        Eigenschaft.Gewandtheit: 10,
        Eigenschaft.Konstitution: 10,
        Eigenschaft.Körperkraft: 10,
    }
    fertigkeiten: _Fertigkeiten
    vorteile: _Vorteile
    nachteile: _Nachteile

    basiswerte: _Basiswerte = {
        Basiswert.Lebensenergie: 100,
        Basiswert.Astralenergie: 100,
        Basiswert.Karmaenergie: 100,
        Basiswert.Seelenkraft: 100,
        Basiswert.Zähigkeit: 100,
        Basiswert.Ausweichen: 100,
        Basiswert.Initiative: 100,
        Basiswert.Geschwindigkeit: 100,
    }

    verbrauchteAP: NonNegativeInt
    ap: NonNegativeInt
