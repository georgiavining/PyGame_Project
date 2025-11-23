import pygame
from game.game import Game
from ui.main_screen import MainScreen

def main():
    pygame.init()
    pygame.display.set_caption("Notty")
    
    game = Game()
    game.start()
    
    screen = MainScreen(game)
    screen.run()

    pygame.quit()

if __name__ == "__main__":
    main()
