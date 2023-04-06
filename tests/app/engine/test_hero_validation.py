from contextlib import nullcontext

from parameterized import parameterized

from src.app.engine.engine import Engine
from src.app.engine.exceptions import HeroInvalidError
from src.app.models.hero import Hero
from src.app.models.rulebook import Rulebook
from tests.base_test_case import BaseTestCase


class TestHeroValidation(BaseTestCase):

    @parameterized.expand([
        (0, 'Mensch'),
        (1, '',),
        (1, '_invalid_'),
    ])
    def test_race_usable(self, error_count: int, race: str):
        # given:
        engine = Engine(Rulebook.map(['dsa5']))
        hero = Hero(name="name",
                    experience_level='Average',
                    race=race,
                    culture='Aranier',
                    profession='Händler',
                    talents=[],
                    combat_techniques=[],
                    advantages=[],
                    disadvantages=[],
                    )
        # when:
        with self.assertRaises(HeroInvalidError) if error_count > 0 else nullcontext() as ctx:
            engine.validate(hero)
        # then:
        if ctx and ctx.exception:
            self.assertIs(error_count, len(ctx.exception.errors), msg=ctx.exception.errors)

    @parameterized.expand([
        (0, 'Mensch', 'Aranier'),
        (1, 'Mensch', ''),
        (1, 'Mensch', '_invalid_'),
        (1, 'Mensch', 'Erzzwerge'),
    ])
    def test_culture_usable(self, error_count: int, race: str, culture: str):
        # given:
        engine = Engine(Rulebook.map(['dsa5']))
        hero = Hero(name="name",
                    experience_level='Average',
                    race=race,
                    culture=culture,
                    profession='Händler',
                    talents=[],
                    combat_techniques=[],
                    advantages=[],
                    disadvantages=[],
                    )
        # when:
        with self.assertRaises(HeroInvalidError) if error_count > 0 else nullcontext() as ctx:
            engine.validate(hero)
        # then:
        if ctx and ctx.exception:
            self.assertIs(error_count, len(ctx.exception.errors), msg=ctx.exception.errors)

    @parameterized.expand([
        (0, 'Mensch', 'Menschlichekultur', 'Händler'),
        (1, 'Mensch', 'Menschlichekultur', ''),
        (1, 'Mensch', 'Menschlichekultur', '_invalid_'),
        (1, 'Mensch', 'Menschlichekultur', 'Zauberweber'),
    ])
    def test_profession_usable(self, error_count: int, race: str, culture: str, profession: str):
        # given:
        engine = Engine(Rulebook.map(['dsa5']))
        hero = Hero(name="name",
                    experience_level='Average',
                    race=race,
                    culture=culture,
                    profession=profession,
                    talents=[],
                    combat_techniques=[],
                    advantages=[],
                    disadvantages=[],
                    )
        # when:
        with self.assertRaises(HeroInvalidError) if error_count > 0 else nullcontext() as ctx:
            engine.validate(hero)
        # then:
        if ctx and ctx.exception:
            self.assertIs(error_count, len(ctx.exception.errors), msg=ctx.exception.errors)

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
    #                                      race: str,
    #                                      culture: str,
    #                                      profession: str,
    #                                      talents: dict[str, int],
    #                                      combat_techniques: dict[str, int]):
    #     # given:
    #     engine = Engine(Rulebook.list_by(['dsa5']))
    #     hero = Hero(name="name",
    #                 race=race,
    #                 culture=culture,
    #                 profession=profession,
    #                 talents=talents,
    #                 combat_techniques=combat_techniques)
    #     # when:
    #     errors = engine.validate(hero)
    #     # then:
    #     self.assertIs(error_count, len(errors), msg=errors)
