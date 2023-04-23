from __future__ import annotations  # required till PEP 563

import logging
import sys
from enum import Enum

logger = logging.getLogger(__name__)


# author: https://stackoverflow.com/users/2988730/mad-physicist
# source: https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility/35804945#35804945
def add_logging_level(level_name, level_num, method_name=None):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    `levelName` becomes an attribute of the `logging` module with the value
    `levelNum`. `methodName` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
    used.

    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present

    Example
    -------
    >>> add_logging_level('TRACE', logging.DEBUG - 5)
    >>> logging.getLogger(__name__).setLevel("TRACE")
    >>> logging.getLogger(__name__).trace('that worked')
    >>> logging.trace('so did this')
    >>> logging.TRACE
    5

    """
    if not method_name:
        method_name = level_name.lower()

    if hasattr(logging, level_name):
        raise AttributeError(f"{level_name} already defined in logging module")
    if hasattr(logging, method_name):
        raise AttributeError(f"{method_name} already defined in logging module")
    if hasattr(logging.getLoggerClass(), method_name):
        raise AttributeError(f"{method_name} already defined in logger class")

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # http://stackoverflow.com/a/13638084/2988730
    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message, *args, **kwargs):
        logging.log(level_num, message, *args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, log_for_level)
    setattr(logging, method_name, log_to_root)


add_logging_level('TRACE', logging.DEBUG - 5)


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
    TRACE = 'trace', logging.TRACE

    def __init__(self, uvicorn: str, python: int):
        self.uvicorn = uvicorn
        self.python = python

    @staticmethod
    def argparse(arg):
        """Make argument case in-sensitiv"""
        try:
            return LogLevel[arg.upper()]
        except KeyError:
            return arg

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
