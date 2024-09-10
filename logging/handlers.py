import logging

"""
Useful when we want to set logger messages into multiple places
"""

logger = logging.getLogger(__name__)

"""
Another types of loggers
- RotatingFileHandler
- TimedRotatingFileHandler
"""
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode='a', encoding='utf-8')

"""Add formatters"""
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

console_handler.setFormatter(formatter)



logger.addHandler(console_handler)
logger.addHandler(file_handler)


"""For now the log level is NOTSET"""

logger.warning("Some warning message")