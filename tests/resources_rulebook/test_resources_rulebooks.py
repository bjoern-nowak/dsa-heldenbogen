from app.engine.rulebook_program import RulebookProgram
from app.engine.rulebook_validator import RulebookValidator
from app.models.rulebook import Rulebook
from tests.base_test_case import BaseTestCase
from tests.engine.test_engine import TestEngine

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
        required_programs = [RulebookProgram.RULEBOOK_USABLE]
        # when:
        errors = []
        for rulebook in known_rulebooks:
            engine = TestEngine(rulebook)
            missing_programs = engine.has_programs(required_programs)
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
            engine = TestEngine(rulebook)
            has_function, others = engine.has_only_function([RulebookProgram.RULEBOOK_USABLE], FACT_RULEBOOK, rulebook.name)
            if not has_function:
                errors.append(f"Rulebook '{rulebook}' does not declares itself as fact.")
            if others:
                errors.append(f"Rulebook '{rulebook}' declares to be other rulebook(s): {others}")

        # then:
        if errors:
            self.fail('\n'.join(errors))
