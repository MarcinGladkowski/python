"""
Enumerate is using to iterate over elements with index
It's an iterator.
"""


names = ['Bob', 'Martin', 'Ben']

for index, name in enumerate(names):
    print(f"name: {name}, index: {index}")


print(enumerate(names))

print(list(enumerate(names)))
