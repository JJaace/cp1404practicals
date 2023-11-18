"""Estimate: 2 hours
   Actual: 3 hours"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    user_input = ""
    while user_input != "q":
        print("q)uit, c)hoose taxi, d)rive")
        user_input = input(">>> ").lower()

        if user_input == 'q':
            break
        elif user_input == 'c':
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            except (ValueError, IndexError):
                print("Invalid taxi choice")
                print(f"Bill to date: ${bill_to_date:.2f}")
        elif user_input == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                bill_to_date += cost
                print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

main()
