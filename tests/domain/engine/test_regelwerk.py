import unittest

from app.models import Held
from app.models.feature import Feature
from app.service import RegelEngine
from app.service.regelwerk import Regelwerk


class TestRegelwerk(unittest.TestCase):
    def test_check_kultur(self):
        held = Held(
            name='Test',
            spezies='Mensch',
            kultur='Nordaventurier',
        )
        engine = RegelEngine([Regelwerk.DSA5])
        result = engine.check(held, True)
        self.assertTrue(result)

    def test_list(self):
        engine = RegelEngine([Regelwerk.DSA5, Regelwerk.DSA5_EXPANSION])
        spezies = engine.list(Feature.Spezies)
        print(f"{len(spezies)} Spezies: {spezies}")
        kulturen = engine.list(Feature.Kultur)
        print(f"{len(kulturen)} Kulturen: {kulturen}")


if __name__ == '__main__':
    unittest.main()
