import unittest

from src.app import logger


class BaseTestCase(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        logger.init_config(logger.LogLevel.WARNING)


if __name__ == '__main__':
    unittest.main()
