import os

dirs = os.listdir(os.getcwd())


def snake_case(name: str):
    result = ''
    for i, l in enumerate(name):

        if l.isupper() and i == 0:
            result += l.lower()
            continue

        if l.isupper() and i != 0:
            result += '_' + l.lower()
            continue

        result += l

    return result


for dir in dirs:
    if not dir.startswith('.') and os.path.isdir(dir):
        os.rename(dir, snake_case(dir))


assert snake_case('PrimeNumbers') == 'prime_numbers'
