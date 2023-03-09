import unittest

from parameterized import parameterized

from app.models.hero import Hero
from app.models.rulebook import Rulebook
from app.services.hero_service import HeroService


class TestHeroService(unittest.TestCase):
    service = HeroService()

    @parameterized.expand([
        (0, 'Elfen', 'Auelfen', 'Händler'),
        (0, 'Elfen', 'Auelfen', 'Wildnisläuferin'),
        (1, 'Elfen', 'Andergaster', 'Händler'),
        (1, 'Elfen', 'Ambosszwerge', 'Händler'),

        (0, 'Mensch', 'Andergaster', 'Händler'),
        (1, 'Mensch', 'Auelfen', 'Händler'),
        (1, 'Mensch', 'Andergaster', 'Wildnisläuferin'),
        (1, 'Mensch', 'Ambosszwerge', 'Händler'),

        (0, 'Zwerg', 'Ambosszwerge', 'Händler'),
        (1, 'Zwerg', 'Auelfen', 'Händler'),
        (1, 'Zwerg', 'Ambosszwerge', 'Wildnisläuferin'),
        (1, 'Zwerg', 'Andergaster', 'Händler'),
    ])
    def test_validation(self,
                        error_count: int,
                        species: str,
                        culture: str,
                        profession: str,
                        ):
        # given:
        rulebooks = [Rulebook.DSA5]
        hero = Hero(name='Test',
                    species=species,
                    culture=culture,
                    profession=profession,
                    talents={},
                    combat_techniques={},
                    advantages={},
                    disadvantages={},
                    )
        # when:
        errors = self.service.validate(hero, rulebooks)
        # then:
        self.assertIs(len(errors), error_count, msg=errors)


if __name__ == '__main__':
    unittest.main()
