countries = {
    'Poland': 10,
    'Canada': 1
}

# 4 methods to check and get keys
key = 'USA'

# 1
if key in countries:
    counter = countries[key]
else:
    counter = 0

countries[key] = counter + 1

# 2
try:
    counter = countries[key]
except KeyError:
    counter = 0

countries[key] = counter + 1

# 3
counter = countries.get(key, 0)
countries[key] = counter + 1

# 4
counter = countries.setdefault(key, 0)
countries[key] = counter + 1
