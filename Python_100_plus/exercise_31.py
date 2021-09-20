"""
Define a function that can accept two strings as input and print the string with maximum length in console.
 If two strings have the same length, then the function should print all strings line by line.
"""


def which_longer(value_1, value_2):
    value_1_len, value_2_len = len(value_1), len(value_2)

    if value_1_len > value_2_len:
        return value_1_len
    elif value_2_len > value_1_len:
        return value_2_len
    else:
        return value_1_len + value_2_len
