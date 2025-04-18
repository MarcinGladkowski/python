"""
Level 2

Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
 Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
"""
from unittest import TestCase
import re


def countLowersAndUppers(param: str):
    lowers = re.findall('[a-z]', param)
    uppers = re.findall('[A-Z]', param)

    return f"UPPER CASE {len(uppers)} LOWER CASE {len(lowers)}"


class TestCountLowersAndUppers(TestCase):

    def test_count_uppers_and_lowers(self):
        self.assertEqual(countLowersAndUppers('Hello world!'), 'UPPER CASE 1 LOWER CASE 9')
