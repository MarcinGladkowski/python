"""
Exercise: print Hello world without using brackets in code!
"""

class X:
    __init__ = lambda x, y: None
    __lt__ = print

@X
class Y:
    pass


Y < "Hello world"