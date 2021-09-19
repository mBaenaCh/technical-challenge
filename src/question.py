class Question:
    def __init__(self, id, title, categoryId, answerId):
        self.id = id
        self.title = title
        self.categoryId = categoryId
        self.answerId = answerId
    
    def __str__(self):
        return self.title + " " + self.categoryId + " " +self.answerId