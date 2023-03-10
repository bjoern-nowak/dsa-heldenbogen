import unittest

from parameterized import parameterized

from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.services.meta_service import MetaService


class TestMetaService(unittest.TestCase):
    service = MetaService()

    @parameterized.expand([
        (3, Feature.SPECIES),
        (33, Feature.CULTURE),
    ])
    def test_feature_listing(self, expected_count: int, feature: Feature):
        # given:
        rulebooks = ['dsa5']
        # when:
        found = self.service.list_known_feature_values(feature, Rulebook.list_by(rulebooks))
        # then:
        self.assertIs(len(found), expected_count)


if __name__ == '__main__':
    unittest.main()
