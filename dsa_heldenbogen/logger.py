import logging
import sys

import main

# TODO check what config stream sys.stderr does
log_level: int = logging.DEBUG if main.config.should_reload else logging.INFO
logging.basicConfig(stream=sys.stderr, level=log_level)


#
# Convenience methods: so that this package can be used as logging wrapper
#

def debug(msg, *args, **kwargs):
    """
    Delegate a debug call to the underlying logging.
    """
    logging.log(logging.DEBUG, msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """
    Delegate an info call to the underlying logging.
    """
    logging.log(logging.INFO, msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Delegate a warning call to the underlying logging.
    """
    logging.log(logging.WARNING, msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """
    Delegate an error call to the underlying logging.
    """
    logging.log(logging.ERROR, msg, *args, **kwargs)


def exception(msg, *args, exc_info=True, **kwargs):
    """
    Delegate an exception call to the underlying logging.
    """
    logging.log(logging.ERROR, msg, *args, exc_info=exc_info, **kwargs)


def critical(msg, *args, **kwargs):
    """
    Delegate a critical call to the underlying logging.
    """
    logging.log(logging.CRITICAL, msg, *args, **kwargs)
