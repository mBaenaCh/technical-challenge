class Answer:
    def __init__(self, id, text, isCorrect):
        self.id = id
        self.text = text
        self.isCorrect = isCorrect
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text = text

    @property
    def isCorrect(self):
        return self._isCorrect
    
    @isCorrect.setter
    def isCorrect(self, isCorrect):
        self._isCorrect = isCorrect

    def __str__(self):
        return self.text + " " +str(self.isCorrect)