"""
Estimate: 1 hour
Actual: 2 hours"""

from prac_06.guitar import Guitar


def get_valid_input(prompt, data_type, error_message="Invalid input. Please enter a valid value."):
    while True:
        try:
            user_input = data_type(input(prompt))
            if user_input < 0:
                print("Invalid.")
                continue
            return user_input
        except ValueError:
            print(error_message)


def main():
    print("My Guitars!")

    guitars = []

    name = input("Name: ")

    while name != "":
        year = get_valid_input("Year: ", int, "Invalid year. Please enter a valid year.")
        cost = get_valid_input("Cost: $", float, "Invalid cost. Please enter a valid cost.")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar)

        name = input("Name: ")

    print("\nThese are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    max_cost_length = max(len(f"{guitar.cost:.2f}") for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_info = "(vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}:\t{guitar.name:{max_name_length}} ({guitar.year})"
            f", worth ${guitar.cost:>{max_cost_length}.2f} {vintage_info}")


if __name__ == "__main__":
    main()
