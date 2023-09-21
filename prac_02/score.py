import random

def main():
    score = float(input("Enter score: "))

    result = calculate_score(score)
    rand_score = random_score()
    random_result = calculate_score(rand_score)

    print(f"Your result is {result}")
    print(f"Random result is {random_result}({rand_score})")

def random_score():
    random_score = random.randint(100, 100)
    return random_score
def calculate_score(score):
    if score >= 0 and score < 50:
        result = "Bad"
    elif score >= 50 and score < 90:
        result = "Passable"
    elif score >= 90 and score <= 100:
        result = "Excellent"
    else:
        result = "Invalid"
    return result


main()