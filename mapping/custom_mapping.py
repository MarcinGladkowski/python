from collections.abc import Mapping, MutableMapping
"""Source https://realpython.com/python-mappings/"""

class PizzaMenu(Mapping):
    """
    MutableMapping requires to implement methods
    __delitem__()
    __setitem__()
    """
    def __init__(self, menu: dict):
        self._menu = menu

    def __getitem__(self, item):
        return self._menu[item]

    def __iter__(self):
        return iter(self._menu)

    def __len__(self):
        return len(self._menu)

    def __repr__(self):
        """
        This method produces output that can be used to re-create the object.

        More Pythonic way than type(self).__name__
        """
        return f"{self.__class__.__name__}({self._menu})"

    def __str__(self):
        return str(self._menu)

    def __contains__(self, key):
        """
        Python uses this method to check membership
        """
        return key in self._menu


menu = PizzaMenu({"Margherita": 9.6})
print(menu)