"""
Based on @see https://www.bitecode.dev/
"""

def decorator(callback_function):
    def wrapper():
        print('before decoration')
        callback_function()
        print('after decoration')

    return wrapper


@decorator
def function_without_parameters():
    print('no parameters')


function_without_parameters()


def decorator_with_parameter(callback_function):
    def wrapper(*args, **kwargs): # get arguments
        """
        We need to get params in dynamically way
        by get
        - *args = positional_params
        - **kwargs = keyword_params
        - decorator works no matter the number of params we pass
        """
        print('before decoration')
        result = callback_function(*args, **kwargs)
        print('after decoration')
        return result
    return wrapper



@decorator_with_parameter
def function_with_parameters(first_parameter: str, second_parameter: str):
    return first_parameter + ' ' + second_parameter

result = function_with_parameters('first', 'second')

print(result)


from functools import wraps

def function_that_creates_a_decorator(upper_case=False):
    """
    What about configuring decorators ?
    e.g. decorator(upper_case=False)
    - we cannot do it same as code above - we need to create decorator
    """
    def simple_decorator(func):
        @wraps(func) # get func metadata e.g. docstring
        def wrapper(*args, **kwargs):
            if upper_case:
                print('UPPER CASE')
                result = func(*args, **kwargs)
            else:
                print('lower case')
                result = func(*args, **kwargs)
            return result
        return wrapper
    return simple_decorator # return the decorator


created_decorator = function_that_creates_a_decorator(True)


@created_decorator
def print_values(first_value: str, second_value: str):
    return first_value, second_value


print_values()


