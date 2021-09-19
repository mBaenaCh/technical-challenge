class Question:
    def __init__(self, id, title, categoryId, answer_list):
        self.id = id
        self.title = title
        self.categoryId = categoryId
        self.answer_list = answer_list

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def categoryId(self):
        return self._categoryId

    @categoryId.setter
    def categoryId(self, categoryId):
        self._categoryId = categoryId

    @property
    def answer_list(self):
        return self._answer_list
    
    @answer_list.setter
    def answer_list(self, answer_list):
        self._answer_list = answer_list

    def __str__(self):
        return str(self.id)+ " " + self.title + " " + str(self.categoryId)
