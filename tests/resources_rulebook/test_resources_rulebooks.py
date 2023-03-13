import unittest

from app.engine.rulebook_validator import RulebookValidator
from app.models.rulebook import Rulebook


class TestResourcesRulebooks(unittest.TestCase):

    def test_rulebooks_valid(self):
        # given:
        rulebooks = Rulebook.list_known()
        # when:
        valid_rulebooks = RulebookValidator.filter(rulebooks)
        # then: no rulebook has been filtered
        diff = {r.name for r in rulebooks} ^ {r.name for r in valid_rulebooks}
        self.assertFalse(diff, msg="List of invalid rulebooks shall be empty.")


if __name__ == '__main__':
    unittest.main()
