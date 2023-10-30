class Guitar:
    """Represents a guitar with attributes with its name, year and cost"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Gets the age of the guitar"""
        CURRENT_YEAR = 2023
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Checks if the guitar is vintage"""
        VINTAGE = 50
        return self.get_age() >= VINTAGE

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f} added."
