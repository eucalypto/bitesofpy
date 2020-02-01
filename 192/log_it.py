import logging
from typing import Callable

pyb_logger = logging.getLogger('pybites_logger')

DEBUG = pyb_logger.debug
INFO = pyb_logger.info
WARNING = pyb_logger.warning
ERROR = pyb_logger.error
CRITICAL = pyb_logger.critical


def log_it(level: Callable, msg: str) -> None:
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
