import types
from functools import wraps


'''
Class decorator get class instance and can return the new one or modify it
It helps to modify methods and attributes of class
It's more flexible than metaclasses

'''


def my_class_decorator(klass):
    klass.extra_param = 'Hello'
    return klass


@my_class_decorator
class MyClass:
    pass


print(MyClass)
print(MyClass.extra_param)


def trace_func(func):
    if hasattr(func, 'tracing'):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f'{func.__name__}({args!r}), ({kwargs!r}) -> {result!r}')

    wrapper.tracing = True
    return wrapper


trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType
)


def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass


@trace
class TraceDict(dict):
    pass


trace_dict = TraceDict([('Hello', 1)])
trace_dict['dude'] = 2
trace_dict['Hello']
try:
    trace_dict['dont exist']
except KeyError:
    pass
