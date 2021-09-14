"""
Level 3

Question: Write a program to compute the frequency of the words from the input. The output should output after sorting
the key alphanumerically. Suppose the following input is supplied to the program:

'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'

 Then, the output should be: 2:2 3:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

Hints In case of input data being supplied to the question, it should be assumed to be a console input.
"""
from collections import OrderedDict


def words_frequency(input):
    result = OrderedDict()
    for word in input.split(" "):
        if result.get(word) is not None:
            result[word] = result[word] + 1
        else:
            result[word] = 1

    for key in sorted(result):
        result.move_to_end(key)

    to_print = ''
    for elem in result:
        to_print += f"{elem}:{result[elem]} "

    return to_print.strip()


assert "2:2 3:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1" == \
       words_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3")
