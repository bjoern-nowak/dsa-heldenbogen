import logging
import sys

logger = logging.getLogger(__name__)


def init_config():
    logging.basicConfig(
        stream=sys.stderr,  # TODO check what config stream sys.stderr does
        level=logging.DEBUG,
        # TODO may add session/request info or %(process)d %(processName)s %(thread)d %(threadName)s
        format='%(asctime)s.%(msecs)03d [%(levelname)-8s] [%(thread)-15d] %(name)s - %(message)s',
        datefmt='%y-%m-%d %H:%M:%S'
    )
    logger.info(f"Default logger configured.")
