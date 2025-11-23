import pygame
from config import screen_width, screen_height

class VisualObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    def draw(self, surface):
        pass

class ImageBasedObject(VisualObject):
    def __init__(self, filename, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(filename)
        self.size = self.image.get_size()

    def get_width():
        return self.size[0]

    def get_height():
        return self.size[1]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))  

class Background(ImageBasedObject):
    def __init__(self):
        super().__init__('assets/backgrounds/green_felt.png', 0, 0)
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        self.size = self.image.get_size()