class Vehicle:
    def __init__(self, wheels=0) -> None:
        self.wheels = wheels
        self.turn_on()

    def turn_on(self):
        print('starting engine!')


class Car(Vehicle):
    pass


car = Car(wheels=4)
print(car.wheels)