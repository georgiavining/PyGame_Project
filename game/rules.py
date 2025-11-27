from itertools import combinations
from game.card import Card

class Rules:
    @staticmethod
    def is_valid_group(group):
        for item in group:
            if not hasattr(item, "colour") or not hasattr(item, "number"):
                return False
        
        colours = {c.colour for c in group}
        numbers = {int(c.number) for c in group}
        if len(group)>=3 and len(colours) == 1:
            sorted_nums = sorted(numbers)
            if all(sorted_nums[i] + 1 == sorted_nums[i+1] for i in range(len(sorted_nums)-1)):
                return True
        elif len(group)>=4 and len(colours) == len(group) and len(numbers) == 1:
            return True
        return False
    
    @staticmethod
    def find_valid_groups(hand):
        cards = []
        n = len(hand)
        valid_groups = []

        if n >= 3:
            for size in range(3, n+1):
                for group in combinations(hand.cards, size):
                    if Rules.is_valid_group(group):
                        valid_groups.append(group)
        return valid_groups

    @staticmethod
    def has_won(player):
        if len(player.hand) == 0:
            return True
        else:
            return False

    

        
        