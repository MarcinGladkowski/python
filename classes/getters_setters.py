"""
Don't implement getters and setters for classes!
* You can use decorators for it!
* Try to using only public visibility
* You can use @property when access to prop have been under strict control
* @property is built-in decorator
"""

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms += 5e3

print(r1.ohms)


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        print('setter called!')
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(100)
print(r2.current)

r2.voltage = 10
print(r2.current)


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms < 0:
            raise ValueError
        self._ohms = ohms


r3 = BoundedResistance(10)
'''Using this operator the method @ohms.setter is called'''
# r3.ohms = -4 ValueError!

