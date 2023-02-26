from pathlib import Path
from typing import List

from clingo import Control
from clingo import Model
from clingo import SolveResult

from app.engine.hero_wrapper import HeroWrapper
from app.engine.rulebook_program import RulebookProgram
from app.engine.rulebook_validator import RulebookValidator
from app.models import Held
from app.models.feature import Feature
from app.resource import get_path
from app.service import Regelwerk


class ClingoEngine:

    def __init__(self, _rulebooks: List[Regelwerk]) -> None:
        rulebooks = RulebookValidator.filter(_rulebooks)
        rules: List[Path] = self._get_rules(rulebooks)
        hero_facts: Path = get_path('hero_facts.lp')
        self.ctl = ClingoEngine._create_control([hero_facts], rules)

    @staticmethod
    def _get_rules(rulebooks: List[Regelwerk]) -> List[Path]:
        rules = []
        for book in rulebooks:
            rules.append(get_path(f"regelwerk/{book.value}/meta.lp"))
            rules.append(get_path(f"regelwerk/{book.value}/base_rules.lp"))
        return rules

    @staticmethod
    def _create_control(facts: List[Path], rules: List[Path]) -> Control:
        ctl = Control()
        for lp in facts + rules:
            # print(f"load {lp}")
            ctl.load(lp.as_posix())
        return ctl

    def check(self, held: Held, is_print_model: bool = False) -> bool:
        self.ctl.ground(context=HeroWrapper.wrap(held))
        result: SolveResult = self.ctl.solve(on_model=lambda m: self._print_model(m, is_print_model))
        return result.satisfiable

    def _print_model(self, m: Model, is_print_model: bool):
        if is_print_model:
            print(m)

    def list(self, merkmal: Feature) -> List[str]:
        self.ctl.ground([(RulebookProgram.list(merkmal), [])])
        merkmale = []
        self.ctl.solve(on_model=lambda m: ClingoEngine._collect_symbols(merkmale, m))
        return merkmale

    @staticmethod
    def _collect_symbols(found: List[str], model: Model):
        for sym in model.symbols(shown=True):
            for arg in sym.arguments:
                found.append(arg.string)
