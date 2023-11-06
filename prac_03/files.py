file = open('name.txt', 'w')
user_name = input("Enter name: ")
file.write(user_name)
file.close()


text = open('name.txt', 'r')
text_name = text.read()
print(f"Your name is {text_name}")

numbers_file = open('numbers.txt', 'r')

line1 = int(numbers_file.readline().strip())
line2 = int(numbers_file.readline().strip())
result = line1 + line2

print(result)

numbers_file = open('numbers.txt', 'r')
total = 0

for line in numbers_file:
    number = int(line.strip())
    total += number

print(total)

