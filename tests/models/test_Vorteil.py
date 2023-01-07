import unittest

from pydantic import IntegerError
from pydantic import NumberNotGtError
from pydantic import StrError
from pydantic import ValidationError

from dsa_heldenbogen.models import Vorteil
from tests.models.pydantic_util import assert_errors


class TestVorteil(unittest.TestCase):
    valid = Vorteil(name='name',
                    beschreibung='beschreibung',
                    voraussetzung='voraussetzung',
                    kosten=1)

    def test_valid(self):
        self.assertIsInstance(self.valid, Vorteil)

    def test_does_cost(self):
        with self.assertRaises(ValidationError) as context:
            invalid = {'kosten': 0}
            self.valid.copy(update=invalid)
        assert_errors(self, context.exception, invalid.keys(), NumberNotGtError, limit_value=0)

        with self.assertRaises(ValidationError) as context:
            invalid = {'kosten': -1}
            self.valid.copy(update=invalid)
        assert_errors(self, context.exception, invalid.keys(), NumberNotGtError, limit_value=0)

    def test_level_must_be_positive(self):
        with self.assertRaises(ValidationError) as context:
            invalid = {'stufen': 0}
            self.valid.copy(update=invalid)
        assert_errors(self, context.exception, invalid.keys(), NumberNotGtError, limit_value=0)

        with self.assertRaises(ValidationError) as context2:
            invalid = {'stufen': -1}
            self.valid.copy(update=invalid)
        assert_errors(self, context2.exception, invalid.keys(), NumberNotGtError, limit_value=0)

    def test_strict_numbers(self):
        with self.assertRaises(ValidationError) as context:
            invalid = {'stufen': '1', 'kosten': '1'}
            self.valid.copy(update=invalid)
        assert_errors(self, context.exception, invalid.keys(), IntegerError)

    def test_strict_strings(self):
        with self.assertRaises(ValidationError) as context:
            invalid = {'name': 1, 'beschreibung': 1, 'voraussetzung': 1, 'reichweite': 1}
            self.valid.copy(update=invalid)
        assert_errors(self, context.exception, invalid.keys(), StrError)


if __name__ == '__main__':
    unittest.main()
