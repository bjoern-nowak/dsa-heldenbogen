import unittest

from app.engine import RegelSet
from app.engine import Regelwerk
from app.models import Held


class TestRegelwerk(unittest.TestCase):
    def test_check_kultur(self):
        held = Held(
            spezies='Mensch',
            kultur='Thorwaler',
        )
        regelwerk = Regelwerk([RegelSet.DSA5_GRUND, RegelSet.DSA5_OPTIONAL])
        result = regelwerk.check(held, True)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
