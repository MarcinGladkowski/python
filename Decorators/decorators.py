from functools import wraps


def trace(func):
    @wraps(func) # to fix the reference to function
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) 'f'->  {result!r}')
        return result

    return wrapper


@trace
def fibonacci(n):
    """Value n number from Fibonacci"""
    if n in (0, 1):
        return n
    return fibonacci(n-2) + fibonacci(n - 1)


fibonacci(4)
print(fibonacci) # function trace -> not fibonacci!
help(fibonacci)

