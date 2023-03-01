import unittest

from clingo import Control
from clingo import SolveResult
from clingo import String
from clingo import Symbol
from pydantic import BaseModel


class Held(BaseModel):
    species: str
    culture: str

    def _species(self) -> Symbol:
        return String(self.species)

    def _culture(self) -> Symbol:
        return String(self.culture)


class Regelwerk:

    def check(self, held: Held) -> bool:
        ctl = Control()
        ctl.load('example2.lp')
        ctl.ground(context=held)
        result: SolveResult = ctl.solve(on_model=lambda m: print(m))
        return result.satisfiable


class TestRegelwerk(unittest.TestCase):
    def test_check_culture(self):
        held = Held(
            species='Zwerg',
            culture='aaaaaa',
        )
        regelwerk = Regelwerk()
        result = regelwerk.check(held)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
