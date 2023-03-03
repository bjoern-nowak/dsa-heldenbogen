import unittest

from parameterized import parameterized

from app.models import Hero
from app.models.rulebook import Rulebook
from app.service import HeroService


class TestHeroService(unittest.TestCase):
    service = HeroService()

    @parameterized.expand([
        (0, 'Elf', 'Auelfen', 'Söldner'),
        (0, 'Elf', 'Auelfen', 'Zauberweber'),
        (1, 'Elf', 'Andergaster', 'Söldner'),
        (1, 'Elf', 'Ambosszwerge', 'Söldner'),

        (0, 'Mensch', 'Andergaster', 'Söldner'),
        (1, 'Mensch', 'Auelfen', 'Söldner'),
        (1, 'Mensch', 'Andergaster', 'Zauberweber'),
        (1, 'Mensch', 'Ambosszwerge', 'Söldner'),

        (0, 'Zwerg', 'Ambosszwerge', 'Söldner'),
        (1, 'Zwerg', 'Auelfen', 'Söldner'),
        (1, 'Zwerg', 'Ambosszwerge', 'Zauberweber'),
        (1, 'Zwerg', 'Andergaster', 'Söldner'),
    ])
    def test_validation(self,
                        error_count: int,
                        species: str,
                        culture: str,
                        profession: str,
                        # characteristics: dict[Characteristic, NonNegativeInt],
                        # skill: dict[str, NonNegativeInt],
                        # advantages: List[str],
                        # disadvantages: List[str],
                        ):
        # given:
        rulebooks = [Rulebook.DSA5]
        held = Hero(name='Test',
                    species=species,
                    culture=culture,
                    profession=profession,
                    # characteristics=characteristics,
                    # skill=skill,
                    # advantages=advantages,
                    # disadvantages=disadvantages,
                    )
        # when:
        errors = self.service.validate(held, rulebooks)
        # then:
        self.assertIs(len(errors), error_count, msg=errors)


if __name__ == '__main__':
    unittest.main()
