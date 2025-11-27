import pygame
import random
from game.card import Card
from config import colours, numbers, deck_x, deck_y, card_width, card_height
from ui.visual_objects import ImageBasedObject

class Deck(ImageBasedObject):
    def __init__(self, x=deck_x, y=deck_y):
        super().__init__("assets/cards/back.png", x=x, y=y)
        self.image = pygame.transform.scale(self.image, (card_width, card_height))
        self.size = self.image.get_size()
        
        self.cards = [Card(col, int(num)) for _ in range(2) for col in colours for num in numbers]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, players, cards_per_player=4):
        for player in players:
            if len(self.cards) == 0:
                break
            player.hand.add_to_hand(self.draw_from_deck(cards_per_player))
        
    def draw_from_deck(self, num):
        if len(self.cards) == 0:
            return []
        return [self.cards.pop() for _ in range(min(num, len(self.cards)))]

    def add_to_deck(self, cards):
        if not isinstance(cards, list):
            cards = [cards]
        self.cards.extend(cards)
        random.shuffle(self.cards)