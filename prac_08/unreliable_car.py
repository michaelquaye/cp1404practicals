import random

from prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.reliability = 70
    def drive(self, distance):
        if self.reliability >= random.randint(0,101):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
            print('broken')
        return distance_driven
    def __str__(self):
        return "{}".format(super().__str__())