from parameterized import parameterized

from dsaheldenbogen.app.models.feature import Feature
from dsaheldenbogen.app.services.meta_service import MetaService
from tests.app.engine.engine import TestEngine
from tests.app.models.rulebook import TestRulebook
from tests.base_test_case import BaseTestCase


class TestMetaService(BaseTestCase):
    service = MetaService(TestEngine)

    @parameterized.expand([
        (1, Feature.EXPERIENCE_LEVEL),
        (2, Feature.RACE),
        (3, Feature.CULTURE),
        (1, Feature.PROFESSION),
        (4, Feature.ADVANTAGE),
        (3, Feature.DISADVANTAGE),
        (2, Feature.TALENT),
        (1, Feature.COMBAT_TECHNIQUE),
    ])
    def test_feature_listing(self, expected_count: int, feature: Feature):
        # given:
        rulebooks = ['meta_service']
        # when:
        found = self.service.list_known_feature_values(feature, TestRulebook.map(rulebooks))
        # then:
        self.assertIs(len(found), expected_count)
