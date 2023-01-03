"""
Level 2

Question: Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
from unittest import TestCase
import re


def sentence_counter(sentence):
    letters = re.findall('[a-z]', sentence)
    numbers = re.findall('[0-9]', sentence)

    return f"LETTERS {len(letters)} DIGITS {len(numbers)}"


class TestSentenceCounter(TestCase):

    def test_should_return_correct_numbers(self):
        self.assertEqual("LETTERS 10 DIGITS 3", sentence_counter('hello world! 123'))
