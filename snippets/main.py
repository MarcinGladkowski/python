def sum_first_numbers(n):
    """Returns the sum of the first n natural numbers."""
    return n * (n + 1) // 2


def slow_sum_first_numbers(n):
    """Returns the sum of the first n natural numbers using a loop (less efficient)."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total



count = 1000000

print(sum_first_numbers(count))  # Output: 500000500000
print(slow_sum_first_numbers(count))  # Output: 500000500000