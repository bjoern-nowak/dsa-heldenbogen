from parameterized import parameterized

from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.services.meta_service import MetaService
from tests.base_test_case import BaseTestCase


class TestMetaService(BaseTestCase):
    service = MetaService()

    @parameterized.expand([
        (4, Feature.SPECIES),
        (33, Feature.CULTURE),
        (4, Feature.PROFESSION),
        (34, Feature.ADVANTAGE),
        (16, Feature.DISADVANTAGE),
        (31, Feature.TALENT),
        (7, Feature.COMBAT_TECHNIQUE),
    ])
    def test_feature_listing(self, expected_count: int, feature: Feature):
        # given:
        rulebooks = ['dsa5']
        # when:
        found = self.service.list_known_feature_values(feature, Rulebook.map(rulebooks))
        # then:
        self.assertIs(len(found), expected_count)
