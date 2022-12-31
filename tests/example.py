import unittest
from clingo.symbol import Number
from clingo.control import Control


class Context:
    def inc(self, x):
        return Number(x.number + 1)

    def seq(self, x, y):
        return [x, y]


class ClingoExample(unittest.TestCase):
    def test_asp(self):
        ctl = Control()
        ctl.load("example.lp")
        ctl.ground([("base", [])], context=Context())
        print(ctl.solve(on_model=self.__on_model))

    def __on_model(self, m):
        print(m)


if __name__ == '__main__':
    unittest.main()






