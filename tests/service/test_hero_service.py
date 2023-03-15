from parameterized import parameterized

from app.engine.exceptions import HeroInvalidError
from app.models.hero import Hero
from app.models.hero_validation_error import HeroValidationError
from app.models.hero_validation_param import HeroValidationParam
from app.models.rulebook import Rulebook
from app.services.hero_service import HeroService
from tests import invalid_heros
from tests import valid_heros
from tests.base_test_case import BaseTestCase


def _is_subset_of(subset: dict, superset: dict) -> bool:
    return all(item in superset.items() for item in subset.items())


class TestHeroService(BaseTestCase):
    service = HeroService()

    @parameterized.expand([
        (invalid_heros.UNKNOWN_SPECIES,),
        (invalid_heros.UNKNOWN_CULTURE,),
        (invalid_heros.UNKNOWN_PROFESSION,),
        (invalid_heros.UNKNOWN_TALENT,),
        (invalid_heros.UNKNOWN_COMBAT_TECHNIQUE,),
        (invalid_heros.UNKNOWN_ADVANTAGE,),
        (invalid_heros.UNKNOWN_DISADVANTAGE,),
    ])
    def test_invalid_heros(self, data: tuple[HeroValidationError.Type, dict[HeroValidationParam, str], Hero]):
        # given:
        rulebooks = Rulebook.map(['dsa5'])
        expected_error_type = data[0]
        expected_error_params = data[1]
        invalid_hero = data[2]
        # expect:
        with self.assertRaises(HeroInvalidError) as ctx:
            # when:
            self.service.validate(invalid_hero, rulebooks)
        # then:
        found = False
        for error in ctx.exception.errors:
            if error.type == expected_error_type:
                self.assertTrue(
                    _is_subset_of(expected_error_params, error.parameter),
                    msg=f"Found error type but does not have expected params."
                        f"\nexpected params: {expected_error_params}"
                        f"\nerror params: {error.parameter}"
                )
                found = True
        self.assertTrue(found, msg=f"Did not find error of expected type."
                                   f"\nexpected type: {expected_error_type}"
                                   f"\nfound errors: {ctx.exception.errors}"
                        )

    @parameterized.expand([
        (valid_heros.SOELDNER,),
        (valid_heros.ZAUBERWEBER,),
        (valid_heros.HAENDLER,),
    ])
    def test_valid_hero(self, valid_hero: Hero):
        # given:
        rulebooks = Rulebook.map(['dsa5'])
        # when:
        try:
            self.service.validate(valid_hero, rulebooks)
        # then:
        except HeroInvalidError:
            self.fail(f"A valid Hero has validation errors.")
