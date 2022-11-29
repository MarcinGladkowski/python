numbers = [1, 2, 3, 4]

squared_numbers = map(lambda x: x ** 2, numbers)

print(list(squared_numbers))
print(type(squared_numbers))


def square(number):
    """
    Simplify the map function by passing a function
    """
    return number ** 2


print(
    list(map(square, numbers))
)
