from guitar import Guitar


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


guitars = []
with open("guitars.csv", "r") as file:
    for line in file:
        name, year, cost = line.strip().split(',')
        year = int(year)
        cost = float(cost)
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

print("Guitars:")
for guitar in guitars:
    print(guitar)

guitars.sort()
print("\nSorted by year (oldest to newest):")
for guitar in guitars:
    print(guitar)

name = input("Name: ")

new_guitars = []
while name != "":
    year = get_valid_input("Year: ", int, "Invalid year. Please enter a valid year.")
    cost = get_valid_input("Cost: $", float, "Invalid cost. Please enter a valid cost.")

    guitar = Guitar(name, year, cost)
    new_guitars.append(guitar)
    print(guitar)

    name = input("Name: ")

with open("guitars.csv", "a") as file:
    for guitar in new_guitars:
        file.write(f"\n{guitar.name},{guitar.year},{guitar.cost:.2f}")

print("Data saved to guitars.csv")
