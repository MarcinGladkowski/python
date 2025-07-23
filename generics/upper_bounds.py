from collections.abc import Sequence
from typing import Protocol

class HasArea(Protocol):
    def area(self) -> float: ...

def sort_by_area[T: HasArea](shapes: Sequence[T]) -> Sequence[T]:
    return sorted(shapes, key=lambda shape: shape.area())