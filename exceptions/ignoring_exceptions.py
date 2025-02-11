from contextlib import suppress

data = {}


"""
Typical ignore exception while we can expect it
"""
try:
    del data['missing_index']
except:
    pass


"""
Using contex manager

more decent and elegant way
"""
with suppress(KeyError):
    del data['missing_key']

