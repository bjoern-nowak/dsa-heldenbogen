from __future__ import annotations  # required till PEP 563

import logging
import sys
from enum import Enum

logger = logging.getLogger(__name__)


def init_config(level: LogLevel):
    logging.basicConfig(
        stream=sys.stderr,  # TODO check what config stream sys.stderr does
        level=level.python,
        # TODO may add session/request info or %(process)d %(processName)s %(thread)d %(threadName)s
        format='%(asctime)s.%(msecs)03d [%(levelname)-8s] [%(thread)-15d] %(name)s - %(message)s',
        datefmt='%y-%m-%d %H:%M:%S'
    )
    logger.info(f"Default logger configured with level {level}")


class LogLevel(Enum):
    CRITICAL = 'critical', logging.CRITICAL
    ERROR = 'error', logging.ERROR
    WARNING = 'warning', logging.WARNING
    INFO = 'info', logging.INFO
    DEBUG = 'debug', logging.DEBUG
    TRACE = 'trace', logging.DEBUG

    def __init__(self, uvicorn: str, python: int):
        self.uvicorn = uvicorn
        self.python = python

    @staticmethod
    def argparse(s):
        """Make argument case in-sensitiv"""
        try:
            return LogLevel[s.upper()]
        except KeyError:
            return s

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
