class Category:
    def __init__(self, id, dificulty, name):
        self.id = id
        self.dificulty = dificulty
        self.name = name

    def __str__(self):
        return self.name + " " + self.dificulty