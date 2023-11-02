"""Estimate: 5 hours"""

"""Priority Queue
1 - Load projects
2 - Save Projects
3 - Display projects
4 - Add new project
5 - filter project by date
6 - Update project"""

from prac_07.project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (Q)uit")

projects = []

user_input = ""
while user_input != "Q":
    print(MENU)
    user_input = input(">>> ").upper()
    if user_input == "L":
        filename = input("Enter filename to load projects from: ") + ".txt"
        projects = Project.load_projects(filename)
    elif user_input == "S":
        print("Save")
    elif user_input == "D":
        print("Display")
    elif user_input == "F":
        print("Filter")
    elif user_input == "A":
        print("Add")
    elif user_input == "U":
        print("Update")
    elif user_input != "Q":
        print("Invalid Input")

print("Quit")
