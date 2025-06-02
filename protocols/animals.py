from typing import Protocol, runtime_checkable


"""
Protocols are resolving problem with inheritance.
They are focused only on the behavior of the class, not on the class hierarchy.
Submarine is an Swimmer because implements the methods of the Swimmer protocol.
Structural inheritance
"""

type GpsLocation = tuple[float, float]  # latitude, longitude

@runtime_checkable
class Swimmer(Protocol):
    """
    Protocols and type checking

    - Not possible to use isinstance() with Protocols
    - The typing module provides runtime decorators like @runtime_checkable
    - Not checking method signatures, but the presence of methods
    """
    def dive(self, depth: float) -> None: ...
    def swim(self, to: GpsLocation) -> None: ...


class Submarine(Swimmer):
    def dive(self, depth: float) -> None:
        print("Submarine diving")

    def swim(self, to: GpsLocation) -> None:
        print("Submarine swimming")

class Whale(Swimmer):
    def dive(self, depth: float) -> None:
        print("Whale ... something ... diving")

    def swim(self, to: GpsLocation) -> None:
        print("Whale ... something ... swimming")


class NotASwimmer:
    def dive(self, depth: float) -> float: # Signature of Swimmer.dive is not followed!!!
        print("Not a swimmer diving")

    def swim(self, to: GpsLocation) -> None:
        print("Not a swimmer swimming")


class Airplane:
    def fly(self, to: GpsLocation) -> None:
        print("Airplane flying")

def swim_around(swimmer: Swimmer) -> None:
    if not isinstance(swimmer, Swimmer):
        raise TypeError(f"{type(swimmer).__name__}? Not a swimmer!")
    swimmer.dive(50)
    swimmer.swim((39.912182, -72.053608))
    swimmer.swim((38.473770, -10.103880))


swim_around(Airplane()) # Raises TypeError: Airplane? Not a swimmer!


