from abc import ABC, abstractmethod


class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boil water")

    def pour_in_cup(self):
        print("Brew")

    @abstractmethod
    def add_condiments(self):
        pass

    @abstractmethod
    def brew(self):
        pass

class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

class Tea(Beverage):
    def brew(self):
        print("Steeping the tee")

    def add_condiments(self):
        print("Adding lemon")