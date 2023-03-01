import unittest

from parameterized import parameterized

from app.models import Hero
from app.models.rulebook import Rulebook
from app.service import HeroService


class TestHeroService(unittest.TestCase):
    service = HeroService()

    @parameterized.expand([
        (0, 'Elf', 'Auelfen'),
        (1, 'Elf', 'Andergaster'),
        (0, 'Mensch', 'Andergaster'),
        (1, 'Mensch', 'Ambosszwerge'),
        (0, 'Zwerg', 'Ambosszwerge'),
        (1, 'Zwerg', 'Auelfen'),
    ])
    def test_validation(self, error_count: int, species: str, culture: str):
        # given:
        rulebooks = [Rulebook.DSA5]
        held = Hero(name='Test', species=species, culture=culture)
        # when:
        errors = self.service.validate(held, rulebooks)
        # then:
        self.assertIs(len(errors), error_count)


if __name__ == '__main__':
    unittest.main()
