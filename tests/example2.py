import unittest

from clingo import Control
from clingo import SolveResult
from clingo import String
from clingo import Symbol
from pydantic import BaseModel


class Held(BaseModel):
    spezies: str
    kultur: str

    def _spezies(self) -> Symbol:
        return String(self.spezies)

    def _kultur(self) -> Symbol:
        return String(self.kultur)


class Regelwerk:

    def check(self, held: Held) -> bool:
        ctl = Control()
        ctl.load('dsa5.lp')
        ctl.ground(context=held)
        result: SolveResult = ctl.solve(on_model=lambda m: print(m))
        return result.satisfiable


class TestRegelwerk(unittest.TestCase):
    def test_check_kultur(self):
        held = Held(
            spezies='Zwerg',
            kultur='aaaaaa',
        )
        regelwerk = Regelwerk()
        result = regelwerk.check(held)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
