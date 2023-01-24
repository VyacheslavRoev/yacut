import logging
from logging.handlers import RotatingFileHandler

from .constants import (BASE_DIR, DT_FORMAT, LOG_FORMAT, SECRET_KEY,
                        SQLALCHEMY_DATABASE_URI)


class Config(object):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def configure_logging():
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'yacut_logger.log'
    rotating_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 ** 6,
        backupCount=5,
        encoding="UTF-8"
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
