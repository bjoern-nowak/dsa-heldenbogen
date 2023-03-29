from typing import List
from typing import Optional

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
        (invalid_heros.UNKNOWN_RACE,),  # case 0
        (invalid_heros.UNKNOWN_CULTURE,),  # case 1 ...
        (invalid_heros.UNKNOWN_PROFESSION,),
        (invalid_heros.UNKNOWN_TALENT,),
        (invalid_heros.UNKNOWN_COMBAT_TECHNIQUE,),
        (invalid_heros.UNKNOWN_ADVANTAGE,),
        (invalid_heros.UNKNOWN_DISADVANTAGE,),
        (invalid_heros.CULTURE_UNUSABLE_BY_RACE,),
        (invalid_heros.PROFESSION_UNUSABLE_BY_RACE,),
        (invalid_heros.PROFESSION_UNUSABLE_BY_CULTURE,),
        (invalid_heros.PROFESSION_MISSING_LEVEL_FOR_TALENT,),
        (invalid_heros.PROFESSION_MISSING_LEVEL_FOR_COMBAT_TECHNIQUE,),
        (invalid_heros.PROFESSION_MISSING_LEVEL_FOR_ANY_OF_COMBAT_TECHNIQUES,),
        (invalid_heros.TALENT_EXCEEDS_MAX_LEVEL_BY_EXPERIENCE,),
        (invalid_heros.COMBAT_TECHNIQUE_EXCEEDS_MAX_LEVEL_BY_EXPERIENCE,),
    ])
    def test_invalid_heros(self,
                           data: tuple[HeroValidationError.Type, dict[HeroValidationParam, str, Optional[List[str]]], Hero]):
        # given:
        expected_error_type = data[0]
        expected_error_params = data[1]
        invalid_hero = data[2]
        rulebooks = data[3] if len(data) == 4 else ['dsa5']
        # expect:
        with self.assertRaises(HeroInvalidError) as ctx:
            # when:
            self.service.validate(invalid_hero, Rulebook.map(rulebooks))
        # then:
        found_type = False
        found_params = False
        for error in ctx.exception.errors:
            if error.type == expected_error_type:
                found_type = True
                if _is_subset_of(expected_error_params, error.parameter):
                    found_params = True
                    break
        self.assertTrue(found_type, msg=f"Did not find error of expected type."
                                        f"\nexpected type: {expected_error_type}"
                                        f"\nfound errors: {ctx.exception.errors}")
        params_of_correct_error_type = [str(e.parameter) for e in ctx.exception.errors if e.type == expected_error_type]
        self.assertTrue(found_params, msg=f"Found error type but does not have expected params."
                                          f"\nexpected params: {expected_error_params}"
                                          f"\nfound params:"
                                          f"\n{chr(10).join(params_of_correct_error_type)}")

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
