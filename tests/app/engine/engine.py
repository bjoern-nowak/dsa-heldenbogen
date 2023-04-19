from __future__ import annotations  # required till PEP 563

import logging
from typing import List

from dsaheldenbogen.app.engine.engine import Engine
from dsaheldenbogen.app.engine.rulebook_program import RulebookProgram
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.infrastructure.clingo_executor import ClingoExecutor

logger = logging.getLogger(__name__)


class TestEngine(Engine):
    """
    This is the actual engine for test implementations of rulebooks and hence having some modifications:
     - given rulebooks can be real ones or test implementations (TestRulebook), so mixing is possible
     - it does NOT validate given rulebooks
     - it does NOT check the rulebooks usability
    """

    def __init__(self, rulebooks: List[Rulebook]) -> None:
        self.rulebooks = rulebooks
        self.clingo_executor = ClingoExecutor(
            [r.entrypoint_file() for r in self.rulebooks],
            [RulebookProgram.BASE]
        )

        self._find_extra_hero_validation_steps()
        self.hero_validation_steps = dict(sorted(self.hero_validation_steps.items()))  # sort by keys
