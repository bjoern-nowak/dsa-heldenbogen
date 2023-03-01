from pathlib import Path
from typing import List

from clingo import Control
from clingo import Model
from clingo import SolveResult

from app.engine.collector import Collector
from app.engine.hero_wrapper import HeroWrapper
from app.engine.rulebook_function import RulebookFunction
from app.engine.rulebook_program import RulebookProgram
from app.engine.rulebook_validator import RulebookValidator
from app.models import Hero
from app.models.feature import Feature
from app.models.rulebook import Rulebook
from app.resource import get_path


class UnusableRulebookError(Exception):
    """Set of rulebooks contains at least one unusable."""


class ClingoEngine:

    def __init__(self, _rulebooks: List[Rulebook]) -> None:
        self.rulebooks = RulebookValidator.filter(_rulebooks)
        self.ctl = self._create_control()
        self._is_usable()

    def _create_control(self) -> Control:
        ctl = Control()
        for path in ClingoEngine._get_facts() + self._get_rules():
            # print(f"load {lp}")
            ctl.load(path.as_posix())
        return ctl

    @staticmethod
    def _get_facts() -> List[Path]:
        return [get_path('hero_facts.lp')]

    def _get_rules(self) -> List[Path]:
        rules = []
        for book in self.rulebooks:
            rules.append(get_path(f"regelwerk/common.lp"))
            rules.append(get_path(f"regelwerk/{book}/meta.lp"))
            rules.append(get_path(f"regelwerk/{book}/rules.lp"))
        return rules

    def _is_usable(self) -> None:
        self.ctl.ground([(RulebookProgram.IS_USABLE, [])])
        unusables: List[List[str]] = []
        self.ctl.solve(on_model=lambda m: Collector.functions_strings(unusables, m, RulebookFunction.RULEBOOK_UNUSABLE))
        if unusables:
            messages = []
            for a in unusables:
                messages.append(f"Rulebook '{a[0]}' missing '{a[1]}'.")
            raise UnusableRulebookError(chr(10).join(messages))

    def check(self, hero: Hero, is_print_model: bool = False) -> bool:
        self.ctl.ground(context=HeroWrapper.wrap(hero))
        result: SolveResult = self.ctl.solve(on_model=lambda m: ClingoEngine._print_model(m, is_print_model))
        return result.satisfiable

    @staticmethod
    def _print_model(m: Model, is_print_model: bool):
        if is_print_model:
            print(m)

    def list(self, merkmal: Feature) -> List[str]:
        self.ctl.ground([(RulebookProgram.list(merkmal), [])])
        features: List[str] = []
        self.ctl.solve(on_model=lambda m: Collector.functions_first_string(features, m, RulebookFunction.of(merkmal)))
        return features
