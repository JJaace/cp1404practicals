"""Estimate: 5 hours"""

"""Priority Queue
1 - Load projects
2 - Display projects
3 - Add new project
4 - filter project by date
5 - Update project
6 - Save Projects"""

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
        Project.display_projects(projects)
    elif user_input == "F":
        print("Filter")
    elif user_input == "A":
        project_name = input("Enter the project name:")
        start_date = input("Enter the start date (DD/MM/YYYY): ")
        priority = int(input("Enter the priority: "))
        cost_estimate = float(input("Enter the cost estimate: "))
        completion_percentage = int(input("Enter the completion percentage: "))
        Project.add_new_project(projects, project_name, start_date, priority, cost_estimate, completion_percentage)
    elif user_input == "U":
        print("Update")
    elif user_input != "Q":
        print("Invalid Input")

print("Quit")
