class Round:
    def __init__(self, id, number, award, questionId):
        self.id = id
        self.number = number
        self.award = award
        self.questionId = questionId

    def __str__(self):
        return self.number + " " + self.award + " " + self.questionId