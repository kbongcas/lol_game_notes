class Note:
    
    def __init__(self, game, note):
        self.game = game
        self.note = note 

    def __str__(self):
        return str(self.game) + " " +  self.note
