from contextlib import contextmanager


class SimpleContextManager:
    def __enter__(self):
        print("acquire")
        return "resource"

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("release")


with SimpleContextManager() as manager:
    print(manager)


@contextmanager
def simple_context_manager():
    print("acquire")
    try:
        yield "resource"
    finally:
        print("release")

with simple_context_manager() as manager:
    print(manager)