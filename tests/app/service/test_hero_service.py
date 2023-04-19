from parameterized import parameterized

from dsaheldenbogen.app.engine.exceptions import HeroInvalidError
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.services.hero_service import HeroService
from tests import invalid_heros
from tests import valid_heros
from tests.base_test_case import BaseTestCase
from tests.invalid_heros import InvalidHeroTestcase
from tests.valid_heros import ValidHeroTestcase


def _is_subset_of(subset: dict, superset: dict) -> bool:
    return all(item in superset.items() for item in subset.items())


class TestHeroService(BaseTestCase):
    service = HeroService()

    @parameterized.expand([
        (invalid_heros.UNKNOWN_RACE,),
        (invalid_heros.UNKNOWN_CULTURE,),
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
    def test_invalid_heros(self, testcase: InvalidHeroTestcase):
        # expect:
        with self.assertRaises(HeroInvalidError) as ctx:
            # when:
            self.service.validate(testcase.hero, Rulebook.map(testcase.rulebooks))
        # then:
        found_type = False
        found_params = False
        for error in ctx.exception.errors:
            if error.type == testcase.error_type:
                found_type = True
                if _is_subset_of(testcase.error_params, error.parameter):
                    found_params = True
                    break
        self.assertTrue(found_type, msg=f"Did not find error of expected type."
                                        f"\nexpected type: {testcase.error_type}"
                                        f"\nfound errors: {ctx.exception.errors}")
        params_of_correct_error_type = [str(e.parameter) for e in ctx.exception.errors if e.type == testcase.error_type]
        self.assertTrue(found_params, msg=f"Found error type but does not have expected params."
                                          f"\nexpected params: {testcase.error_params}"
                                          f"\nfound params:"
                                          f"\n{chr(10).join(params_of_correct_error_type)}")

    @parameterized.expand([
        (valid_heros.SOELDNER,),
        (valid_heros.ZAUBERWEBER,),
        (valid_heros.HAENDLER,),
    ])
    def test_valid_hero(self, testcase: ValidHeroTestcase):
        # given:
        rulebooks = Rulebook.map(testcase.rulebooks)
        # when:
        try:
            self.service.validate(testcase.hero, rulebooks)
        # then:
        except HeroInvalidError:
            self.fail(f"A valid Hero has validation errors.")
