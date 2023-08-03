from collections import defaultdict


'''
Usage of method defaultdict isn't clear
'''


visits = {
    'Poland': {'Katowice', 'Warszawa'},
    'Czech': {'Prague'}
}
# short version
visits.setdefault('France', set()).add('Paris')

# longer
if (japan := visits.get('Japan')) is None:
    visits['Japan'] = japan = set()
    japan.add('Kioto')


# try to cover behaviour to get better interface
class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


# usage defaultdict from collection module
class VisitsCollection:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)
