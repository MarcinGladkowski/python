"""
Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def even_numbers():
    return ','.join([str(x) for x in range(1000, 3001) if x % 2 == 0])


print(even_numbers())