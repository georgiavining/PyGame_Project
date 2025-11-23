from game.deck import Deck
from game.player import Player, ComputerPlayer
from game.state import GameState

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [ComputerPlayer("Computer"), Player("You")]
        self.state = GameState()
        # self.rules = Rules(self)
        # self.turn_manager = TurnManager(self.players)

    def start(self):
        self.deck.shuffle()
        self.deck.deal(self.players)

    def update(self):
        pass