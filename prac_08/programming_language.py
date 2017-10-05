class ProgrammingLanguage:
    def __init__(self, name, typing, is_reflection, year):
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year
    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        return ('{}, {} Typing, Reflection = {}, First appeared in {}'.format(self.name, self.typing, self.is_reflection, self.year))
