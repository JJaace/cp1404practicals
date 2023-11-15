"""Estimate: 1 hour
   Actual: 1 hour 40 minutes"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Taxi 1", 100, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(f"The total of your fare is ${silver_service_taxi.get_fare()}")


main()
