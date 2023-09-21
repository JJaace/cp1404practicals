def main():
    PROMPT = ("(G)et a valid score (must be 0-100 inclusive)\n"
              "(P)rint result\n"
              "(S)how stars\n"
              "(Q)uit")

    print(PROMPT)
    choice = input(">>> ").upper()
    score = ""
    result = ""
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == "":
                print("Get valid score first")
            else:
                result = calculate_score(score)
                print(result)
        elif choice == "S":
            if result == "":
                print("Get result first")
            else:
                stars = print_asterisks(result)
                print(stars)
        else:
            print("Invalid choice")
        print(PROMPT)
        choice = input(">>> ").upper()

    print("Farewell.")
def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score
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

def print_asterisks(result):
    asterisks = "*" * len(result)
    return asterisks

main()
