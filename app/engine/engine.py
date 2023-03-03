from typing import List

from clingo import Control
from clingo import SolveResult

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


class Engine:

    def __init__(self, rulebooks: List[Rulebook]) -> None:
        self.ctl = Engine._create_control(RulebookValidator.filter(rulebooks))
        self._check_rulebooks_usable()

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

    def validate(self, hero: Hero) -> List[str] | None:
        errors = self.validate_step(hero, RulebookProgram.VALIDATE_HERO_STEP1)
        if not errors:
            errors = self.validate_step(hero, RulebookProgram.VALIDATE_HERO_STEP2)
        if not errors:
            errors = self.validate_step(hero, RulebookProgram.VALIDATE_HERO_STEP3)
        return errors

    def validate_step(self, hero: Hero, step: RulebookProgram) -> List[str] | None:
        self.ctl.ground([RulebookProgram.BASE, RulebookProgram.HERO_FACTS, step], HeroWrapper.wrap(hero))
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
