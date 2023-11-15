"""Estimate: 1 hour
   Actual: 1 hour 20 minutes"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable car"""
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """only drives the car if random number is less than the reliability"""
        random_number = random.randint(1, 100)
        if random_number < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
