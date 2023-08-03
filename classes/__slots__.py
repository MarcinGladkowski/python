"""
__slots__
* Useful for lightweight classes - limits memory usage
* Prevents automatic adding attrs to __dict__
* Prevents adding new attributes dynamically
"""


class Point:
    """
    Cannot call __dict__ attr on this class!
    """
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int) -> None:
        self.y = y
        self.x = x


