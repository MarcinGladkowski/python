
def prime_numbers(n):
    x = n**0.5

    for i in range(2, int(x)):
        if n % i == 0.0:
            return False
    return True


def better_prime_numbers(n, i=2):
    if n % i == 0.0:
        return False

    if i > int(n**0.5):
        return True

    return better_prime_numbers(n, int(n ** 0.5) + i)




