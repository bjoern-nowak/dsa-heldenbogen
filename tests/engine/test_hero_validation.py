import unittest

from parameterized import parameterized

from app.engine.engine import Engine
from app.models.hero import Hero
from app.models.rulebook import Rulebook


class TestHeroValidation(unittest.TestCase):

    @parameterized.expand([
        (0, 'Elfen'),
        (1, '',),
        (1, '_invalid_'),
    ])
    def test_species_usable(self, error_count: int, species: str):
        # given:
        engine = Engine(Rulebook.list_by(['dsa5']))
        hero = Hero(name="name", species=species, culture='Auelfen', profession='Händler', talents={}, combat_techniques={})
        # when:
        errors = engine.validate(hero)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    @parameterized.expand([
        (0, 'Elfen', 'Auelfen'),
        (1, 'Elfen', ''),
        (1, 'Elfen', '_invalid_'),
        (1, 'Elfen', 'Menschlichekultur'),
    ])
    def test_culture_usable(self, error_count: int, species: str, culture: str):
        # given:
        engine = Engine(Rulebook.list_by(['dsa5']))
        hero = Hero(name="name", species=species, culture=culture, profession='Händler', talents={}, combat_techniques={})
        # when:
        errors = engine.validate(hero)
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
        engine = Engine(Rulebook.list_by(['dsa5']))
        hero = Hero(name="name", species=species, culture=culture, profession=profession, talents={}, combat_techniques={})
        # when:
        errors = engine.validate(hero)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    # @parameterized.expand([
    #     (0, 'Mensch', 'Menschlichekultur', 'Händler', {}, {}),
    #     (1, 'Mensch', 'Menschlichekultur', 'Söldner', {}, {}),
    #     (0, 'Mensch', 'Menschlichekultur', 'Söldner',
    #      {"Körperbeherrschung": 3, "Kraftakt": 3, "Selbstbeherrschung": 4, "Zechen": 5, "Menschenkenntnis": 3, "Überreden": 3,
    #       "Orientierung": 4, "Wildnisleben": 3, "Götter & Kulte": 3, "Kriegskunst": 6, "Sagen & Legenden": 5, "Handel": 3,
    #       "Heilkunde Wunden": 4},
    #      {"Armbrüste": 10, "Raufen": 10, "Stangenwaffen": 9, "Zweihandschwerter": 10}
    #      ),
    # ])
    # def test_profession_requirements_met(self,
    #                                      error_count: int,
    #                                      species: str,
    #                                      culture: str,
    #                                      profession: str,
    #                                      talents: dict[str, int],
    #                                      combat_techniques: dict[str, int]):
    #     # given:
    #     engine = Engine(Rulebook.list_by(['dsa5']))
    #     hero = Hero(name="name",
    #                 species=species,
    #                 culture=culture,
    #                 profession=profession,
    #                 talents=talents,
    #                 combat_techniques=combat_techniques)
    #     # when:
    #     errors = engine.validate(hero)
    #     # then:
    #     self.assertIs(error_count, len(errors), msg=errors)


if __name__ == '__main__':
    unittest.main()
