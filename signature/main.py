from inspect import signature

def my_join(left: str, right: str, sep: str = " ") -> str:
    return left + sep + right

sig = signature(my_join)
print(sig)  # (left: str, right: str, sep: str = ' ') -> str
print(type(sig))  # <class 'inspect.Signature'>
print(sig.parameters)  # OrderedDict([('left', <Parameter "left: str">), ('right', <Parameter "right: str">), ('sep', <Parameter "sep: str = ' '">)])