"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

amount = int(input("Enter amount: "))
while amount >= 0:
    if amount < 1000 and amount >= 0:
        bonus = amount * 0.1
        print(f"Your bonus is ${bonus}")
    elif amount >= 1000:
        bonus = amount * 0.15
        print(f"Your bonus is ${bonus}")
    amount = int(input("Enter amount: "))
