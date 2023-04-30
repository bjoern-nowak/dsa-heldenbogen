from http import HTTPStatus

from httpx import Response
from parameterized import parameterized
from starlette.testclient import TestClient

from dsaheldenbogen.api.root import app
from dsaheldenbogen.api.schemas.hero_validation_result import HeroValidationResult
from tests.e2e.invalid_heros import InvalidHeroTestcase
from tests.e2e.invalid_heros import InvalidHeroTestcases
from tests.e2e.valid_heros import ValidHeroTestcase
from tests.e2e.valid_heros import ValidHeroTestcases


def _is_subset_of(subset: dict, superset: dict) -> bool:
    return all(item in superset.items() for item in subset.items())


class TestHeroApi:
    client = TestClient(app)

    @parameterized.expand(InvalidHeroTestcases.all())
    def test_invalid_heros(self, testcase: InvalidHeroTestcase):
        # when:
        response: Response = self.client.post("/api/hero/validate",
                                              json=testcase.hero.dict(),
                                              params={'rulebooks': testcase.rulebooks})
        # then:
        assert response.status_code == HTTPStatus.OK
        result = HeroValidationResult.parse_obj(response.json())
        # and:
        found_type = False
        found_params = False
        for error in result.errors:
            if error.type == testcase.error_type:
                found_type = True
                if _is_subset_of(testcase.error_params, error.parameter):
                    found_params = True
                    break
        assert found_type, f"Did not find error of expected type." \
                           f"\nexpected type: {testcase.error_type}" \
                           f"\nfound errors: {result.errors}"
        params_of_correct_error_type = [str(e.parameter) for e in result.errors if e.type == testcase.error_type]
        assert found_params, f"Found error type but does not have expected params." \
                             f"\nexpected params: {testcase.error_params}" \
                             f"\nfound params:" \
                             f"\n{chr(10).join(params_of_correct_error_type)}"

    @parameterized.expand(ValidHeroTestcases.all())
    def test_valid_hero(self, testcase: ValidHeroTestcase):
        # when:
        response: Response = self.client.post("/api/hero/validate",
                                              json=testcase.hero.dict(),
                                              params={'rulebooks': testcase.rulebooks})
        # then:
        assert response.status_code == HTTPStatus.OK
        result = HeroValidationResult.parse_obj(response.json())
        # and:
        assert result.valid, "A valid Hero has validation errors."
