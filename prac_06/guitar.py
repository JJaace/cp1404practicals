class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = 2023
        age = current_year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f} added."