from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.services.rulebook_validator import RulebookValidator


class TestResourcesRulebooks:

    def test_rulebooks_valid(self):
        # given:
        known_rulebooks = Rulebook.list_known()
        # when:
        errors = []
        for rulebook in known_rulebooks:
            errors = errors + RulebookValidator.check(rulebook)
        # then:
        if errors:
            self.fail('\n'.join(errors))
