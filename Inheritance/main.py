class Vehicle:
    def __init__(self) -> None:
        self.turn_on()

    def turn_on(self):
        print('starting engine!')


class Car(Vehicle):
    pass


car = Car()
