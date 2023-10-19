class ProgrammingLanguage:
    def __init__(self, name="Language", typing="Type", reflection=False, appeared=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.appeared = appeared

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.appeared}"
