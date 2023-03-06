import unittest

from parameterized import parameterized

from app.engine import Engine
from app.models import Hero
from app.models.rulebook import Rulebook


class TestHeroValidation(unittest.TestCase):

    @parameterized.expand([
        (0, 'Elf'),
        (1, '',),
        (1, '_invalid_'),
    ])
    def test_species_usable(self, error_count: int, species: str):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species=species, culture='Auelfen', profession='Händler', talents={}, combat_techniques={})
        # when:
        errors = engine.validate(held)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    @parameterized.expand([
        (0, 'Elf', 'Auelfen'),
        (1, 'Elf', ''),
        (1, 'Elf', '_invalid_'),
        (1, 'Elf', 'Menschlichekultur'),
    ])
    def test_culture_usable(self, error_count: int, species: str, culture: str):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species=species, culture=culture, profession='Händler', talents={}, combat_techniques={})
        # when:
        errors = engine.validate(held)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    @parameterized.expand([
        (0, 'Mensch', 'Menschlichekultur', 'Händler'),
        (1, 'Mensch', 'Menschlichekultur', ''),
        (1, 'Mensch', 'Menschlichekultur', '_invalid_'),
        (1, 'Mensch', 'Menschlichekultur', 'Zauberweber'),
    ])
    def test_profession_usable(self, error_count: int, species: str, culture: str, profession: str):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species=species, culture=culture, profession=profession, talents={}, combat_techniques={})
        # when:
        errors = engine.validate(held)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)


if __name__ == '__main__':
    unittest.main()
