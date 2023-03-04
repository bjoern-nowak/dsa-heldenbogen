from symtable import Symbol
from typing import List

from clingo import Control
from clingo import SolveResult
from clingo import Symbol

from app.engine.collector import Collector
from app.engine.hero_validation_interpreter import HeroValidationInterpreter
from app.engine.hero_wrapper import HeroWrapper
from app.engine.rulebook_function import RulebookFunction
from app.engine.rulebook_program import RulebookProgram
from app.engine.rulebook_validator import RulebookValidator
from app.error import UnusableRulebookError
from app.models import Feature
from app.models import Hero
from app.models import Rulebook

_DEFAULT_HERO_VALIDATION_STEPS = [100, 200, 300]


class Engine:
    hero_validation_steps: dict[int, RulebookProgram | int] = {
        100: RulebookProgram.VALIDATE_HERO_STEP_100,
        200: RulebookProgram.VALIDATE_HERO_STEP_200,
        300: RulebookProgram.VALIDATE_HERO_STEP_300,
    }

    def __init__(self, rulebooks: List[Rulebook]) -> None:
        self.ctl = self._create_control(RulebookValidator.filter(rulebooks))
        self._check_rulebooks_usable()
        self._find_extra_hero_validation_steps()
        # sort by keys
        self.hero_validation_steps = dict(sorted(self.hero_validation_steps.items()))

    @staticmethod
    def _create_control(rulebooks: List[Rulebook]) -> Control:
        ctl = Control()
        for entrypoint in Engine._get_entrypoint_paths(rulebooks):
            ctl.load(entrypoint)
        return ctl

    @staticmethod
    def _get_entrypoint_paths(rulebooks: List[Rulebook]) -> List[str]:
        paths = [Rulebook.common_file()]
        for rulebook in rulebooks:
            paths.append(rulebook.entrypoint())
        return paths

    def _check_rulebooks_usable(self) -> None:
        self.ctl.ground([RulebookProgram.RULEBOOK_USABLE])
        unusables: List[List[str]] = []
        self.ctl.solve(
            on_model=lambda m: Collector.functions_strings(unusables, m, RulebookFunction.RULEBOOK_UNUSABLE)
        )
        if unusables:
            messages = []
            for a in unusables:
                messages.append(f"Rulebook '{a[0]}' missing '{a[1]}'.")
            raise UnusableRulebookError(chr(10).join(messages))  # chr(10) := '\n' (line break)

    def _find_extra_hero_validation_steps(self) -> None:
        steps: List[Symbol] = []
        self.ctl.ground([RulebookProgram.META])
        self.ctl.solve(on_model=lambda m: Collector.functions(steps, m, [RulebookFunction.EXTRA_HERO_VALIDATION_STEP]))
        for step in [step.arguments[0].number for step in steps]:
            self.hero_validation_steps[step] = step
            if step in _DEFAULT_HERO_VALIDATION_STEPS:
                # TODO make it a warning, and it should be a testcase instead of a runtime check
                print(f"Some of the given rulebooks redeclare the default hero validation step '{step}' as an additional."
                      f"It does not harm but it is not recommended.")

    def validate(self, hero: Hero) -> List[str] | None:
        errors = []
        for step in self.hero_validation_steps:
            errors = self._validate_step(hero, step)
            if errors:
                break
        return errors

    def _validate_step(self, hero: Hero, step: RulebookProgram | int) -> List[str] | None:
        program = step if isinstance(step, RulebookProgram) else RulebookProgram.hero_validation_step_for(step)
        self.ctl.ground([RulebookProgram.BASE, RulebookProgram.HERO_FACTS, program], HeroWrapper.wrap(hero))
        errors: List[Symbol] = []
        result: SolveResult = self.ctl.solve(
            on_model=lambda m: Collector.functions(
                errors, m, [RulebookFunction.UNKNOWN_SUFFIX, RulebookFunction.UNUSABLE_SUFFIX]
            )
        )
        if not result.satisfiable:
            return None
        return [HeroValidationInterpreter.str(e) for e in errors]

    def list(self, feature: Feature) -> List[str]:
        self.ctl.ground()
        features: List[str] = []
        self.ctl.solve(
            on_model=lambda m: Collector.functions_first_string(features, m, RulebookFunction.known(feature))
        )
        return features
