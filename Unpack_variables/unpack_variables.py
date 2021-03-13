'''
Don't get values by indexes ex. from Tuple
code is more clear and easy to understood
'''
example_tuple = ('Apple', 'Banana')

print(example_tuple[0], example_tuple[-1])

first, second = example_tuple # the same but more clear to read

print(first, second)

# form more complicated data stucture
snacks = [('Apple', 5), ('Banana', 10)]

for i, (name, price) in enumerate(snacks, 1):
    print(f"#{i} name:{name} cost {price}")


