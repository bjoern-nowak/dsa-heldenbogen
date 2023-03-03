from pathlib import Path
from symtable import Symbol
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
from app.resource import get_path


class Engine:

    def __init__(self, _rulebooks: List[Rulebook]) -> None:
        self.rulebooks = RulebookValidator.filter(_rulebooks)
        self.ctl = self._create_control()
        self._check_rulebooks_usable()

    def _create_control(self) -> Control:
        ctl = Control()
        # TODO may use '#include' in LPs
        for path in self._get_rules():
            ctl.load(path.as_posix())
        return ctl

    def _get_rules(self) -> List[Path]:
        rules = []
        for book in self.rulebooks:
            rules.append(get_path(f"regelwerk/common.lp"))
            rules.append(get_path(f"regelwerk/{book}/meta.lp"))
            rules.append(get_path(f"regelwerk/{book}/rules.lp"))
        return rules

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
            raise UnusableRulebookError(chr(10).join(messages))

    def validate(self, hero: Hero) -> List[str] | None:
        errors: List[str] = self.validate_step(hero, RulebookProgram.VALIDATE_HERO_STEP1)
        if not errors:
            errors: List[str] = self.validate_step(hero, RulebookProgram.VALIDATE_HERO_STEP2)
        if not errors:
            errors: List[str] = self.validate_step(hero, RulebookProgram.VALIDATE_HERO_STEP3)
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
