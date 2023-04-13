from dsaheldenbogen.app.engine.rulebook_program import RulebookProgram
from dsaheldenbogen.app.engine.rulebook_validator import RulebookValidator
from dsaheldenbogen.app.models.rulebook import Rulebook
from tests.app.engine.tester_engine import TesterEngine
from tests.base_test_case import BaseTestCase

REQUIRED_PROGRAMS = [
    RulebookProgram.RULEBOOK_USABLE,
]

FACT_RULEBOOK = 'rulebook'


class TestResourcesRulebooks(BaseTestCase):

    def test_rulebook_valid(self):
        # given:
        rulebooks = Rulebook.list_known()
        # when:
        valid_rulebooks = RulebookValidator.filter(rulebooks)
        # then: no rulebook has been filtered
        diff = {r.name for r in rulebooks} ^ {r.name for r in valid_rulebooks}
        self.assertFalse(diff, msg="List of invalid rulebooks shall be empty.")

    def test_rulebook_has_required_programs(self):
        # given:
        known_rulebooks = Rulebook.list_known()
        # when:
        errors = []
        for rulebook in known_rulebooks:
            engine = TesterEngine(rulebook)
            missing_programs = engine.has_programs(REQUIRED_PROGRAMS)
            if missing_programs:
                errors.append(f"Rulebook '{rulebook}' missing required programs: {missing_programs}")

        # then:
        if errors:
            self.fail('\n'.join(errors))

    def test_rulebook_facts_only_itself(self):
        # given:
        known_rulebooks = Rulebook.list_known()
        # when:
        errors = []
        for rulebook in known_rulebooks:
            engine = TesterEngine(rulebook)
            found, others = engine.has_function_with_value([RulebookProgram.RULEBOOK_USABLE], FACT_RULEBOOK, rulebook.name)
            if not found:
                errors.append(f"Rulebook '{rulebook}' does not declares itself as fact.")
            if others:
                errors.append(f"Rulebook '{rulebook}' declares to be other rulebook(s): {others}")

        # then:
        if errors:
            self.fail('\n'.join(errors))
