class MyBaseClass:
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self, value):
        super().__init__(value, 5)


"""Multiple Inheritance"""
class TimesTwo:
    def __init__(self) -> None:
        self.value *= 2


class PlusFive:
    def __init__(self) -> None:
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


"""
Diamond Inheritance
- super() keyword prevent to make unexpected order of __init__() method 
- MRO - method resolution order (C3 linearization algorithm)
- get order of initializaton <class>.mro()
"""
class TimesTwoCorrect(MyBaseClass):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value *= 2


class PlusNineCorrect(MyBaseClass):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value *= 9


class GoodWay(TimesTwoCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)