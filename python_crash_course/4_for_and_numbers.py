# 4.3
for number in range(21):
    print(number)

# 4.4
billion_numbers = []
for x in range(1_000_001):
    billion_numbers.append(x)

# 4.5
print(max(billion_numbers))
print(min(billion_numbers))
print(sum(billion_numbers))


# 4.6
# using list comprehension, instead of append method on list
odd_numbers = [x for x in range(0, 20, 3)]
print(odd_numbers)

# 4.7
to_cube = [x**3 for x in range(3, 31)]
print(to_cube)

for cube_number in to_cube:
    print(cube_number)

# 4.8
to_cube_first_10 = []
for x in range(11):
    to_cube_first_10.append(x**3)


for x in to_cube_first_10:
    print(x)

# 4.9
to_cube_first_10_comprehension = [x**3 for x in range(11)]
print(to_cube_first_10_comprehension)


