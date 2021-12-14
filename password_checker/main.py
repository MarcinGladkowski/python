import re


def at_least_one_number(password) -> tuple:
    return (True,) if len(re.findall(r'\d', password)) else (False, 'Password must contain one number at least')


def at_least_one_big_letter(password):
    return (True,) if len(re.findall(r'\W', password)) else (False, 'Password must contain one big letter at least')


def at_least_numbers_of_chars(password):
    return (True, ) if len(password) >= 8 else (False, 'Password must contain 8 characters at least!')


def at_least_one_special_chart(password):
    return (True, ) if len(re.findall(r'!|@|#', password)) else (False, 'Password must contain one from specials charts!')


def starts_with_upper(password):
    return password[0].isupper()