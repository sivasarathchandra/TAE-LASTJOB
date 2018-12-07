import logging
import sys
"""This is used for logging all the debug level of data."""
class loggingFE():
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(stream_handler)