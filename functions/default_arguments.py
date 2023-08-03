from time import sleep
from datetime import datetime
import json
from typing import Optional

"""
From where the default argument problem comes from ?
The Python initializes default arguments once when the module starts 
this mean the 'when' parameter will be the same for each call! 
"""


def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('Hello')
sleep(1)
log('Hello after sleep!')
"""The datetime is the same!"""

"""
How to prevent this situation ?
- use a NONE type as default value and use a docstring
"""


def super_log(message, when=None):
    """For displaying an message to console

    Arguments:
        message: message to display
        when: Date and time when it's happen
    """

    if when is None:
        when = datetime.now()

    print(f'{when}: {message}')


super_log('super')
sleep(1)
super_log('super again')

"""Another example"""


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['test'] = 1
bar = decode('also bad data')
bar['test_2'] = 2

assert foo is bar  # this is reference to the same default value

"""Using optional annotation"""


def super_decode(data, when: Optional[datetime] = None):
    if when is None:
        when = datetime.now()
        # ...
