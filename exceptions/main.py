"""
Notes based on https://realpython.com/python-raise-exception/

Not all exceptions are errors.
E.g. the StopIterationException is an example of this.
Incorrect exceptions contains 'Error'

You can raise two types of exceptions:
* Built-in exceptions (not need to import anything)
* User-defines exceptions

You can catch Error by try ... except code block

LBYL - look before you leap
EAFP - easier to ask forgiveness than permission


Remind!
Dunder attributes - __ double underscores at the begging

Catching a generic Exception is generally bad practice
"""


class GradeValueError(Exception):
    """
    Simple implementation of custom Error Exception

    * suffix Error
    * Common practice to add only 'pass' placeholder
    """
    pass


error = Exception('an error occured')
error.args # tuple with arguments


try:
    # do something
    42 / 0
except ZeroDivisionError as error:
    # e.g. logging
    # access to traceback
    tb = error.__traceback__
    raise # reraise LBYL


"""
'from' clause allow to chain exceptions
* both exceptions in traceback
* easier follow track of failing code
* 'from None' -> can hide previous exception traceback
"""
try:
    42 / 0
except Exception as error:
    raise ValueError from error
