import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        pygame.init()

        # Create a screen with height and width
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess Game')
        self.game = Game()

    def mainLoop(self):

        game = self.game
        screen = self.screen

        while True:

            game.show_board(screen)
            game.show_pieces(screen)

            for event in pygame.event.get(): # Press, mouse clicking, etc. to check if the user is leaving
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                
                # Move piece
                if event.type == pygame.MOUSEMOTION:
                    pass
                
                # Release
                if event.type == pygame.MOUSEBUTTONUP:
                    pass    
                
                # Quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.mainLoop()