"""
The idea is to returning instead of lists
- the code which is corresponding with lists ex. append() is not necessary
- the returning values are passing to yields
- we can easily change it into list using list(generator)
- in case of list we have to store a lot of data in (cause big memory consumption or OOM)
"""


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


result = index_words_iter('My name is Marcin')

list(index_words_iter('My name is Marcin'))

print(next(result))
print(next(result))
print(next(result))

"""
Example
"""
file_path = 'my_numbers.txt'


def read_data(path):
    with open(path) as f:
        for line in f:
            yield int(line)


numbers_iterator = read_data(file_path)
print(list(numbers_iterator))
"""
Second time is empty list [] because iterator iterates over all data and raise an 
StopIteration exception
"""
print(list(numbers_iterator))

"""
We can omit it by implementing the own Iterator Protocol
"""
class ReadVisits:
    """Implementation of own iterator"""
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield int(line)



"""
Generator expressions
- creating using ()
- returns an iterator which get only one value
"""


"""Bad solution for big amount of data"""
values = [len(x) for x in open(file_path)]

"""Returns generator object"""
it = (len(x) for x in open(file_path))


























