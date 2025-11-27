from game.player import Player, ComputerPlayer

class GameState:
    def __init__(self):
        self.players = [ComputerPlayer("Computer"), Player("You")]

