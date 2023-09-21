def main():
    PASSWORD_LENGTH = 10

    password = get_password(PASSWORD_LENGTH)

    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end=" ")


def get_password(PASSWORD_LENGTH):
    password = input("Enter Password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Password doesn't meet the minimum length")
        password = input("Enter Password: ")
    return password


main()