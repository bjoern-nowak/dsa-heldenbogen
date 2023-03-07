import logging
from symtable import Symbol
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple

from clingo import Control
from clingo import Model
from clingo import SolveResult
from clingo import Symbol

from app.engine.collector import Collector
from app.engine.hero_validation_interpreter import HeroValidationInterpreter
from app.engine.hero_wrapper import HeroWrapper
from app.engine.rulebook_program import RulebookProgram
from app.engine.rulebook_validator import RulebookValidator
from app.error import UnexpectedResultError
from app.error import UnusableRulebookError
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
    }
    DEFAULT_HERO_VALIDATION_STEPS = hero_validation_steps.keys()

    def __init__(self, rulebooks: List[Rulebook]) -> None:
        self.rulebooks = RulebookValidator.filter(rulebooks)
        self.ctl = self._create_control()
        self._check_rulebooks_usable()
        self._find_extra_hero_validation_steps()
        self.hero_validation_steps = dict(sorted(self.hero_validation_steps.items()))  # sort by keys

    def _create_control(self) -> Control:
        ctl = Control()
        ctl.load(Rulebook.common_file())
        for rulebook in self.rulebooks:
            ctl.load(rulebook.entrypoint())
        return ctl

    def _check_rulebooks_usable(self) -> None:
        unusables: List[List[str]] = []
        self._execute(
            ground_parts=[RulebookProgram.RULEBOOK_USABLE],
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
            ground_parts=[RulebookProgram.META],
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

    def validate(self, hero: Hero) -> List[str] | None:
        errors = []
        for step in self.hero_validation_steps:
            program = step if isinstance(step, RulebookProgram) else RulebookProgram.hero_validation_step_for(step)
            errors = self._perform_hero_validation_step(hero, program)
            if errors:
                break
        return errors

    def _perform_hero_validation_step(self, hero: Hero, program: Tuple[str, Sequence[Symbol]]) -> List[str] | None:
        errors: List[Symbol] = []
        self._execute(
            ground_parts=[RulebookProgram.BASE, RulebookProgram.HERO_FACTS, program],
            context=HeroWrapper(hero),
            on_model=lambda m: Collector.hero_validation_errors(m, errors),
            on_fail_raise=UnexpectedResultError(f"Hero validation could not be performed at: {program[0]}")
        )
        return [HeroValidationInterpreter.str(e) for e in errors]

    def list(self, feature: Feature) -> List[str]:
        known_values: List[str] = []
        self._execute(
            on_model=lambda m: Collector.known_feature_values(m, known_values, feature),
            on_fail_raise=UnexpectedResultError(f"Value listing for feature '{feature}' failed.")
        )
        return known_values

    def _execute(self,
                 ground_parts: Sequence[Tuple[str, Sequence[Symbol]]] = (RulebookProgram.BASE,),
                 context: Any = None,
                 on_model: Optional[Callable[[Model], Optional[bool]]] = None,
                 on_fail_raise: Exception = None):
        self.ctl.ground(ground_parts, context)
        result: SolveResult = self.ctl.solve(on_model=on_model)
        if not result.satisfiable:
            if on_fail_raise:
                raise on_fail_raise
            else:
                logger.warning(f"No exception raise defined, but could not execute programs: {[p[0] for p in ground_parts]}")
