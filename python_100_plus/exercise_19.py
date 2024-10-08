"""
Question 19
Level 3

Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is
string, age and height are numbers. The tuples are input by console. The sort criteria is: 1: Sort based on name; 2:
Then sort based on age; 3: Then sort by score. The priority is that name > age > score. If the following tuples are
given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program
should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
 We use itemgetter to enable multiple sort keys.

Solutions: from operator import itemgetter, attrgetter
"""
import operator

input = 'Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85'


def sort_users(data):
    splited = data.split(' ')
    users_tuples = [tuple(x.split(',')) for x in splited]
    users_tuples.sort (key=operator.itemgetter(0, 1, 2))
    return users_tuples


assert [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')] == \
       sort_users(input)
