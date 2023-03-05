import unittest

from parameterized import parameterized

from app.models import Hero
from app.models.rulebook import Rulebook
from app.service import HeroService


class TestHeroService(unittest.TestCase):
    service = HeroService()

    @parameterized.expand([
        (0, 'Elf', 'Auelfen', 'Händler'),
        (0, 'Elf', 'Auelfen', 'Zauberweber'),
        (1, 'Elf', 'Andergaster', 'Händler'),
        (1, 'Elf', 'Ambosszwerge', 'Händler'),

        (0, 'Mensch', 'Andergaster', 'Händler'),
        (1, 'Mensch', 'Auelfen', 'Händler'),
        (1, 'Mensch', 'Andergaster', 'Zauberweber'),
        (1, 'Mensch', 'Ambosszwerge', 'Händler'),

        (0, 'Zwerg', 'Ambosszwerge', 'Händler'),
        (1, 'Zwerg', 'Auelfen', 'Händler'),
        (1, 'Zwerg', 'Ambosszwerge', 'Zauberweber'),
        (1, 'Zwerg', 'Andergaster', 'Händler'),
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
                    talents={},
                    # advantages=advantages,
                    # disadvantages=disadvantages,
                    )
        # when:
        errors = self.service.validate(held, rulebooks)
        # then:
        self.assertIs(len(errors), error_count, msg=errors)


if __name__ == '__main__':
    unittest.main()
