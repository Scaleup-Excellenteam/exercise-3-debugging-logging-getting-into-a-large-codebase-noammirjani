import logging


logFile = 'logs.log'


def get_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and add it to the logger
    handler = logging.FileHandler(logFile)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger

