import logging


def create_logger(log_handler):
    logger = logging.getLogger(log_handler)
    return logger
