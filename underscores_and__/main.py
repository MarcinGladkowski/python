"""
From https://youtu.be/ALZmCy2u0jQ

It't conventions/hints
_ -> variable should be treated as private
__ -> prevent collision when someone extends this class (name mangling)


dir(object) -> get attributes from object

to access variable form __ it's only t.Test__baz but don't do it! -> this variable should be
using only in current class/instance
"""


class Test:
    def __init__(self) -> None:
        self.foo = 11
        self._bar = 23
        self.__baz = 42


t = Test()
