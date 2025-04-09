"""
Now it's your turn
You learn when you do, not when you read.j

Can you use contextmanager to create a context manager my_suppress that mimics contextlib.suppress?

E.g., the code below should run without raising an exception:

with my_suppress(TypeError):
    print(3 + "hey")
But the code below should raise a IndexError exception:

with my_suppress(TypeError):
    print("hey"[5])
"""
from contextlib import contextmanager


@contextmanager
def my_suppress(type_error):
    try:
        yield
    except IndexError:
        raise IndexError
    except type_error:
        pass


with my_suppress(TypeError):
    print(3 + "hey")


"""Should raise an exception"""
with my_suppress(TypeError):
    print("hey"[5])