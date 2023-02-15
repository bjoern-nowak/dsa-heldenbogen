import unittest

from app.models import Held
from app.models import Kultur
from app.service import RegelSet
from app.service import Regelwerk


class TestRegelwerk(unittest.TestCase):
    def test_check_kultur(self):
        held = Held(
            name='TestHeld',
            spezies='Mensch',
            kultur=Kultur.THORWALER,
        )
        regelwerk = Regelwerk([RegelSet.DSA5_GRUND, RegelSet.DSA5_OPTIONAL])
        result = regelwerk.check(held, True)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
