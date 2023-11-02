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
        incomplete = sorted([project for project in self if project.completion_percentage < 100],
                            key=lambda p: p.priority)
        completed = sorted([project for project in self if project.completion_percentage == 100],
                           key=lambda p: p.priority)

        print("Incomplete projects:")
        for project in incomplete:
            print(
                f"  {project.name}, start: {project.start_date}, priority {project.priority}"
                f", estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

        print("Completed projects:")
        for project in completed:
            print(
                f"  {project.name}, start: {project.start_date}, priority {project.priority}"
                f", estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")
