import logging
import sys
class loggingAPI():
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(stream_handler)