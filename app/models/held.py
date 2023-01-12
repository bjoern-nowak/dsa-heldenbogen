from __future__ import annotations  # required till PEP 563

from app.models import BaseModel


# from typing import TYPE_CHECKING

# from pydantic import NonNegativeInt

# from .basiswert import Basiswert
# from .eigenschaft import Eigenschaft

# if TYPE_CHECKING:  # break issue of circular reference through type hints
#     from .fertigkeit import Fertigkeit
#     from .kultur import Kultur
#     from .nachteil import Nachteil
#     from .profession import Profession
#     from .spezies import Spezies
#     from .vorteil import Vorteil


class Held(BaseModel):
    name: str

    spezies: str
    kultur: str

# class Held(BaseModel):
#     name: str
#
#     spezies: Spezies
#     kultur: Kultur
#     profession: Profession
#     eigenschaften: dict[Eigenschaft, int] = {
#         Eigenschaft.MUT: 10,
#         Eigenschaft.KLUGHEIT: 10,
#         Eigenschaft.INTUITION: 10,
#         Eigenschaft.CHARISMA: 10,
#         Eigenschaft.FINGERFERTIGKEIT: 10,
#         Eigenschaft.GEWANDTHEIT: 10,
#         Eigenschaft.KONSTITUTION: 10,
#         Eigenschaft.KORPERKRAFT: 10,
#     }
#     fertigkeiten: dict[int, Fertigkeit]
#     vorteile: dict[int, Vorteil]
#     nachteile: dict[int, Nachteil]
#
#     basiswerte: dict[Basiswert, int] = {
#         Basiswert.LEBENSENERGIE: 100,
#         Basiswert.ASTRALENERGIE: 100,
#         Basiswert.KARMAENERGIE: 100,
#         Basiswert.SEELENKRAFT: 100,
#         Basiswert.ZAEHIGKEIT: 100,
#         Basiswert.AUSWEICHEN: 100,
#         Basiswert.INITIATIVE: 100,
#         Basiswert.GESCHWINDIGKEIT: 100,
#     }
#
#     verbrauchteAP: NonNegativeInt
#     ap: NonNegativeInt
#
#
# Held.update_forward_refs()
