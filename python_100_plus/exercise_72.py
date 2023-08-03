"""
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints: Use if/elif to deal with conditions.
"""

elements = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(n: list, x: int):
    half = int(round(len(n) / 2, 0))

    if n[0] == x:
        print(f"found! {n}")
        return

    if x > half:
        binary_search(n[half:], x)
    else:
        binary_search(n[:half], x)


binary_search(elements, 6)