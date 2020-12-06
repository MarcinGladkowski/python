# source: https://bulldogjob.pl/news/1016-4-czeste-bledy-poczatkujacych-pythonowcow

# use iterators
my_list = [1, 2, 3]

# instead of
for i in range(len(my_list)):
    print(my_list[i])

# do
for element in my_list:
    print(element)

# use enumerate() when you want access to indexes


# Using global variables (bad practice)
# using global const its good pratice

a = 1


def increment():
    a += 1
    return a


def increment_global():
    global a
    a += 1
    return a


# Mutable objects
# Build in not mutable objects: int, float, string, bool, tuple
example_string = 'test'
# example_string[0] = 'a' # type error!

# Build in mutable objects: list, set, dict
example_list = ['a', 'b']
example_list[0] = 'c' # works!


# problem with default arguments:
def foo(el, some_list=[]):
    some_list.append(el)
    return some_list


print(foo(1)) # 1
print(foo(2)) # 1,2

# to fix this add default argument as type = NONE
# How to fix it?


def foo2(el, some_list=None):
    if some_list is None:
        some_list = []
    some_list.append(el)
    return some_list



