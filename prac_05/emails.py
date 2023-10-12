"""

emails
Estimate: 1 hour
Actual: 1 hour 20 minutes

"""


def get_name(email):
    split = email.split('@')[0].split('.')
    format_name = " ".join(name.title() for name in split)
    return format_name


def main():
    user_data = {}

    email = input("Email: ")

    while email != "":
        name = get_name(email)
        user_input = input(f"Is your name {name}? (Y/n) ").lower()

        if user_input == "y" or user_input == "":
            user_data[email] = name
        elif user_input == "n":
            custom_name = input("Name: ")
            user_data[email] = custom_name

        email = input("Email: ")

    for email, name in user_data.items():
        print(f"{name} ({email})")


main()
