"""
Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then
check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
from unittest import TestCase


def divide_by_5(data):
    binary_digits = data.split(',')
    result = []
    for digit in binary_digits:
        if int(digit, 2) % 5 == 0:
            result.append(digit)

    return ','.join(result)


class TestFindBinaryDividesBy5(TestCase):

    def test_find_numbers(self):

        print(divide_by_5('0100,0011,1010,1001'))

        assert divide_by_5('0100,0011,1010,1001') == '1010'
