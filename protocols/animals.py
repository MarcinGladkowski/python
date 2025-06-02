from typing import Protocol


"""
Protocols are resolving problem with inheritance.
They are focused only on the behavior of the class, not on the class hierarchy.
Submarine is an Swimmer because implements the methods of the Swimmer protocol.
"""

class Swimmer(Protocol):
    def dive(self): ...
    def swim(self): ...


class Submarine(Swimmer):
    def dive(self):
        print("Submarine diving")

    def swim(self):
        print("Submarine swimming")


