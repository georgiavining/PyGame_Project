class Hand:
    def __init__(self):
        self.cards = []

    def add_to_hand(self, cards):
        self.cards.extend(cards)

    def remove_group(self, group):
        for card in group:
            self.cards.remove(card)
