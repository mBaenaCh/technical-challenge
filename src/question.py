class Question:
    def __init__(self, id, title, category_id, answer_list):
        self.id = id
        self.title = title
        self.category_id = category_id
        self.answer_list = answer_list

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def answer_list(self):
        return self._answer_list
    
    @answer_list.setter
    def answer_list(self, answer_list):
        self._answer_list = answer_list

    def __str__(self):
        return str(self.id)+ " " + self.title + " " + str(self.category_id)
