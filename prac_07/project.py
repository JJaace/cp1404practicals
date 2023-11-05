class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def load_projects(self):
        projects = []
        try:
            with open(self, 'r') as file:
                file.readline()
                for line in file:
                    project_data = line.strip().split('\t')
                    name, start_date, priority, cost_estimate, completion_percentage = project_data
                    project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                    projects.append(project)
            print(f"Loaded {len(projects)} projects")
        except FileNotFoundError:
            print(f"{self} not found.")
        return projects

    def display_projects(self):
        if not self:
            print("No file found, please load file")
        else:
            incomplete = sorted([project for project in self if project.completion_percentage < 100],
                                key=lambda p: p.priority)
            completed = sorted([project for project in self if project.completion_percentage == 100],
                               key=lambda p: p.priority)

            print("Incomplete projects:")
            for i, project in enumerate(incomplete):
                print(
                    f"{i} {project.name}, start: {project.start_date}, priority {project.priority}"
                    f", estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

            print("Completed projects:")
            for i, project in enumerate(completed):
                print(
                    f"{i} {project.name}, start: {project.start_date}, priority {project.priority}"
                    f", estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    def add_new_project(self, name, start_date, priority, cost_estimate, completion_percentage):
        new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        self.append(new_project)
        print(f"{new_project} Added")

    def save_file(self, projects):
        if not self:
            print("No file found, please load file")
        else:
            with open(self, 'w') as file:
                header = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n"
                file.write(header)
                for project in projects:
                    file.write(str(project) + '\n')
                print(f"{len(projects)} projects has been saved to '{self}'")

    def update_project_display(self):
        projects = sorted([project for project in self if project.completion_percentage < 100],
                          key=lambda p: p.priority)

        for i, project in enumerate(projects):
            print(
                f"{i} {project.name}, start: {project.start_date}, priority {project.priority}"
                f", estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    def update_project(self):
        if not self:
            print("No file found, please load file")
        else:
            Project.update_project_display(self)
            try:
                project_choice = int(input("Project choice: "))
            except ValueError:
                print("Enter valid project number")

            try:
                project_choice = int(project_choice)
                if 0 <= project_choice < len(self):
                    project = self[project_choice]
                    print(project)

                    new_completion = input("New Percentage: ")
                    if new_completion:
                        project.completion_percentage = int(new_completion)

                    new_priority = input("New Priority: ")
                    if new_priority:
                        project.priority = int(new_priority)

                    print("Project updated")
                else:
                    print("Please select a valid project number.")
            except ValueError:
                print("Please enter a valid project number.")
