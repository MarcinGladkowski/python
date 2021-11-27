import re

print(re.sub(r"a", "b", "banana"))

print(re.sub(r"\d", "X", 'This is secret amount 1234$'))
