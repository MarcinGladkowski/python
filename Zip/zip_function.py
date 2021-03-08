# soruce https://medium.com/techtofreedom/7-levels-of-using-the-zip-function-in-python-a4bd22ee8bcd

from itertools import zip_longest

matrix = [[1, 2, 3], [1, 2, 3]]

zip_matrix = zip(matrix)

print(zip_matrix)

print(list(zip_matrix))

# transpose
transposed_zip_matrix = [list(i) for i in zip(*matrix)]

print(transposed_zip_matrix)

# zip function can aggregate data from all iterables: lists, tuples, dictionaries, sets
ids = [1 , 2, 4]
persons = ['person1', 'person2', 'person3']

zip_ids_persons = zip(ids, persons)

print(zip_ids_persons) # returns zip object

# list of tuples
print(list(zip_ids_persons))

# from one list to n list to zip
sex = ['male', 'female']
unique_id = [1234, 2345]
job = ['programmer', 'owner']

zipped_3_lists = zip(unique_id, sex, job)

print(list(zipped_3_lists))

# What about unequal list provided to zip function ?
longest_id = [1, 2]
longest_person = ['person1', 'person2', 'person3']

print(list(zip_longest(longest_id, longest_person))) # fill None for id - person3

# How to unpack it ?
# use ASTERISKS
unpack_id, unpack_person = zip(*[(1, 'person1'), (2, 'person2')])
print(unpack_id) # 1, 2
print(unpack_person) # person1, person2

to_unpack_id, to_unpack_person = zip((1, 'person1'), (2, 'person2'))
print(to_unpack_id) # 1, 2
print(to_unpack_person) # person1, person2

# Use zip() with dictionaries

# easy update dictionary

persons = {1: 'person1', 2: 'person2'}

new_persons_ids = [3, 4]
new_persons_names = ['person3', 'person4']
# NO FOR
persons.update(zip(new_persons_ids, new_persons_names))

print(persons)