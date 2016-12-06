import logging
from django.conf import settings

from logging.handlers import RotatingFileHandler

class loggers(object):
    active_loggers = dict()
def getLogger(name=None):
    if loggers.active_loggers.has_key(name or 'base'):
        return loggers.active_loggers[name or 'base']

    logger = logging.getLogger(name)
    loggers.active_loggers[name] = logger
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
    file_handler = RotatingFileHandler(settings.LOG_FILE, 'a', 1000000, 1)
    file_handler.setLevel(getattr(logging,settings.LOG_LEVEL))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


loggers.active_loggers["base"] = getLogger()