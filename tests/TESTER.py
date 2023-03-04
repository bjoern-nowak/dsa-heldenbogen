import unittest

from clingo import Model
from clingo.control import Control


class ClingoTester(unittest.TestCase):
    def test_asp(self):
        ctl = Control()
        ctl.load("TESTER.lp")
        ctl.ground()
        print(ctl.solve(on_model=self.on_model))

    def on_model(self, m: Model):
        print(m)


if __name__ == '__main__':
    unittest.main()