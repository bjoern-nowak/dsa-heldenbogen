from __future__ import annotations  # required till PEP 563

from dsaheldenbogen.app.models.rulebook import Rulebook
from tests.app.testing_resource import TestingResource


class TestingRulebook(Rulebook):
    RES = TestingResource
