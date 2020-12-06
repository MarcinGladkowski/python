# source: https://medium.com/better-programming/mutable-default-arguments-in-python-643ae2583e00

# immutable: int, float, bool, str, tuple, Unicode
# mutable: list, set, dict

def foo_bar(element, data=[]):
    data.append(element)
    return data

# default arguments are creating when function is declared
print(foo_bar(12))
print(foo_bar(13))
print(foo_bar(14))
# result is [12, 13, 14]

# tuple with default values __defaults__
print(foo_bar.__defaults__)


def foo_bar_immutable(elemenet, data=None):
    if data is None:
        data = []
    data.append(elemenet)
    return data


print(foo_bar_immutable(1))
print(foo_bar_immutable(2))
print(foo_bar_immutable(3))

