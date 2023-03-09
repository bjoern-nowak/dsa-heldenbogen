from __future__ import annotations  # required till PEP 563

import logging
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Sequence

from clingo import Control
from clingo import Model
from clingo import SolveResult
from clingo import Symbol

from app.engine.collector import Collector
from app.engine.exceptions import HeroInvalidError
from app.engine.exceptions import UnexpectedResultError
from app.engine.exceptions import UnusableRulebookError
from app.engine.hero_validation_error import HeroValidationError
from app.engine.hero_validation_warning import HeroValidationWarning
from app.engine.hero_wrapper import HeroWrapper
from app.engine.rulebook_program import RulebookProgram
from app.engine.rulebook_validator import RulebookValidator
from app.models import Feature
from app.models import Hero
from app.models import Rulebook

logger = logging.getLogger(__name__)


class Engine:
    hero_validation_steps: dict[int, RulebookProgram | int] = {
        100: RulebookProgram.VALIDATE_HERO_STEP_100,
        150: RulebookProgram.VALIDATE_HERO_STEP_150,
        200: RulebookProgram.VALIDATE_HERO_STEP_200,
        250: RulebookProgram.VALIDATE_HERO_STEP_250,
        300: RulebookProgram.VALIDATE_HERO_STEP_300,
        350: RulebookProgram.VALIDATE_HERO_STEP_350,
        400: RulebookProgram.VALIDATE_HERO_STEP_400,
        450: RulebookProgram.VALIDATE_HERO_STEP_450,
        500: RulebookProgram.VALIDATE_HERO_STEP_500,
        550: RulebookProgram.VALIDATE_HERO_STEP_550,
    }
    DEFAULT_HERO_VALIDATION_STEPS = hero_validation_steps.keys()

    def __init__(self, rulebooks: List[Rulebook]) -> None:
        self.rulebooks = RulebookValidator.filter(rulebooks)
        self._check_rulebooks_usable()
        self._find_extra_hero_validation_steps()
        self.hero_validation_steps = dict(sorted(self.hero_validation_steps.items()))  # sort by keys

    def _check_rulebooks_usable(self) -> None:
        unusables: List[List[str]] = []
        self._execute(
            programs=[RulebookProgram.RULEBOOK_USABLE],
            on_model=lambda m: Collector.unusable_rulebooks(m, unusables),
            on_fail_raise=UnexpectedResultError(f"Failed to collect unusable rulebooks.")
        )
        if unusables:
            messages = []
            for a in unusables:
                messages.append(f"Rulebook '{a[0]}' missing '{a[1]}'.")
            raise UnusableRulebookError(chr(10).join(messages))  # chr(10) := '\n' (line break)

    def _find_extra_hero_validation_steps(self) -> None:
        steps: List[Symbol] = []
        self._execute(
            programs=[RulebookProgram.META],
            on_model=lambda m: Collector.extra_hero_validation_steps(m, steps),
            on_fail_raise=UnexpectedResultError(f"Failed to find extra hero validation steps.")
        )
        if steps:
            logger.debug(f"Found extra hero validation steps: {steps}")

        for step in [step.arguments[0].number for step in steps]:
            if step in self.DEFAULT_HERO_VALIDATION_STEPS:
                # TODO should be a testcase instead of a runtime check
                logger.warning(f"Some rulebook redeclare default hero validation step '{step}' as extra. "
                               f"It does not harm but it is not recommended for clarity. "
                               f"Used rulebooks: {self.rulebooks}")
            else:
                self.hero_validation_steps[step] = step

    def validate(self, _hero: Hero) -> List[HeroValidationWarning]:
        """
        If this method passes without an exception the hero has passed the validation positively
        It breaks validation steps-wise on validation errors, but collect warnings step-wide.
        :returns: list of warnings, when validation passed
        :raises HeroInvalidError: whenever any hero validation step has an error
        :raises UnexpectedResultError: whenever any hero validation step could not be performed
        """
        hero = HeroWrapper(_hero)
        warnings: List[HeroValidationWarning] = []
        for step in self.hero_validation_steps:
            program = step if isinstance(step, RulebookProgram) else RulebookProgram.hero_validation_step_for(step)
            step_errors, step_warnings = self._perform_hero_validation_step(hero, program)
            warnings += [HeroValidationWarning.from_(w) for w in step_warnings]
            if step_errors:
                # TODO 'return' vs 'raise' is discussable.
                #  One could argue that an HeroInvalidError should only be raised if the input values are e.g. unknown
                #   and 'hero validation errors' are seen as normal case hence should be returned.
                #  In contrast the main point is to find errors and should be prominent whenever found.
                #   Using an return (tuple or class) could lead to higher chances of mishandling.
                #  What is bad now, is that warnings may be fetched by return or raise.
                raise HeroInvalidError([HeroValidationError.from_(e) for e in step_errors], warnings)
        return warnings

    def _perform_hero_validation_step(self,
                                      hero: HeroWrapper,
                                      program: tuple[str, Sequence[Symbol]]) -> tuple[List[Symbol], List[Symbol]]:
        """
        :return: tuple of errors and warnings
        """
        errors: List[Symbol] = []
        warnings: List[Symbol] = []
        self._execute(
            programs=[RulebookProgram.WORLD_FACTS, RulebookProgram.HERO_FACTS, program],
            context=hero,
            on_model=lambda m: Collector.hero_validation_errors_and_warnings(m, errors, warnings),
            on_fail_raise=UnexpectedResultError(f"Hero validation could not be performed at: {program[0]}")
        )
        return errors, warnings

    def list_known_for(self, feature: Feature) -> List[str]:
        known_values: List[str] = []
        self._execute(
            programs=[RulebookProgram.WORLD_FACTS],
            on_model=lambda m: Collector.known_feature_values(m, known_values, feature),
            on_fail_raise=UnexpectedResultError(f"Value listing for feature '{feature}' failed.")
        )
        return known_values

    def _execute(self,
                 programs: List[tuple[str, Sequence[Symbol]]],
                 context: Any = None,
                 on_model: Optional[Callable[[Model], Optional[bool]]] = None,
                 on_fail_raise: Exception = None):
        default_programs: List[tuple[str, Sequence[Symbol]]] = [RulebookProgram.BASE]
        ctl = self._create_control()
        ctl.ground(default_programs + programs, context)
        result: SolveResult = ctl.solve(on_model=on_model)
        if not result.satisfiable:
            if on_fail_raise:
                raise on_fail_raise
            else:
                logger.warning(f"No exception raise defined, but could not execute programs: {[p[0] for p in programs]}")

    def _create_control(self) -> Control:
        ctl = Control()
        ctl.load(Rulebook.common_file())
        for rulebook in self.rulebooks:
            ctl.load(rulebook.entrypoint())
        return ctl
