import logging
"""FROM https://realpython.com/python-logging/"""

"""
Log levels:
- NOTSET
- DEBUG debug()
- INFO info()
- WARNING warning()
- ERROR error()
- CRITICAL critical()


:root: name for default logger
"""
# logging.warning("This is a warning")

"""
Lets run logging

set logging level
"""

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)  # must be set before any log function

# NOTSET 0
logging.debug('This is a debug message')  # 10
logging.info('This is an info message')  # 20
logging.warning('This is a warning message')  # 30
logging.error('This is an error message')  # 40
logging.critical('This is a critical message')  # 50
"""
As default the messages not logged to console for INFO and DEBUG because default log level is WARNING. 
Logger log only levels for WARNING and above.
"""

"""Logging to a file"""
logging.basicConfig(
    filename="app.log",
    encoding='utf-8', # file encoding
    filemode='a', # append mode
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

"""Display variables"""
name="developer"
logging.debug("name=%s", name) # by %s interpolation


"""Logging stacktrace"""
try:
    10 / 0
except ZeroDivisionError:
    logging.error("Calculation error", exc_info=True)
    # OR
    logging.exception("Calculation error") # better way of logging exception stacktrace













