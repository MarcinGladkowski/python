'''
* Thanks to keyword *with* it's possible to using many times code from try-finally
blocks
* module *contextlib* give us decorator *contextmanager* which is possible to
use our functions with *with*
'''


from threading import Lock
import logging
from contextlib import contextmanager

lock = Lock()
with lock:
    pass  #

lock.acquire()
try:
    pass
finally:
    lock.release()


def my_function():
    """
        Default error level is WARNINIG
        Only error() show message
    """
    logging.debug('Data to debug')
    logging.error('Error occurred')
    logging.debug('More data to debug')


my_function()


@contextmanager
def debug_logging(level):
    """
        Temporary set to custom level
    """
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
    print('* Inside:')
    my_function()

print('* After:')
my_function()


'''
Using with files is good practice to be sure the file (handle)
will be closed properly.
'''


with open('my_file.txt', 'w') as handle:
    handle.write('Some data!')


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_logger = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_logger)


with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is information!')
    logging.debug('Wont display!')
