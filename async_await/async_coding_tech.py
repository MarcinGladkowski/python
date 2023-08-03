import asyncio

"""
Based on examples in https://www.youtube.com/watch?v=VTl9WNP7GCU&ab_channel=CodingTech
"""


async def hello():
    print('Hello!')
    await asyncio.sleep(1)
    print('Goodbye')


async def main():
    await asyncio.gather(hello(), hello())


asyncio.run(main())


def generate_even_numbers(start, end):
    """
    Function to generate even numbers in range
    In classic way for 99999 we have to wait
    """
    even_numbers = []
    for number in range(start, end):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def generate_even_numbers_generator(start, end):
    """
    Function using generators
    """
    for number in range(start, end):
        if number % 2 == 0:
            yield number


generator = generate_even_numbers_generator(2, 10)
print(next(generator))
print(next(generator))
print(next(generator))
# or
for i in generator:
    print(i)
