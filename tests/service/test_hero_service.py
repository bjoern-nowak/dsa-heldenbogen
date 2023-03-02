import unittest

from parameterized import parameterized

from app.models import Hero
from app.models.rulebook import Rulebook
from app.service import HeroService


class TestHeroService(unittest.TestCase):
    service = HeroService()

    @parameterized.expand([
        (0, 'Elf', 'Auelfen', 'Zauberweber'),
        (1, 'Elf', 'Andergaster', 'Zauberweber'),
        (0, 'Mensch', 'Andergaster', 'Zauberweber'),
        (1, 'Mensch', 'Ambosszwerge', 'Zauberweber'),
        (0, 'Zwerg', 'Ambosszwerge', 'Zauberweber'),
        (1, 'Zwerg', 'Auelfen', 'Zauberweber'),
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
        self.assertIs(len(errors), error_count)


if __name__ == '__main__':
    unittest.main()
