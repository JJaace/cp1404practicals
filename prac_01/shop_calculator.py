items = int(input("Number of items: "))

while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))

total = 0

for item in range(items):
    item = float(input("Enter item: "))
    total += item

print(f"Total price for {items} items is ${total:.2f}")
