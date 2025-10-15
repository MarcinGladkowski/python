"""
* -> asterisks
"""

# using for multiplication
result = 2 * 3


def add(*numbers):
    print(type(numbers))
    """
    Single asterisks * - args
    *args => returns tuple
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(add(1, 2, 3, 4, 5))


def add_numbers(number_1, number_2, number_3):
    """
    use asterisks to destructuring parameters
    """
    return sum([number_1, number_2, number_3])


numbers = [1, 2, 3]

print(add_numbers(*numbers))


def change_user_details(username, email, phone, date_of_birth):
    """
    **kwargs
    """
    pass


def change_user_details_kwargs(username, **kwargs):
    """
    kwargs => returns dictionary
    user.email = kwargs['email']
    user.phone = kwargs['phone']
    """
    pass


user_details = {
    'email': 'someuser@notexistsdomain.com',
    'phone': '123456789',
    'date_of_birth': '1990-08-29'
}

change_user_details('myuser', **user_details)


# Restricting
def keyword_arguments(*, keyword_arg_1):
    """
    Allows only keyword arguments only
    """
    pass


keyword_arguments(keyword_arg_1='test')


def positional_arguments(arg1, arg2, /):
    """
    Only positional arguments
    """
    pass


# positional_arguments(arg1='test', arg2='test2')


# Usage of * and ** in literals -> merging lists
list_1 = [1, 2, 3]
middle = 4
list_2 = [5, 6, 7]

list_3 = [*list_1, middle, list_2]


# Constructing dictionaries
social = {
    'twitter': 'some_user'
}

details = {
    'birthdate': '1990-07-29'
}

full_user_details = { 'username': 'user_1', **social, **details }

# destructing lists
my_list = [1, 2, 3]

a, *b, c = my_list # b -> rest of elements from the middle


def pow_(x, y, *, modulo=None):
    """
    Example of using * to force keyword arguments
    """
    return pow(x, y, modulo)

print('pow_ function result', pow_(2, 3, modulo=3))
