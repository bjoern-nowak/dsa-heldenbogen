from __future__ import annotations  # required till PEP 563

from dsaheldenbogen.app.models.rulebook import Rulebook
from tests.app.resource import TestResource


class TestRulebook(Rulebook):
    RES = TestResource
