from game.player import Player, ComputerPlayer
from game.rules import Rules
import pygame

class TurnManager:
    def __init__(self, game, players, deck):
        self.players = players
        self.current_index = 0
        self.round = 1
        self.deck = deck
        self.game = game
        self.current_turn_complete = False
        self.draws_this_turn = 0

    def get_current_player(self):
        """Return the Player whose turn it currently is."""
        return self.players[self.current_index]

    def next_turn(self):
        """
        Advance the game to the next player's turn.
        """
        if self.game.status != "running":
            return

        self.current_index = (self.current_index + 1) % len(self.players)

        if self.current_index == 0:
            self.round += 1

        self.current_turn_complete = False   

    def run_turn(self):
        player = self.get_current_player()

        if isinstance(player, ComputerPlayer):
            pygame.time.wait(500)
            player.take_turn(self.game.state, self.deck)
            self.next_turn()

        elif isinstance(player, Player):
            if self.current_turn_complete:
                self.next_turn()

    