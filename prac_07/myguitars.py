from guitar import Guitar

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
