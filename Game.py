class Game:
    
    def __init__(self, win, rolePlayed, champPlayed, score, goldCount):
        self.win = win
        self.rolePlayed = rolePlayed
        self.champPlayed = champPlayed
        self.score = score
        self.goldCount = goldCount

    def __str__(self):
        return "{} {} {} {} {}".format(self.win, self.rolePlayed, self.champPlayed, self.score, self.goldCount)
