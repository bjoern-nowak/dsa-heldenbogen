from __future__ import annotations  # required till PEP 563

from typing import List
from typing import Sequence

from clingo import Symbol

from dsaheldenbogen.app.engine import hero_validation_interpreter
from dsaheldenbogen.app.engine.collector import Collector
from dsaheldenbogen.app.engine.exceptions import HeroInvalidError
from dsaheldenbogen.app.engine.exceptions import UnexpectedResultError
from dsaheldenbogen.app.engine.exceptions import UnusableRulebookError
from dsaheldenbogen.app.engine.rulebook_program import RulebookProgram
from dsaheldenbogen.app.logger import getLogger
from dsaheldenbogen.app.models.feature import Feature
from dsaheldenbogen.app.models.hero import Hero
from dsaheldenbogen.app.models.hero_validation_warning import HeroValidationWarning
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.infrastructure.clingo_executor import ClingoExecutor

logger = getLogger(__name__)


class Engine:
    # TODO one could argue that these step count is execcsive.
    #  To reduce this would require an error/warning filtering to root causes
    #   so that only one step per feature (instead of currently two) is used
    #  Anyway having steps is useful, since it allows rulebooks to intervene
    hero_validation_steps: dict[int, RulebookProgram | int] = {
        50: RulebookProgram.VALIDATE_HERO_STEP_50,
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
        self.rulebooks = rulebooks
        self.clingo_executor = ClingoExecutor(
            [Rulebook.common_file()] + [r.entrypoint_file() for r in self.rulebooks],
            [RulebookProgram.BASE]
        )
        self._check_rulebooks_usable()

        self._find_extra_hero_validation_steps()
        self.hero_validation_steps = dict(sorted(self.hero_validation_steps.items()))  # sort by keys

    def _check_rulebooks_usable(self) -> None:
        unusables: List[List[str]] = Collector.unusable_rulebooks(
            self.clingo_executor.run(
                programs=[RulebookProgram.RULEBOOK_USABLE],
                on_fail=UnexpectedResultError("Failed to collect unusable rulebooks.")
            )
        )
        if unusables:
            messages = []
            for sym in unusables:
                messages.append(f"Rulebook '{sym[0]}' missing '{sym[1]}'.")
            raise UnusableRulebookError(chr(10).join(messages))  # chr(10) := '\n' (line break)

    def _find_extra_hero_validation_steps(self) -> None:
        steps: List[Symbol] = Collector.extra_hero_validation_steps(
            self.clingo_executor.run(
                programs=[RulebookProgram.META],
                on_fail=UnexpectedResultError("Failed to find extra hero validation steps.")
            )
        )
        if steps:
            logger.debug(f"Found extra hero validation steps: {steps}")

        for step in [step.arguments[0].number for step in steps]:
            if step in self.DEFAULT_HERO_VALIDATION_STEPS:
                # TODO should be a testcase instead of a runtime check
                logger.warning(f"Some rulebook redeclare default hero validation step '{step}' as extra. "
                               "It does not harm but it is not recommended for clarity. "
                               f"Used rulebooks: {self.rulebooks}")
            else:
                self.hero_validation_steps[step] = step

    def validate(self, hero: Hero) -> List[HeroValidationWarning]:
        """
        If this method passes without an exception the hero has passed the validation positively
        It breaks validation steps-wise on validation errors, but collect warnings step-wide.
        :returns: list of warnings, when validation passed
        :raises HeroInvalidError: whenever any hero validation step has an error
        :raises UnexpectedResultError: whenever any hero validation step could not be performed
        """
        warnings: List[HeroValidationWarning] = []
        for step in self.hero_validation_steps:
            program = step if isinstance(step, RulebookProgram) else RulebookProgram.hero_validation_step_for(step)
            step_errors, step_warnings = self._perform_hero_validation_step(hero, program)
            warnings += [hero_validation_interpreter.as_warning(w) for w in step_warnings]
            if step_errors:
                # TODO 'return' vs 'raise' is discussable.
                #  One could argue that an HeroInvalidError should only be raised if the input values are e.g. unknown
                #   and 'hero validation errors' are seen as normal case hence should be returned.
                #  In contrast, the main point is to find errors and should be prominent whenever found.
                #   Using a return (tuple or class) could lead to higher chances of mishandling.
                #  What is bad now, is that warnings may be fetched by return or raise.
                raise HeroInvalidError([hero_validation_interpreter.as_error(e) for e in step_errors], warnings)
        return warnings

    def _perform_hero_validation_step(self,
                                      hero: Hero,
                                      program: tuple[str, Sequence[Symbol]]) -> tuple[List[Symbol], List[Symbol]]:
        """
        :return: tuple of (errors, warnings)
        """
        model = self.clingo_executor.run(
            programs=[RulebookProgram.WORLD_FACTS, RulebookProgram.HERO_FACTS, program],
            context=hero,
            on_fail=UnexpectedResultError(f"Hero validation could not be performed at: {program[0]}")
        )
        errors: List[Symbol] = Collector.hero_validation_errors(model)
        warnings: List[Symbol] = Collector.hero_validation_warnings(model)
        return errors, warnings

    def list_known_for(self, feature: Feature) -> List[tuple[str, str, int]] | List[str]:
        known_values: List[Symbol] = Collector.known_feature_values(
            self.clingo_executor.run(
                programs=[RulebookProgram.WORLD_FACTS],
                on_fail=UnexpectedResultError(f"Value listing for feature '{feature}' failed.")
            ),
            feature
        )
        if feature in [Feature.ADVANTAGE, Feature.DISADVANTAGE]:
            return [(da.arguments[0].string, da.arguments[1].string, da.arguments[2].number) for da in known_values]
        return [k.arguments[0].string for k in known_values]
