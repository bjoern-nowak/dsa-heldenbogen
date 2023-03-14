from contextlib import nullcontext

from parameterized import parameterized

from app.engine.exceptions import HeroInvalidError
from app.models.experience_level import ExperienceLevel
from app.models.hero import Hero
from app.models.rulebook import Rulebook
from app.services.hero_service import HeroService
from tests import heros
from tests.base_test_case import BaseTestCase


class TestHeroService(BaseTestCase):
    service = HeroService()

    @parameterized.expand([
        (0, 'Elfen', 'Auelfen', 'Händler'),
        (0, 'Elfen', 'Firnelfen', 'Wildnisläuferin'),
        (0, 'Mensch', 'Andergaster', 'Händler'),
        (1, 'Mensch', 'Andergaster', 'Wildnisläuferin'),
        (16, 'Mensch', 'Andergaster', 'Söldner'),
    ])
    def test_validation(self,
                        error_count: int,
                        species: str,
                        culture: str,
                        profession: str,
                        ):
        # given:
        rulebooks = ['dsa5']
        hero = Hero(name='Test',
                    experience_level=ExperienceLevel.AVERAGE,
                    species=species,
                    culture=culture,
                    profession=profession,
                    talents=[],
                    combat_techniques=[],
                    advantages=[],
                    disadvantages=[],
                    )
        # when:
        with self.assertRaises(HeroInvalidError) if error_count > 0 else nullcontext() as ctx:
            self.service.validate(hero, Rulebook.map(rulebooks))
        # then:
        if ctx and ctx.exception:
            self.assertIs(error_count, len(ctx.exception.errors), msg=ctx.exception.errors)

    @parameterized.expand([
        (heros.VALID_SOELDNER,),
        (heros.VALID_ZAUBERWEBER,),
        (heros.VALID_HAENDLER,),
    ])
    def test_valid_hero(self, valid_hero: Hero):
        # given:
        rulebooks = ['dsa5']
        # when:
        try:
            self.service.validate(valid_hero, Rulebook.map(rulebooks))
        # then:
        except HeroInvalidError:
            self.fail(f"A valid Hero has validation errors.")
