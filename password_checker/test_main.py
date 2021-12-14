from main import at_least_one_number, at_least_numbers_of_chars, at_least_one_special_chart, starts_with_upper

assert False is at_least_one_number('test')[0]
assert 'Password must contain one number at least' == at_least_one_number('test')[1]
assert True is at_least_one_number('test2')[0]


assert True is at_least_numbers_of_chars('12345678')[0]
assert False is at_least_numbers_of_chars('1234567')[0]
assert True is at_least_numbers_of_chars('123456789')[0]

assert True is at_least_one_special_chart('ts!Are')[0]
assert False is at_least_one_special_chart('test')[0]

assert True is starts_with_upper('Test')
assert False is starts_with_upper('test')

