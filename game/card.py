import pygame
from ui.sprites import ImageBasedObject
from config import card_width, card_height

class Card(ImageBasedObject):
    def __init__(self, colour, number):
        self.colour = colour
        self.number = number

        super().__init__(f"assets/cards/{self.number}_of_{self.colour}.png", x=0, y=0)
        self.image = pygame.transform.scale(self.image, (card_width, card_height))
        self.size = self.image.get_size()