from clingo.control import Control
from clingo.symbol import Number


class Context:
    def inc(self, x):
        return Number(x.number + 1)

    def seq(self, x, y):
        return [x, y]


class ClingoContextExample:
    def test_asp(self):
        ctl = Control()
        ctl.load('clingo_context.lp')
        ctl.ground([('base', [])], context=Context())
        print(ctl.solve(on_model=self._on_model))

    def _on_model(self, m):
        print(m)


if __name__ == '__main__':
    ClingoContextExample().test_asp()
