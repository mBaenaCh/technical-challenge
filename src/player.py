class Player:
    def __init__(self, id, username, score, playing):
        self.id = id
        self.username = username
        self.score = score
        self.playing = playing
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    @property
    def playing(self):
        return self._playing
    
    @playing.setter
    def playing(self, playing):
        self._playing = playing

    def __str__(self):
        return self.username + " " + str(self.score) + " " + str(self.playing)