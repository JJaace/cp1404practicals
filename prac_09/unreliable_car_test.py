"""Estimate: 1 hour
   Actual: 1 hour 20 minutes"""

from unreliable_car import UnreliableCar

my_car = UnreliableCar("Ol Reliable", 100, 50)
distance_driven = my_car.drive(20)
print(my_car)
print(f"Distance driven: {distance_driven} km")
