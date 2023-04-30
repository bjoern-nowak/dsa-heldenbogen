from parameterized import parameterized
from tests.base_test_case import BaseTestCase

from dsaheldenbogen.app.engine.exceptions import HeroInvalidError
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.services.hero_service import HeroService
from tests.e2e.invalid_heros import InvalidHeroTestcase
from tests.e2e.invalid_heros import InvalidHeroTestcases
from tests.e2e.valid_heros import ValidHeroTestcase
from tests.e2e.valid_heros import ValidHeroTestcases


def _is_subset_of(subset: dict, superset: dict) -> bool:
    return all(item in superset.items() for item in subset.items())


class TestHeroService(BaseTestCase):
    service = HeroService()

    @parameterized.expand(InvalidHeroTestcases.all())
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

    @parameterized.expand(ValidHeroTestcases.all())
    def test_valid_hero(self, testcase: ValidHeroTestcase):
        # given:
        rulebooks = Rulebook.map(testcase.rulebooks)
        # when:
        try:
            self.service.validate(testcase.hero, rulebooks)
        # then:
        except HeroInvalidError:
            self.fail("A valid Hero has validation errors.")
