"""
Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after
removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect
practice world

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use set
container to remove duplicated data automatically and then use sorted() to sort the data.
"""
from unittest import TestCase


def sort_and_remove_duplicates(param):
    elements = param.split(' ')
    unique = list(set(elements))
    unique.sort()
    return ' '.join(unique)


class TestRemoveDuplicates(TestCase):

    def test_remove_duplicates(self):
        self.assertEqual('again and hello makes perfect practice world', sort_and_remove_duplicates(
            'hello world and practice makes perfect and hello world again'
        ))
