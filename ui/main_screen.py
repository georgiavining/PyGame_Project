from ui.screen import Screen
from game.deck import Deck
from config import screen_width, screen_height, card_width, card_height, max_spacing, min_spacing, overlap_offset, hand_gap, deck_x, deck_y
from ui.layout import get_hand_layout

class MainScreen(Screen):
    def __init__(self, game):
        super().__init__() 
        self.game = game

        #placing deck in middle (& making it appear slightly stacked)
        self.deck_stack = [Deck(deck_x + 2*n, deck_y - 2*n) for n in range(3)]
        
        self.computer_cards = self.game.players[0].hand.cards
        self.player_cards = self.game.players[1].hand.cards

        self.objects += self.deck_stack + self.computer_cards + self.player_cards

    def update_objects(self):
        #placing computer hand at top
        computer_layout = get_hand_layout(len(self.computer_cards), screen_width, card_width, max_spacing, min_spacing)
        
        for row_index, (row,spacing) in enumerate(computer_layout):
            total_width = (len(row) - 1) * spacing + card_width
            computer_x = (screen_width - total_width) // 2
            computer_y = deck_y - card_height - hand_gap - row_index * (card_height - overlap_offset)
            
            for i, index in enumerate(row):
                card = self.computer_cards[index]
                card.x = computer_x + i * spacing
                card.y = computer_y
                
        #placing player hand at bottom
        player_layout = get_hand_layout(len(self.player_cards), screen_width, card_width, max_spacing, min_spacing)
        
        for row_index, (row,spacing) in enumerate(player_layout):
            total_width = (len(row) - 1) * spacing + card_width
            player_x = (screen_width - total_width) // 2
            player_y = deck_y + card_height + hand_gap + row_index * (card_height - overlap_offset)
            
            for i, index in enumerate(row):
                card = self.player_cards[index]
                card.x = player_x + i * spacing
                card.y = player_y