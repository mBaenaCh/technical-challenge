class Category:
    def __init__(self, id, dificulty, name):
        self.id = id
        self.dificulty = dificulty
        self.name = name

    @property
    def dificulty(self):
        return self._difficulty

    @dificulty.setter
    def dificulty(self, dificulty):
        self._difficulty = dificulty

    def __str__(self):
        return  str(self.id)+ " " + self.name + " " + str(self.dificulty)