class Answer:
    def __init__(self, id, text, isCorrect):
        self.id = id
        self.text = text
        self.isCorrect = isCorrect
    
    def __str__(self):
        return self.text + " " +self.isCorrect