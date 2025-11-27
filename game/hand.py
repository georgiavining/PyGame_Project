import random

class Hand:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)

    def add_to_hand(self, cards):
        self.cards.extend(cards)

    def remove_group(self, group):
        for card in group:
            if card in self.cards:
                self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
