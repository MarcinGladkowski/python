"""
JSON data type
- object
- array
- string
- number
- boolean
- null

JSON syntax pitfalls
- using only double quotes for strings
- any inlines comments
- trailing comma after final key-pair value
- trailing comma after last element in array


data -> JSON file (serialization)
JSON file -> data (deserialization)

"""

import json

"""Serializing to JSON"""
food_ratings = {
    "organic food": 2,
    "human food": 10,
    1: 20,
    2: True
}
print(json.dumps(food_ratings))

"""
Not all of data type can be used as JSON key: 
- dict
- list
- tuple

Note: dictionaries and tuples are not hashable
"""

"""Automatic skip not possible keys without throwing TypeError"""
json.dumps({}, skipkeys=True)

"""write JSON file"""
with open('developer.json', 'w', encoding='utf-8') as outfile:
    json.dump(food_ratings, outfile)

"""
Reading JSON FILES

json.loads() - your data presents in python program
json.load() - external files saved on disk

NOTE: null will be presented as None
"""

user = {"name": "John"}

print(json.dumps(user))

