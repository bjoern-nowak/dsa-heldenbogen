import unittest

from app.models import Hero
from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.service import RuleEngine


class TestRegelwerk(unittest.TestCase):
    def test_check_culture(self):
        held = Hero(
            name='Test',
            species='Mensch',
            culture='Nordaventurier',
        )
        engine = RuleEngine([Rulebook.DSA5])
        result = engine.check(held, True)
        self.assertTrue(result)

    def test_list(self):
        engine = RuleEngine([Rulebook.DSA5, Rulebook.DSA5_EXPANSION])
        species = engine.list(Feature.SPECIES)
        print(f"{len(species)} Species: {species}")
        cultures = engine.list(Feature.CULTURE)
        print(f"{len(cultures)} Cultures: {cultures}")


if __name__ == '__main__':
    unittest.main()
