from __future__ import annotations  # required till PEP 563

from typing import Callable

from clingo import String
from clingo import Symbol

from app.models import Held


class ClingoHeld(Held):
    # redefine fields to make them callable for clingo
    spezies: Callable[[], Symbol]
    kultur: Callable[[], Symbol]

    @classmethod
    def wrap(cls, held: Held) -> ClingoHeld:
        return ClingoHeld(
            spezies=lambda: String(held.spezies),
            kultur=lambda: String(held.kultur)
        )
