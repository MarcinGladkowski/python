def prime_numbers(n):
    x = n ** 0.5

    for i in range(2, int(x)):
        if n % i == 0.0:
            return False
    return True


def better_prime_numbers(n, i=2):
    if n % i == 0.0 and n != i or n < 2:
        return False

    if i > int(n ** 0.5):
        return True

    return better_prime_numbers(n, i + 1)


assert False == better_prime_numbers(1)
assert False == better_prime_numbers(4)
assert False == better_prime_numbers(10)
assert False == better_prime_numbers(99)
assert False == better_prime_numbers(-2)
assert False == better_prime_numbers(0)
assert True == better_prime_numbers(2)
assert True == better_prime_numbers(3)
assert True == better_prime_numbers(7)
assert True == better_prime_numbers(29)
assert True == better_prime_numbers(89)
assert True == better_prime_numbers(97)
assert False == better_prime_numbers(99)
