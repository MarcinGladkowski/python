"""
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints: Use timeit() function to measure the running time.
"""
import timeit


def sum_numbers():
    return 1 + 1


print(timeit.timeit(stmt=sum_numbers, number=10000))
