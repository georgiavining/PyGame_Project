from game.hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

class ComputerPlayer(Player):
    pass
