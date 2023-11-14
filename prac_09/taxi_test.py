from prac_09.taxi import Taxi

my_taxi = Taxi(100, "prius 1", 1.23)
my_taxi.drive(40)
print(f"Taxi drove 40 km:"
      f"\n{my_taxi}"
      f"\nCurrent Fare: ${my_taxi.get_fare():.2f}\n")

my_taxi.start_fare()
my_taxi.drive(100)
print(f"Taxi 100 km:"
      f"\n{my_taxi}"
      f"\nCurrent Fare: ${my_taxi.get_fare():.2f}")
