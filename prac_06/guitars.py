from prac_06.guitar import Guitar


def main():
    print("My Guitars!")

    guitars = []
    guitar_number = 1

    name = input("Name: ")

    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
            name = input("Name: ")
            continue

        if year < 0 or cost < 0:
            print("Year and cost must be non-negative.")
            name = input("Name: ")
            continue

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar)
        guitar_number += 1

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
