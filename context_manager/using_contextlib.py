from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwargs):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)


"""Equivalent to class context manager"""
class ManagedResource:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.resource = None

    def __enter__(self):
        self.resource = acquire_resource(*self.args, *self.kwargs)
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        release_resource(self.resource)