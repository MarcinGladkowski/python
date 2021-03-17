'''
sort() works with numbers, floats, strings etc.
'''

numbers = [20, 2, 1, 8, 99]

numbers.sort()

print(numbers)

'''
Case sensitive sorting
'''
cities = ['New York', 'San Francisco', 'Miami', 'Atlanta', 'boston']
cities.sort()
print(cities) # boston is last :/

cities.sort(key=lambda x:x.lower())
print(cities) # boston is second!


'''
Sorting objects
- they need to have implemented magic method __repr__() 
'''


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('screwdriver', 0.5),
    Tool('hammer', 2.0),
    Tool('key', 1.5)
]
# Without specify key for sort it's throw an error
# print(tools.sort())

tools.sort(key=lambda x: x.name)
print(tools)
tools.sort(key=lambda x: x.weight)
print(tools)

'''
Sorting using many keys and Tuples // 68
'''
