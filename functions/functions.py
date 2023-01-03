def get_stats():
    return 1, 2


print(get_stats())  # return as tuple!

'''
- Functions shouldn't return more than 2 variables
- Functions shouldn't return some variables when result isn't expected - don't return None, False, empty string
- Good behaviour is raise an Exception
- Document raised exceptions
- You can add type hinting also
'''


def careful_divide(a: float, b: float) -> float:
    """Divide two float numbers

    Raise:
        ValueError: when dividing isn't possible

    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Incorrect input data')


'''
Python functions can be:
- passed as arguments to other functions
- returned as values from other functions
- assigned to variables and stored also in lists
'''


def some_function():
    pass


functions_list = []
functions_list[some_function]

# function_list[0]() <- to call it
