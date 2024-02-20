"""
Case 1 - intercepting calls

Let's consider behaviour of functools.cache
If for the same parameters has value, then doesn't
execute function but instead returns cached value
"""

import functools
import time


def basic_throttle(calls_per_second):
    def decorator(func):

        last_called = 0.0
        count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called, count
            current_time = time.time()

            # Reset counter if new second
            if current_time - last_called >= 1:
                last_called = current_time
                count = 0

            # enforce the limit
            if count < calls_per_second:
                count += 1
                return func(*args, **kwargs)

            return None

        return wrapper

    return decorator


@basic_throttle(5)
def send_alert():
    print("Alert !")


# breaks after 5 call
for i in range(10):
    send_alert()

"""
Case 2 - registering the function
- using reference of function
"""

"""
Case 3 - enrich the call
- add additional behaviour
"""


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.3f} seconds")
        return result

    return wrapper
