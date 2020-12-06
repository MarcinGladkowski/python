# sources:
# - https://bulldogjob.pl/news/1016-4-czeste-bledy-poczatkujacych-pythonowcow
# - https://bulldogjob.pl/news/1076-pisz-lepszy-kod-w-pythonie

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


# using f-strings to formatting for strings
first_name = 'Jan'
last_name = 'Kowalski'
middle_name = 'Marcin'
# using %
print("You are a great programmer, %s %s %s" % (first_name, middle_name, last_name))
# using str.format
print("You are a great programmer, {} {} {}".format(first_name, middle_name, last_name))
# and using f-strings
print(f"You are a great programmer, {first_name} {middle_name} {last_name}")

# List comprehension
# Doing the same thing for all elements in list
# Traditional way:
numbers = [1, 2, 3]
extended_numbers = []
for elem in numbers:
    extended_numbers.append(elem * 2)


print(numbers)

print(extended_numbers)
# Change for it:
new_extended_list = [item * 2 for item in numbers]

print(new_extended_list)

# more complicated example - a few functions:


def process(item):
    item = item * 2
    item = item / 5
    return item


new_list = [process(item) for item in numbers]
print(new_list)
new_list2 = list(map(process, numbers))
print(new_list2)

# easy filtering using list comprehension
filtered = [item for item in numbers if item > 5]
