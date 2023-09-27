"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when a decimal number is entered in either a numerator or denominator
2. When will a ZeroDivisionError occur?
when a 0 is entered for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")