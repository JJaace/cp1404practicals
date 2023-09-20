PROMPT = ("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit")

name = input("Enter name: ").title()
print(PROMPT)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(PROMPT)
    choice = input(">>> ").upper()

print("Finished.")
