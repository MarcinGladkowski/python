"""
Level 2

Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console
"""
import re


def calculate_bank_amount(data):
    operations = re.findall('[D|W]\s{1}[0-9]{3}', data)
    total = 0
    for x in operations:
        if x.startswith('D'):
            match = re.search('[0-9]+', x)
            total += int(match.group(0))
        if x.startswith('W'):
            match = re.search('[0-9]+', x)
            total -= int(match.group(0))

    return total


assert calculate_bank_amount('D 300 D 300 W 200 D 100') == 500