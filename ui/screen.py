import pygame
from ui.sprites import Background
from config import screen_width, screen_height
from pygame.locals import *

class Screen:
    def __init__(self):
        self.background = Background()
        self.objects = [self.background]
        self.close = False
        self.next_screen = None

    def process_event(self, event):
        pass

    def update_objects(self):
        pass
        
    def run(self):
        surface = pygame.display.set_mode((screen_width, screen_height))

        # Main pygame loop
        while not self.close:
            for event in pygame.event.get():
                if event.type == QUIT:
                    current_screen = None
                    return

                self.process_event(event)

            self.update_objects()
            
            for o in self.objects:
                o.draw(surface)
            
            pygame.display.flip()
            pygame.time.wait(10)

        return self.next_screen